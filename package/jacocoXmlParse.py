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
        self.lines_valid = root_attrib.get("lines-valid")  # TODO need calc
        self.lines_covered = root_attrib.get("lines-covered")  # TODO need calc
        self.line_rate = root_attrib.get("line-rate")  # TODO need calc
        # self.branches_covered = root_attrib.get("branches-covered") # need calc
        # self.branches_valid = root_attrib.get("branches-valid")
        # self.branch_rate = root_attrib.get("branch-rate") # need calc
        # self.complexity = root_attrib.get("complexity") # is with in methode
        self.sessionInfo = []
        self.packages = []
        self.counter = []
        for child in root_children:
            if child.tag == "sessioninfo":
                self.sessionInfo.append(SessionInfoType(child))
            elif child.tag == "package":
                self.packages.append(PackageType(child))
            # TODO handle counter types
            elif child.tag == "counter":
                self.counter.append(CounterType(child))

    def simple_report(self):
        return {
            "line-rate": self.line_rate,
            "lines-valid": self.lines_valid,
            "lines-covered": self.lines_covered,
            "packages": [{"path": package.path,
                          "line-rate": package.line_rate,
                          "classes": [{"path": _class.path,
                                       "line-rate": _class.line_rate,
                                       } for _class in package.classes]}
                         for package in self.packages]
        }


class SessionInfoType:
    def __init__(self, sessionInfo):
        self.id = sessionInfo.get("id")
        self.start = sessionInfo.get("start")
        self.dump = sessionInfo.get("dump")


class SourcefileType:
    def __init__(self, source):
        self.name = source.attrib.get("name")
        self.lines = [LineType(line) for line in source]


class PackageType:
    def __init__(self, package):
        package_attrib = package.attrib
        self.path = package_attrib.get("name")
        self.line_rate = package_attrib.get("line-rate")   # TODO need from Counter
        self.branch_rate = package_attrib.get("branch-rate")   # TODO need from Counter
        self.complexity = package_attrib.get("complexity")   # TODO need from Counter
        self.classes = []
        self.sourcefiles = []
        self.counter = []
        for child in package:
            if child.tag == "class":
                self.classes.append(ClassType(child))
            elif child.tag == "sourcefile":
                self.sourcefiles.append(SourcefileType(child))
            # TODO handle counter types
            elif child.tag == "counter":
                self.counter.append(CounterType(child))

        # TODO still missing counter tag


class ClassType:
    def __init__(self, _class):
        class_attrib = _class.attrib
        self.path = class_attrib.get("name")
        self.filename = class_attrib.get("sourcefilename")
        self.complexity = class_attrib.get("complexity")  # TODO need from Counter
        self.line_rate = class_attrib.get("line-rate")  # TODO need from Counter
        self.branch_rate = class_attrib.get("branch-rate")  # TODO need from Counter
        self.methods = []
        self.counter = []
        for child in _class:
            if child.tag == "method":
                self.methods.append(MethodType(child))
            # TODO handle counter types
            elif child.tag == "counter":
                self.counter.append(CounterType(child))
        # self.lines = [LineType(line) for line in _class[1]] # with in methode


class MethodType:
    def __init__(self, method):
        method_attrib = method.attrib
        self.name = method_attrib.get("name")
        self.destination = method_attrib.get("desc")
        self.line = method_attrib.get("line")
        self.counter = []
        for child in method:
            # TODO handle counter types
            if child.tag == "counter":
                _type = child.get("type")
                if _type == "INSTRUCTION":
                    pass
                elif _type == "LINE":
                    pass
                elif _type == "COMPLEXITY":
                    pass
                elif _type == "METHOD":
                    pass
                self.counter.append(CounterType(child))


class LineType:
    def __init__(self, line):
        line_attrib = line.attrib
        # TODO not sure!!!
        self.number = line_attrib.get("nr")
        self.hits = line_attrib.get("ci")


class CounterType:
    def __init__(self, counter):
        counter_attrib = counter.attrib
        self.type = counter_attrib.get("type")
        self.missed = counter_attrib.get("missed")
        self.covered = counter_attrib.get("covered")


if __name__ == "__main__":
    import time
    start = time.time()
    dataType = XmlParse("../jacoco.xml")
    print(f"executing took: {int((time.time() - start) * 1000)}ms")
    print("done")
