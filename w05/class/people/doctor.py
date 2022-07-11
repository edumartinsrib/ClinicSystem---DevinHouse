from json import load, dump
from persons import Person

class Doctor(Person):
    def __init__(self, name: str, email: str, phone:str, crm: str, phone_secondary: int):
         self.phone_secondary = phone_secondary
         self.crm = crm
         super().__init__(name, phone, email)
         
    def register_doctor(self):
        print('Please, type doctor informations:')
        while True:
            try:
                self.name = input("Type the name: ")
                self.phone_secondary = int(input("Type a phone secondary: "))
                self.crm = input("Type the crm credencial: ")
                self.email = input("Type the email: ")
                self.phone = input("Type the phone: ")
                
                self.save_doctor('doctors.json', [self.__dict__()])             
                break
            except ValueError:
                print("Type just numbers")
    
    def show_doctor(self):
        return f"{self.name}, {self.phone}, {self.email}, {self.crm}, {self.phone_secondary}"
    
    @staticmethod
    def save_doctor(arquivo, array):
        with open(arquivo, 'w') as f:
            dump(array, f)
     
        with open(arquivo, 'r') as f:
            array = load(f)
     
        for doctor in array:
            print(doctor)

