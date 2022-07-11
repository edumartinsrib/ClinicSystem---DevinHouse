from requests import request
from json import load, dump
from pathlib import Path

class Address:
    def __init__(self):
        self.__address: str = None
        self.__number: int = None
        self.__city: str = None
        self.__state: str = None
        self.__neighborhood: str = None
        self.list_address = self.load_list_address()

    def register_address(self, address, number, city, state, neighborhood):
        self.__address = address
        self.__number = number
        self.__city = city
        self.__state = state
        self.__neighborhood = neighborhood

    def register_by_cep(self):
        cep = input("Please enter your ZipCode: ")
        response = request("GET", f"https://viacep.com.br/ws/{cep}/json/")
        address = load(response.content)
        number_house = input("Please, enter the number of house:")
        self.register_address(address['logradouro'], number_house, address['localidade'], address['uf'], address['bairro'])

    
    def show_address(self):
        return f"{self.__address}, {self.__number}, {self.__city}, {self.__state}, {self.__neighborhood}"
    
    def __dict__(self):
        return {"address": self.__address,
                "number": self.__number,
                "city": self.__city,
                "state": self.__state,
                "neighborhood": self.__neighborhood}
    
    def load_list_address(self):
        file_address = Path("address.json")
        if file_address.exists():
            with open("address.json", "r") as file:
                self.list_address = load(file)
        else:
            self.list_address = []
    
    def save_address(arquivo, array):
        with open(arquivo, 'w') as f:
            dump(array, f)

        with open(arquivo, 'r') as f:
            array = load(f)

        for address in array:
            print(address)

    def save_address_file(self):
        self.list_address.append(self.__dict__())
        self.save_address("address.json", self.list_address)