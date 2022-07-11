from pathlib import Path

class Settings:
    
    ROOT_PATH = Path(__file__).parent.parent
    DATA_PATH = ROOT_PATH / 'data'
    DATA_ADDRESS_PATH = DATA_PATH / 'address.csv'
    DATA_PERSON_PATH = DATA_PATH / 'person.csv'
    DATA_SCHEDULE_PATH = DATA_PATH / 'schedule.csv'
    
    