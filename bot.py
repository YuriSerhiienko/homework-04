phonebook = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "There is no such name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
        except TypeError:
            return "Incorrect values"
    return inner

def greeting(_):
    return "How can I help you?"

def unknown_command():
    return "Unknown command"

def exit(_):
    return None

@input_error
def add_user(*args):
    name, phone = args
    phonebook[name] = int(phone)
    return "Contact added successfully"

@input_error
def change_phone(*args):
    name, phone = args
    phonebook[name] = phone
    return "Contact updated successfully."

def show_all(_):
    if not phonebook:
        return "The phonebook is empty"
    result = ''
    for name, phone_number in phonebook.items():
        result += f"{name}: {phone_number}\n"
    return result.rstrip()

@input_error
def get_phone_number(name):
    return phonebook[name]

commands = {
    'hello': greeting,
    'add': add_user,
    'change': change_phone,
    'show all': show_all,
    "phone": get_phone_number,
    'exit': exit,
    'good bye': exit,
    'close': exit,
}

def main():
    while True:
        command, *args = input(">>> ").strip().split(' ', 1)
        if commands.get(command):
            handler = commands.get(command)
            if args:
                args = args[0].split()    
                result = handler(*args)
            else:
                result = handler("")
        elif args and commands.get(command + ' ' + args[0]):
            command = command + ' ' + args[0]
            args = args[1:]
            handler = commands.get(command)      
            result = handler(args)
        else:
            result = unknown_command()

        if not result:
            print('Good bye!')
            break

        print(result)

if __name__ == "__main__":
    main()
