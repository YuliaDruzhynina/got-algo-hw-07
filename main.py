from classes import AddressBook
from classes import Record, Birthday


def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter user name"
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args 
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    else:    
        record.add_phone(phone)
    return "Contact added."


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    else:
        record.edit_phone(old_phone, new_phone)
        return "Contact changed."


@input_error
def show_phone(args, book: AddressBook): 
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
     
    return f"Conactname: {name},{'; '.join(str(phone) for phone in record.phones)}"


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
                                    #else: return None
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return record.birthday()


@input_error
def show_all(book: AddressBook):
    return list(book.items())
# вместо даты рождения - обьект класса

@input_error
def birthdays(args, book: AddressBook):
    name = args[0]
    if name in book.keys():
        return book.get_upcoming_birthdays()


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))  
        elif command == "birthdays":
            print(birthdays(book))      
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
