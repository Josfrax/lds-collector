from datetime import date
from json import dump
from typing import BinaryIO


def JSONFile(data: dict, name: str) -> BinaryIO:
    """ Create JSON file. Default path: data directory.

      Params: 
        data(dict): recive data in formar JSON to save.
        name(str): Set name to file.

      Return:
        Binary (JSON file)
    """
    today: str = date.today().strftime('%Y%m%d')
    file_name: str = f'./data/{today}_{name.upper()}.json'
    try:
        with open(file_name, 'a') as file:
            dump(data, file, indent=4, sort_keys=True)
            file.close()
    except FileNotFoundError:
        print("The 'data' directory does not exist", FileNotFoundError)
