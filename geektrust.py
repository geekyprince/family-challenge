from family_challenge.CommandLineApp import CommandLineApp
from family_challenge.Family import Family
from family_challenge.Decoder import Decoder


def main():
    family_instance = Family()
    file_data = CommandLineApp().get_file_data()
    decoder_instance = Decoder()
    # Main Logic
    for line in file_data:
        operation, *data = line.strip().split()
        
        if operation == 'GET_RELATIONSHIP':
            answer = decoder_instance.get_relationship(data, family_instance.family_dict)
        else:
            answer = decoder_instance.add_child(data, family_instance)
        decoder_instance.print_answer(answer)
            
if __name__ == "__main__":
    main()
