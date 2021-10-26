import xml.etree.ElementTree as ET


class XmlParse:
    def __init__(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        # root attrib
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
        # sources
        self.sources = [SourceType(source) for source in root[0]]  # TODO not by index but by name
        # packages
        self.packages = [PackageType(package) for package in root[1]]  # TODO not by index but by name


class SourceType:
    def __init__(self, source):
        self.path = source.text


class PackageType:
    def __init__(self, package):
        package_attrib = package.attrib
        self.name = package_attrib.get("name")
        self.line_rate = package_attrib.get("line-rate")
        self.branch_rate = package_attrib.get("branch-rate")
        self.complexity = package_attrib.get("complexity")
        self.classes = [ClassType(_class) for _class in package[0]]  # TODO not by index but by name


class ClassType:
    def __init__(self, _class):
        class_attrib = _class.attrib
        self.name = class_attrib.get("name")
        self.filename = class_attrib.get("filename")
        self.complexity = class_attrib.get("complexity")
        self.line_rate = class_attrib.get("line-rate")
        self.branch_rate = class_attrib.get("branch-rate")
        self.methods = [method for method in _class[0]]  # TODO not by index but by name
        self.lines = [LineType(line) for line in _class[1]]  # TODO not by index but by name


class LineType:
    def __init__(self, line):
        line_attrib = line.attrib
        self.number = line_attrib["number"]
        self.hits = line_attrib["hits"]


if __name__ == "__main__":
    dataType = XmlParse("../coverage.xml")
    print("done")
