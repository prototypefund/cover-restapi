import xml.etree.ElementTree as ET
if __name__ == "__main__":
    import time
    # import memory_profiler


class XmlParse:
    # @memory_profiler.profile
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


class PackageType:
    # @memory_profiler.profile
    def __init__(self, package):
        package_attrib = package.attrib
        self.path = package_attrib.get("name")
        self.line_rate = package_attrib.get("line-rate")
        self.branch_rate = package_attrib.get("branch-rate")
        self.complexity = package_attrib.get("complexity")
        self.classes = []
        for child in package:
            if child.tag == "classes":
                self.classes = [ClassType(_class) for _class in child]


class ClassType:
    # @memory_profiler.profile
    def __init__(self, _class):
        class_attrib = _class.attrib
        self.name = class_attrib.get("name")
        self.path = class_attrib.get("filename")
        self.complexity = class_attrib.get("complexity")
        self.line_rate = class_attrib.get("line-rate")
        self.branch_rate = class_attrib.get("branch-rate")
        self.methods = []
        self.lines = []
        for child in _class:
            if child.tag == "method":
                self.methods = [method for method in child]
            elif child.tag == "lines":
                self.lines = [LineType(line) for line in child]


class LineType:
    # @memory_profiler.profile
    def __init__(self, line):
        line_attrib = line.attrib
        self.number = line_attrib["number"]
        self.hits = line_attrib["hits"]


if __name__ == "__main__":
    start = time.time()
    filename = "../coverage_c.xml"
    print(f"report for: {filename}")
    dataType = XmlParse(filename)
    print(f"executing took: {int((time.time() - start)*1000)}ms")
    print("done")
    print(dataType.basic_report())
