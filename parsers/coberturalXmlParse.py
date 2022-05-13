import xml.etree.ElementTree as ET
import requests
import json
import os.path
from collections import namedtuple

if __name__ == "__main__":
    import time


class XmlParse:
    # TODO from data to xml file
    def __init__(self, path=None, from_dict=None):
        if path is not None:
            tree = ET.parse(path)
            root = tree.getroot()
            root_attrib = root.attrib
            self.version = root_attrib.get("version")
            self.timestamp = root_attrib.get("timestamp")
            self.lines_valid = root_attrib.get("lines-valid")
            self.lines_covered = root_attrib.get("lines-covered")
            self.line_rate = root_attrib.get("line-rate")
            self.branches_covered = root_attrib.get("branches-covered")
            self.branches_valid = root_attrib.get("branches-valid")
            self.branch_rate = root_attrib.get("branch-rate")
            self.complexity = root_attrib.get("complexity")
            self.sources = []
            self.packages = []
            for child in root:
                if child.tag == "sources":
                    self.sources = [SourceType(source=source) for source in root[0]]
                elif child.tag == "packages":
                    self.packages = [PackageType(package=package) for package in root[1]]
        elif from_dict is not None:
            try:
                from_dict = dict(from_dict)
                self.version = from_dict.get("version")
                self.timestamp = from_dict.get("timestamp")
                self.lines_valid = from_dict.get("lines-valid")
                self.lines_covered = from_dict.get("lines-covered")
                self.line_rate = from_dict.get("line-rate")
                self.branches_covered = from_dict.get("branches-covered")
                self.branches_valid = from_dict.get("branches-valid")
                self.branch_rate = from_dict.get("branch-rate")
                self.complexity = from_dict.get("complexity")
                self.sources = [SourceType(from_dict=source) for source in from_dict.get("sources")]
                self.packages = [PackageType(from_dict=package) for package in from_dict.get("packages")]
            except Exception as e:
                print(e)
                raise Exception("error at from_dict failed initialize XMLParse")
        else:
            raise Exception("need path or from_dict to initialize XMLParse")

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "timestamp": self.timestamp,
            "lines-valid": int(self.lines_valid),
            "lines-covered": int(self.lines_covered),
            "line-rate": int(self.line_rate),
            "branches-covered": int(self.branches_covered),
            "branches-valid": int(self.branches_valid),
            "branch-rate": int(self.branch_rate),
            "complexity": int(self.complexity),
            "sources": [source.to_dict() for source in self.sources],
            "packages": [package.to_dict() for package in self.packages],
        }

    def to_api_db(self, _url):
        data = self.to_dict()
        headers = {'Content-type': 'application/json'}
        x = requests.post(_url, json=json.dumps(data), headers=headers)
        print(x.status_code)

    def to_xml_file(self, _filename):
        if not _filename.endswith('.xml'):
            raise Exception("filename must end with .xml")
        coverage = ET.Element("coverage", {
            "version": self.version,
            "timestamp": self.timestamp,
            "lines-valid": self.lines_valid,
            "lines-covered": self.lines_covered,
            "line-rate": self.line_rate,
            "branches-covered": self.branches_covered,
            "branches-valid": self.branches_valid,
            "branch-rate": self.branch_rate,
            "complexity": self.complexity,
        })

        sources = ET.SubElement(coverage, "sources")
        for source in self.sources:
            ET.SubElement(sources, "source").text = source.path

        packages = ET.SubElement(coverage, "packages")
        for package in self.packages:
            package_element = ET.SubElement(packages, "package", {
                "name": package.path,
                "line-rate": package.line_rate,
                "branch-rate": package.branch_rate,
                "complexity": package.complexity,
            })

            classes = ET.SubElement(package_element, "classes")
            for _class in package.classes:
                _class_element = ET.SubElement(classes, "class", {
                    "name": _class.name,
                    "filename": _class.path,
                    "complexity": _class.complexity,
                    "line-rate": _class.line_rate,
                    "branch-rate": _class.branch_rate,
                })

                methods = ET.SubElement(_class_element, "methods")

                lines = ET.SubElement(_class_element, "lines")
                for line in _class.lines:
                    line_element = ET.SubElement(lines, "line", {
                        "number": line.number,
                        "hits": line.hits,
                    })

        tree = ET.ElementTree(coverage)
        tree.write(_filename, encoding="UTF-8", xml_declaration=True)

    def basic_report(self):
        return {
            "line-rate": self.line_rate,
            "lines-valid": self.lines_valid,
            "lines-covered": self.lines_covered,
        }

    def simple_report(self):
        return {
            "line-rate": self.line_rate,
            "lines-valid": self.lines_valid,
            "lines-covered": self.lines_covered,
            "timestamp": self.timestamp,
            "complexity": self.complexity,
            "packages": [{"path": package.path,
                          "line-rate": package.line_rate,
                          "classes": [{"path": _class.path,
                                       "line-rate": _class.line_rate,
                                       } for _class in package.classes]}
                         for package in self.packages]
        }


class SourceType:
    def __init__(self, source=None, from_dict=None):
        if source is not None:
            self.path = source.text
        elif from_dict is not None:
            self.path = from_dict.get('path')
        else:
            raise Exception("need source or from_dict to initialize SourceType")

    def to_dict(self):
        return {
            "path": self.path,
        }


class PackageType:
    def __init__(self, package=None, from_dict=None):
        if package is not None:
            package_attrib = package.attrib
            classes = []
            for child in package:
                if child.tag == "classes":
                    classes = [ClassType(_class=_class) for _class in child]
            self.path = package_attrib.get("name")
            self.line_rate = package_attrib.get("line-rate")
            self.branch_rate = package_attrib.get("branch-rate")
            self.complexity = package_attrib.get("complexity")
            self.classes = classes
        elif from_dict is not None:
            from_dict = dict(from_dict)
            self.path = from_dict.get("path")
            self.line_rate = from_dict.get("line-rate")
            self.branch_rate = from_dict.get("branch-rate")
            self.complexity = from_dict.get("complexity")
            self.classes = from_dict.get("classes")
        else:
            raise Exception("need package or from_dict to initialize PackageType")

    def to_dict(self):
        return {
            "path": self.path,
            "line-rate": int(self.line_rate),
            "branch-rate": int(self.branch_rate),
            "complexity": int(self.complexity),
            "classes": [_class.to_dict() for _class in self.classes]
        }


class ClassType:
    def __init__(self, _class=None, from_dict=None):
        if _class is not None:
            class_attrib = _class.attrib
            methods = []
            lines = []
            for child in _class:
                if child.tag == "method":
                    methods = [method for method in child]
                elif child.tag == "lines":
                    lines = [LineType(line=line) for line in child]
            self.name = class_attrib.get("name")
            self.path = class_attrib.get("filename")
            self.complexity = class_attrib.get("complexity")
            self.line_rate = class_attrib.get("line-rate")
            self.branch_rate = class_attrib.get("branch-rate")
            self.methods = methods
            self.lines = lines
        elif from_dict is not None:
            from_dict = dict(from_dict)
            self.name = from_dict.get("name")
            self.path = from_dict.get("filename")
            self.complexity = from_dict.get("complexity")
            self.line_rate = from_dict.get("line-rate")
            self.branch_rate = from_dict.get("branch-rate")
            self.methods = from_dict.get("methods")
            self.lines = from_dict.get("lines")
        else:
            raise Exception("need _class or from_dict to initialize ClassType")

    def to_dict(self):
        return {"name": self.name,
                "path": self.path,
                "complexity": int(self.complexity),
                "line-rate": int(self.line_rate),
                "branch-rate": int(self.branch_rate),
                # "methods": [],
                "lines": [line.to_dict() for line in self.lines]
                }


class LineType:
    def __init__(self, line=None, from_dict=None):
        if line is not None:
            line_attrib = line.attrib
            self.number = line_attrib.get("number")
            self.hits = line_attrib.get("hits")
        elif from_dict is not None:
            from_dict = dict(from_dict)
            self.number = from_dict.get("number")
            self.hits = from_dict.get("hits")
        else:
            raise Exception("need line or from_dict to initialize LineType")

    def to_dict(self):
        return {"number": self.number,
                "hits": self.hits,
                }


if __name__ == "__main__":
    start = time.time()
    # filename = "../coverage_c.xml"
    filename = "../coverage.xml"
    print(f"report for: {filename}")
    dataType = XmlParse(filename)
    print(f"executing took: {int((time.time() - start) * 1000)}ms")
    print(dataType.basic_report())

    # project_id = "test_project"
    # commit_id = "test_commit"
    # coverage_id = "test_coverage"
    # url = f'http://localhost:8080/Cover-Rest/Interface-API/1.0.9/{project_id}/{commit_id}/coverage/{coverage_id}'
    #
    # dataType.to_api_db(url)

    dataType.to_xml_file("../coverage_reverse.xml")
