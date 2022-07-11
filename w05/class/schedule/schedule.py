from json import load, dump
from pathlib import Path

class Schedule:
    def __init__(self, crm_doctor: int, cpf_pacient: str, day: int, month: int, year: int, time: str, observation: str):
        self.crm_doctor = crm_doctor
        self.cpf_pacient = cpf_pacient
        self.day = day
        self.month = month
        self.year = year
        self.time = time
        self.observation = observation
        
    def register_schedule(self, crm_doctor: int, cpf_pacient: str, day: int, month: int, year: int, time: str, observation: str):
        self.crm_doctor = crm_doctor
        self.cpf_pacient = cpf_pacient
        self.day = day
        self.month = month
        self.year = year
        self.time = time
        self.observation = observation
    
    def list_schedule(self):
        return f"{self.crm_doctor}, {self.cpf_pacient}, {self.day}, {self.month}, {self.year}, {self.time}, {self.observation}"
    
    @staticmethod
    def save_schedule(arquivo, array):
        with open(arquivo, 'w') as f:
            dump(array, f)
        
        with open(arquivo, 'r') as f:
            array = load(f)
        
        for schedule in array:
            print(schedule)