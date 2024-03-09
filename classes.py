from collections import UserDict 
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def is_valid(self, value):
        self.value = value
        return True
    
    @property
    def value(self):
        return self.__value  # можем указать иное значение для возврата напр.множина
    
    @value.setter
    def value(self, value):
        if not self.is_valid(value):
            raise ValueError
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
        
    def add_phone(self, phone):  # self.phones.append(Phone(phone))
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
            return "Not found"
  
           
    def edit_phone(self, old_phone: str, new_phone: str):
        if self.find_phone(old_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {str(self.birthday)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record  # self[record.name.value]
        return record
    
    def find(self, name: str):          
        return self.data.get(name)  # return self.get(name) error не будет:UserDict
    
    def delete(self, name: str):
        if self.find(name):
            del self.data[name]

    def get_upcoming_birthdays(self):
        
        today = datetime.now().date()
        upcoming_birthdays = [record for record in self.data.values() if record.birthday.value.date() > today]
        upcoming_birthdays += upcoming_birthdays  #upcoming_birthday.append(record)
        return upcoming_birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())     

