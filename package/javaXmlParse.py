import xml.etree.ElementTree as ET


class XmlParse:
    def __init__(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        root_children = [e for e in root]  # TODO
        root_attrib = root.attrib
        self.name = root_attrib.get("name")
        # self.version = root_attrib.get("version") # dosen't exist
        # self.timestamp = root_attrib.get("timestamp") # dosen't exist
        # self.lines_valid = root_attrib.get("lines-valid") # need calc
        # self.lines_covered = root_attrib.get("lines-covered") # need calc
        # self.line_rate = root_attrib.get("line-rate") # need calc
        # self.branches_covered = root_attrib.get("branches-covered") # need calc
        # self.branches_valid = root_attrib.get("branches-valid")
        # self.branch_rate = root_attrib.get("branch-rate") # need calc
        # self.complexity = root_attrib.get("complexity") # is with in methode
        self.sessionInfo = []
        for source in root_children:
            if source.tag == "sessioninfo":
                self.sessionInfo.append(SessionInfoType(source))

        self.packages = []
        for package in root_children:
            if package.tag == "package":
                self.packages.append(PackageType(package))


class SessionInfoType:
    def __init__(self, sessionInfo):
        self.id = sessionInfo.get("id")
        self.start = sessionInfo.get("start")
        self.dump = sessionInfo.get("dump")


class SourceType:
    def __init__(self, source):
        self.lines = [LineType(line) for line in source]


class PackageType:
    def __init__(self, package):
        package_attrib = package.attrib
        self.name = package_attrib.get("name")
        # self.line_rate = package_attrib.get("line-rate") # need calc
        # self.branch_rate = package_attrib.get("branch-rate") # need calc
        # self.complexity = package_attrib.get("complexity") # is with in methode
        self.classes = []
        for _class in package:
            if _class.tag == "class":
                self.classes.append(ClassType(_class))
        self.sourcefiles = []
        for sourcefile in package:
            if sourcefile.tag == "sourcefile":
                self.sourcefiles.append(SourceType(sourcefile))
        # TODO still missing counter tag


class ClassType:
    def __init__(self, _class):
        class_attrib = _class.attrib
        self.name = class_attrib.get("name")
        self.filename = class_attrib.get("filename")
        self.complexity = class_attrib.get("complexity")
        self.line_rate = class_attrib.get("line-rate")
        self.branch_rate = class_attrib.get("branch-rate")
        self.methods = []
        for method in _class:
            if method.tag == "method":
                self.methods.append(MethodType(method))
        # self.lines = [LineType(line) for line in _class[1]] # with in methode


class MethodType:
    def __init__(self, method):
        method_attrib = method.attrib
        self.name = method_attrib.get("name")
        self.desc = method_attrib.get("desc")


class LineType:
    def __init__(self, line):
        line_attrib = line.attrib
        # TODO not sure!!!
        self.number = line_attrib.get("nr")
        self.hits = line_attrib.get("ci")


if __name__ == "__main__":
    dataType = XmlParse("../jacoco.xml")
    print("done")
