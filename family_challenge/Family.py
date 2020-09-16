from family_challenge.FileParser import FileParser
from family_challenge.TreeNode import TreeNode
import os


class Family:
    def __init__(self):
        """
        __init__ Automatically gets the family data from the input file
        and then encodes it into dictionary of TreeNodes (Family Tree)

        self.family_dict = {
            member name: TreeNode
            }
        """
        self.file_parser = FileParser()
        self.family_dict = self.__parse_family_file(
            "".join([os.getcwd(), "/FamilyData.txt"])
        )

    def add_member(self, name, father, mother, gender, spouse, family_dict = dict()):
        if spouse == 'None':
            spouse = None
            
        if father == 'None':   #generation 0
            father, mother = None, None 
        elif gender == 'male':
            family_dict[father].son.add(name)
            family_dict[mother].son.add(name)
        else:
            family_dict[father].daughter.add(name)
            family_dict[mother].daughter.add(name)
        member = TreeNode(father, mother, gender, spouse)    
        family_dict[name] = member
            
        return family_dict
            

    def __parse_family_file(self, file_path):
        file_contents = self.file_parser.parse_file(file_path)
        for line in file_contents:
            family_dict = add_member(line.split()) 
        return family_dict
