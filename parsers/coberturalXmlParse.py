import xml.etree.ElementTree as ET
import requests
import json
from collections import namedtuple
if __name__ == "__main__":
    import time


class XmlParse:
    def __init__(self, path=None, from_dict=None):
        if path:
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
                    self.sources = [SourceType(source) for source in root[0]]
                elif child.tag == "packages":
                    self.packages = [PackageType(package) for package in root[1]]
        elif from_dict:
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
                self.sources = from_dict.get("sources")  # TODO convert to Types
                self.packages = from_dict.get("packages")  # TODO convert to Types
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
            "packages": [{# "path": package.path,
                          "path": "test path",
                          "line-rate": int(package.line_rate),
                          "branch-rate": int(package.branch_rate),
                          "complexity": int(package.complexity),
                          "classes": [{# "path": _class.path,
                                       "path": "test path",
                                       "name": _class.name,
                                       "complexity": int(_class.complexity),
                                       "line-rate": int(_class.line_rate),
                                       "branch-rate": int(_class.branch_rate),
                                       "methods": [],
                                       "lines": [{"number": int(line.number),
                                                  "hits": int(line.hits),
                                                  } for line in _class.lines]
                                       } for _class in package.classes],
                          } for package in self.packages],
        }

    def to_api_db(self, url):
        data = self.to_dict()
        print(data)
        headers = {'Content-type': 'application/json'}
        x = requests.post(url, json=json.dumps(data), headers=headers)
        print(x.status_code)

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
    # @memory_profiler.profile
    def __init__(self, source):
        self.path = source.text

    def to_dict(self):
        return {
            # "path": self.path,
            "path": "test path",
        }


PackageTypeTuple = namedtuple('PackageType', 'path line_rate branch_rate complexity classes')
ClassTypeTuple = namedtuple('classType', 'name path complexity line_rate branch_rate methods lines')
LineTypeTuple = namedtuple('lineType', 'number hits')


def PackageType(package) -> PackageTypeTuple:
    package_attrib = package.attrib
    classes = []
    for child in package:
        if child.tag == "classes":
            classes = [ClassType(_class) for _class in child]
    return PackageTypeTuple(package_attrib.get("name"), package_attrib.get("line-rate"),
                            package_attrib.get("branch-rate"), package_attrib.get("complexity"), classes)


def ClassType(_class) -> ClassTypeTuple:
    class_attrib = _class.attrib
    methods = []
    lines = []
    for child in _class:
        if child.tag == "method":
            methods = [method for method in child]
        elif child.tag == "lines":
            lines = [LineType(line) for line in child]
    return ClassTypeTuple(class_attrib.get("name"), class_attrib.get("filename"), class_attrib.get("complexity"),
                          class_attrib.get("line-rate"), class_attrib.get("branch-rate"), methods, lines)


def LineType(line) -> LineTypeTuple:
    line_attrib = line.attrib
    return LineTypeTuple(line_attrib.get("number"), line_attrib.get("hits"))


if __name__ == "__main__":
    start = time.time()
    # filename = "../coverage_c.xml"
    filename = "../coverage.xml"
    print(f"report for: {filename}")
    dataType = XmlParse(filename)
    print(f"executing took: {int((time.time() - start)*1000)}ms")
    print("done")
    print(dataType.basic_report())

    project_id = "TestProject"
    commit_id = "TestCommit"
    url = f'http://localhost:8080/Cover-Rest/Interface-API/1.0.8/{project_id}/{commit_id}/write_coverage'

    dataType.to_api_db(url)
