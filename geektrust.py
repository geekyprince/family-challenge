from family_challenge.CommandLineApp import CommandLineApp
from family_challenge.Family import Family
from family_challenge.Relation import Relation


def main():
    family_instance = Family()
    file_data = CommandLineApp().get_file_data()
    # Main Logic
    for line in file_data:
        operation, *data = line.strip().split()
        # If kingdom is already added in the list then,
        # There is no need to send the data into
        # the solver class
        if operation == 'GET_RELATIONSHIP':
            name = data[0]
            relation = data[-1]
            relative = Relation(relation).relation
            if family_instance.family_dict[name]:
                relative_names = relative.get_relative_names(name, family_instance.family_dict)
                if relative_names:
                    print(*relative_names)
                else:
                    print(None) 
            else:
                print("PERSON_NOT_FOUND")
                
        else:
            mother, name, gender = data
            if family_instance.family_dict[mother]:
                if family_instance.family_dict[mother].gender == 'Female':
                    father = family_instance.family_dict[mother].spouse
                    family_instance.add_member(name,  father, mother, gender)
                    print('CHILD_ADDITION_SUCCEEDED')
                else:
                    print('CHILD_ADDITION_FAILED')
            else:
                print("PERSON_NOT_FOUND")


if __name__ == "__main__":
    main()
