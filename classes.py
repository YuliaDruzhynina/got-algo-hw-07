from collections import UserDict 
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def is_valid(self, value):
        return True
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not self.is_valid(value):
            raise ValueError
        else:
            self.__value = value
    
    def __str__(self) -> str:
        return str(self.value)

    
class Birthday(Field):
    def is_valid(self, value):
        if not datetime.strptime(value, "%d.%m.%Y"):
            return False
        return True
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not self.is_valid(value):
            raise ValueError
        else:
            self.__value = datetime.strptime(value, "%d.%m.%Y")


class Name(Field):  
    def is_valid(self, value):
        return bool(value)


class Phone(Field):
    def is_valid(self, value):
        return value.isdigit() and len(value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)        

    def add_phone(self, phone):  #self.phones.append(Phone(phone))
        ph = Phone(phone)
        self.phones.append(ph)
        return ph
                                         
    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph 
        return None
    
    def remove_phone(self, phone):       
        try:
            self.phones.remove(self.find_phone(phone))
        except ValueError:
            return None  
             
    def edit_phone(self, old_phone: str, new_phone: str):
        ph = self.find_phone(old_phone)
        if ph:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {str(self.birthday)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return record
    
    def find(self, name: str):                
        return self.data.get(name)
    
    def delete(self, name: str):
        if self.find(name):
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        upcoming_birthdays = [record for record in self.data.values() if record.birthday.value.date() > today]
        return upcoming_birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())     

    # Створення нової адресної книги
# book = AddressBook()

#     # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
#     # Додавання запису John до адресної книги
# book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

#     # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)
#     # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
# book.delete("Jane")
