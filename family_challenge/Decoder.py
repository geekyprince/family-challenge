from family_challenge.Relation import Relation

class Decoder:
    def get_relationship(self, data, family_dict):
        name = data[0]
        relation = data[-1]
        relative = Relation(relation).relation
        if family_dict[name]:
            relative_names = relative.get_relative_names(name, family_dict)
            if relative_names:
                return relative_names
            return "NONE"   #no relative with this relation
        return "PERSON_NOT_FOUND"   #given person not in shan family
    
    def add_child(self, data, family_instance):
        mother, name, gender = data
        if family_instance.family_dict[mother]:
            if family_instance.family_dict[mother].gender == "Female":
                father = family_instance.family_dict[mother].spouse
                family_instance.add_member(name,  father, mother, gender)
                return "CHILD_ADDITION_SUCCEEDED"
            return "CHILD_ADDITION_FAILED"    #invalid person for mother
        return "PERSON_NOT_FOUND"  #mother not in Shan family
    

    def print_answer(self, answer):
        """
        print_answer --> Prints the final answer based on the required output
        """
        if isinstance(answer, set):
            print(*answer)
        else:
            print(answer)
