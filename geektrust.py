from family_challenge.CommandLineParser import CommandLineParser
from family_challenge.Family import Family
from family_challenge.Relation import Relation


def main():
    family_instance = Family()
    file_contents = CommandLineParser().get_file_contents()
    # Main Logic
    for line in file_contents:
        operation, *data = line.strip().split()
        # If kingdom is already added in the list then,
        # There is no need to send the data into
        # the solver class
        if operation == 'GET_RELATIONSHIP':
            name = data[0]
            relation = data[-1]
            relative = Relation(relation).relation
            relative_names = relative.get_relative_names(name, family_instance.family_dict)
            if relative_names:
                print(*relative_names)
            else:
                print(None)
        else:
            mother, name, gender = data
            father = family_instance.family_dict[mother].spouse
            family_instance.add_member(name,  father, mother, gender)
            print('CHILD_ADDITION_SUCCEEDED')


if __name__ == "__main__":
    main()
