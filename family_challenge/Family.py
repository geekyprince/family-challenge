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
        self.family_dict = dict()
        self.__parse_family_file(
            "".join([os.getcwd(), "/FamilyData.txt"])
        )

    def add_member(self, name, father, mother, gender, spouse = None):
        if father == 'None':   #parents not defined
            pass     
        elif gender == 'Male': #add son
            self.family_dict[father].son.add(name)
            self.family_dict[mother].son.add(name)
        else:                  #add daughter
            self.family_dict[father].daughter.add(name)
            self.family_dict[mother].daughter.add(name)
        #add member to family_dict
        self.family_dict[name] = TreeNode(father, mother, gender, spouse)

    def __parse_family_file(self, file_path):
        file_contents = self.file_parser.parse_file(file_path)
        for line in file_contents[1:]:  #first line is column names
            self.add_member(*line.split()) 
