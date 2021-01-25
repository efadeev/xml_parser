import xml.etree.ElementTree as et
import sys,os


def parsedump(id):
    xml_path = os.path.dirname(os.path.realpath(__file__)) + '/dump.xml'
    tree = et.parse(xml_path)
    root = tree.getroot()
    for child in root.findall('content[@id="%s"]' % id):
        print(child.attrib)
        for obj in child:
            print(obj.tag, obj.text)


if __name__ == "__main__":
    parsedump(sys.argv[1])
