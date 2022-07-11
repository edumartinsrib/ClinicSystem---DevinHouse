from json import load, dump
from pathlib import Path

class Person:
    def __init__(self, name: str, phone: int, email: str):
        self.name = name
        self.phone = phone
        self.email = email
    
    def register_person(self, name: str, phone: int, email: str):
        self.name = name
        self.phone = phone
        self.email = email
    
    def show_person(self):
        return f"{self.name}, {self.phone}, {self.email}"
    
    def __dict__(self):
        return {
                "name": self.name,
                'phone': self.phone,
                'email': self.email
                }
        
    @staticmethod    
    def save_person(arquivo, array):
        with open(arquivo, 'w') as f:
            dump(array, f)
    
        with open(arquivo, 'r') as f:
            array = load(f)
    
        for person in array:
            print(person)
            