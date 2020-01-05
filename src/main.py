import xml.dom.minidom
from xml.etree import ElementTree


class Parser:
    def __init__(self, file_name):
        self.doc = xml.dom.minidom.parse(file_name)
        self.file_name = file_name
        self.tree = ElementTree.parse(file_name)

    def get_all(self):
        employees = self.doc.getElementsByTagName("employee")
        print("-"*50)
        print("ID\t\tName\t\t\tExpertise")
        print("-"*50)
        for emp in employees:
            nickname = emp.getElementsByTagName("name")[0]
            print(emp.getAttribute("id"), end="\t\t")
            print(nickname.firstChild.data, end="\t\t")
            print(emp.getElementsByTagName("expertise")[0].firstChild.data, end="\t\t")
            print()

    def add(self, id, name, expertise):
        root = ElementTree.parse(self.file_name).getroot()
        new_name = ElementTree.Element("name")
        new_exprt = ElementTree.Element("expertise")
        new_name.text = name
        new_exprt.text = expertise
        new_emp = ElementTree.Element("employee")
        new_emp.append(new_name)
        new_emp.append(new_exprt)
        new_emp.set("id", id)
        root.insert(0, new_emp)
        self.tree.write(root)

    def delete(self, id):
        pass




def main():
    doc = xml.dom.minidom.parse("file.xml")
    print(doc.nodeName)
    print(doc._get_firstChild().tagName)


if __name__ == '__main__':
    parser = Parser("file.xml")
    parser.get_all()
    parser.add("wwwr", "new Name", "ya")
    parser.get_all()
