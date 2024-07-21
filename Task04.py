from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Not existing user name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except:
            return 'Uknown error'
        

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        raise KeyError
    
    contacts[name] = phone
    return f"Contact {name} updated."

@input_error
def show_phone(args, contacts):
    name = args[0]

    if not args:
        raise IndexError

    if name not in contacts:
        raise KeyError
    
    for key, value in contacts.items():
        if key == name:
            return f'{name} {value}'
             
def show_all(contacts):
    result = []

    if not result:
        return 'You dont have any contacts'

    for key, value in contacts.items():
        result.append(f'{key}: {value}')
    return '\n'.join(result)

def main():
    contacts ={}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.") 

if __name__ == "__main__":
    main()
    