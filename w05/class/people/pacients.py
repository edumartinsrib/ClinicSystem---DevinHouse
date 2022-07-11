from .persons import Person
from json import load, dump
from pathlib import Path


class Pacient(Person):
    def __init__(self, rg: str, cpf: str, phone: int, insurance: str, birth: str):
        self.rg = rg
        self.cpf = cpf
        self.phone = phone
        self.insurance = insurance
        self.birth = birth
    
    def register_pacient(self, rg: str, cpf: str, phone: int, insurance: str, birth: str):
        self.rg = rg
        self.cpf = cpf
        self.phone = phone
        self.insurance = insurance
        self.birth = birth
    
    def show_pacient(self):
        return """Paciente:
            Nome: {}
            Phone: {}
            Email: {}
            RG: {}
            CPF: {}
            insurance: {}
            birthday: {}
            """.format(self.name, self.phone, self.email, self.rg, self.cpf, self.insurance, self.birth)
    
    
    def __dict__(self):
        return {  "rg": self.rg, "cpf": self.cpf, "phone": self.phone, "insurance": self.insurance, "birth": self.birth }
    
    @staticmethod
    def save_pacient( arquivo, array):
        with open(arquivo, 'w') as f:
            dump(array, f)
    
        with open(arquivo, 'r') as f:
            array = load(f)
    
        for pacient in array:
            print(pacient)
        
        
new_pacient = Pacient(name='José' ,rg='123456789', cpf='123456789', phone=11, insurance='123456789', birth='123456789')

print(new_pacient.show_pacient())