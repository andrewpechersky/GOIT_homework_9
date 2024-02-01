from types import FunctionType

phonebook = {}
help = """You can use:
add > name
change > name
phone > name
show
and [good bue, close, exit .] to exit"""


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IndexError as e:
            return help
        except ValueError as e:
            return help
        except Exception as e:
            return f"Oops! Something went wrong: {e}"

    return wrapper


@input_error
def hello(user_input):
    return "Hey, how can I help?"


@input_error
def add(user_input):
    action, name, phone_number = user_input.split()
    if name not in phonebook:
        phonebook[name] = phone_number
        return "Contact added successfully!"
    else:
        raise ValueError


@input_error
def change(user_input):
    action, name, phone_number = user_input.split()
    if name in phonebook:
        phonebook[name] = phone_number
        return "Contact updated successfully!"
    else:
        raise ValueError


@input_error
def get_phone(user_input):
    try:
        action, name = user_input.split()
        result = phonebook.get(name, "Contact not found.")
        return f"{name} --> {result}"
    except ValueError:
        return "Oops! Please provide a valid input."


@input_error
def show_all(user_input):
    if user_input != "show all":
        return "Oops! Invalid command."

    if not phonebook:
        return "No contacts available."

    contacts_info = "\n".join([f"{name}: {phone}" for name, phone in phonebook.items()])
    return f"All contacts:\n{contacts_info}"


@input_error
def exit_program(user_input):
    if user_input in ("good bye", "exit", "close", "."):
        return "Good bye!"
    else:
        return "Oops! Invalid command."


@input_error
def get_operation(user_input):
    operation = user_input.split()[0]
    return operations.get(operation, help)


operations = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": get_phone,
    "show": show_all,
    "good": exit_program,
    "exit": exit_program,
    "close": exit_program,
    ".": exit_program
}


def main():
    while True:
        user_input = input(" >-- ").lower().strip()
        func = get_operation(user_input)
        if not isinstance(func, FunctionType):
            print(func)
            continue
        result = func(user_input)
        print(result)

        if result == 'Good bye!':
            break


if __name__ == '__main__':
    main()
