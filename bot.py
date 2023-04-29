phonebook = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Please provide all required arguments"
    return wrapper

@input_error
def add_contact(user_input):
    name = user_input[1]
    phone_number = int(user_input[2])
    phonebook[name] = phone_number
    return "Contact added successfully."

@input_error
def change_contact(user_input):
    name = user_input[1]
    phone_number = user_input[2]
    if name in phonebook:
        phonebook[name] = phone_number
        return "Contact updated successfully."
    else:
        return "Contact not found."

@input_error
def get_phone_number(user_input):
    name = user_input[1]
    if name in phonebook:
        return phonebook[name]
    else:
        return "Contact not found."

def show_all():
    output = ""
    for name, phone_number in phonebook.items():
        output += f"{name}: {phone_number}\n"
    return output.rstrip()



def main():
    while True:
        user_input = input(">>> ").lower().split()

        if user_input[0] == "hello":
            print("How can I help you?")

        elif user_input[0] == "add":
            print(add_contact(user_input))

        elif user_input[0] == "change":
            print(change_contact(user_input))
            
        elif user_input[0] == "phone":
            print(get_phone_number(user_input))

        elif user_input[0] == "show" and user_input[1] == "all":
            print(show_all())

        elif user_input[0] == "good" and user_input[1] == "bye" or user_input[0] == "close" or user_input[0] == "exit":
            print("Good bye!")
            break

        else:
            print("Command not recognized.")

if __name__ == '__main__':
    main()
