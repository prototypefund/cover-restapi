import xml.etree.ElementTree as ET


class XmlParse:
    def __init__(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        # root attrib
        root_attrib = root.attrib
        self.version = root_attrib["version"]
        self.timestamp = root_attrib["timestamp"]
        self.lines_valid = root_attrib["lines-valid"]
        self.lines_covered = root_attrib["lines-covered"]
        self.line_rate = root_attrib["line-rate"]
        self.branches_covered = root_attrib["branches-covered"]
        self.branches_valid = root_attrib["branches-valid"]
        self.branch_rate = root_attrib["branch-rate"]
        self.complexity = root_attrib["complexity"]
        # sources
        self.sources = [source.text for source in root[0]]
        # packages
        self.packages = [source.attrib for source in root[1]]
        print(self.packages)

    @staticmethod
    def parser(path):
        tree = ET.parse(path)
        root = tree.getroot()
        print(root.attrib)
        return root.attrib


if __name__ == "__main__":
    dataType = XmlParse("../coverage.xml")
