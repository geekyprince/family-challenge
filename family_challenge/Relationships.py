from family_challenge.Relationship import Relationship 

class GrandFather(Relationship):
    def __init__(self, connection):
        self.connection = connection
        
    def get_relative_names(self, name, family_dict):
        if self.connection == 'Paternal':
            parent = family_dict[name].father
        else:
            parent = family_dict[name].mother
        if parent == 'None':
            return None
        return family_dict[parent].father

class Uncle(Relationship):
    def __init__(self, connection):
        self.connection = connection
        
    def get_relative_names(self, name, family_dict):
        grandfather = GrandFather(self.connection).get_relative_names(name, family_dict)
        if grandfather:
            return family_dict[grandfather].son - {family_dict[name].father}
        return None
        
         
class Aunt(Relationship):
    def __init__(self, connection):
        self.connection = connection
        
    def get_relative_names(self, name, family_dict):
        grandfather = GrandFather(self.connection).get_relative_names(name, family_dict)
        return family_dict[grandfather].daughter - {family_dict[name].mother}
    
class Siblings(Relationship):
    def get_relative_names(self, name, family_dict):
        father_name = family_dict[name].father
        if father_name == 'None':
            return set() 
        sons = family_dict[father_name].son
        daughters = family_dict[father_name].daughter
        return sons.union(daughters) - {name}

class Sisters(Relationship):
    def get_relative_names(self, name, family_dict):
        father_name = family_dict[name].father
        if father_name == 'None':
            return set()
        return family_dict[father_name].daughter - {name}

class Brothers(Relationship):
    def get_relative_names(self, name, family_dict):
        father_name = family_dict[name].father
        if father_name == 'None':
            return set()
        return family_dict[father_name].son - {name}
    
class SpouseOfSiblings(Relationship):
    def get_relative_names(self, names, family_dict):
        spouses = set()
        for name in names:
            spouses.add(family_dict[name].spouse)
        return spouses
    
class SisterInLaw(Relationship):
    def get_relative_names(self, name, family_dict):
        spouse_sisters = set()
        if family_dict[name].spouse != 'None':
            spouse_sisters = Sisters().get_relative_names(family_dict[name].spouse, family_dict)
        brothers = Brothers().get_relative_names(name, family_dict)
        wife_of_brothers = SpouseOfSiblings().get_relative_names(brothers, family_dict)
        return spouse_sisters.union(wife_of_brothers)
    
class BrotherInLaw(Relationship):
    def get_relative_names(self, name, family_dict):
        spouse_brothers = set()
        if family_dict[name].spouse != 'None':
            spouse_brothers = Brothers().get_relative_names(family_dict[name].spouse, family_dict)
        sisters = Sisters().get_relative_names(name, family_dict)
        husband_of_sisters = SpouseOfSiblings().get_relative_names(sisters, family_dict)
        return spouse_brothers.union(husband_of_sisters) 

class Son(Relationship):
    def get_relative_names(self, name, family_dict):
        return family_dict[name].son 

class Daughter(Relationship):
    def get_relative_names(self, name, family_dict):
        family_dict[name].daughter 

 