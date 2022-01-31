import xml.etree.ElementTree as ET
from collections import namedtuple
if __name__ == "__main__":
    import time


class XmlParse:
    def __init__(self, path):
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
    filename = "../coverage_c.xml"
    print(f"report for: {filename}")
    dataType = XmlParse(filename)
    print(f"executing took: {int((time.time() - start)*1000)}ms")
    print("done")
    print(dataType.basic_report())
