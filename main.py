#! /usr/bin/python

from read import *
from parse import *

def get_intro():
    return """
                      ___                      _ 
/'\_/`\              |  _`\                   ( )
|     |   _ _    __  | (_) )   __     _ _    _| |
| (_) | /'_` ) /'_ `\| ,  /  /'__`\ /'_` ) /'_` |
| | | |( (_| |( (_) || |\ \ (  ___/( (_| |( (_| |
(_) (_)`\__,_)`\__  |(_) (_)`\____)`\__,_)`\__,_)
              ( )_) |                            
               \___/'                            
    """

def get_card_data(device):
    raw_data = read(device)
    card_data = parse_raw_data(raw_data)

    return card_data

def get_card_string(device):
    card = get_card_data(device)

    return card

def main():
    print(get_intro())
    readers = get_readers()
    device = get_device_from_readers(readers)
    if device is None:
        return
    while True:
        
        print(f"\n{get_card_string(device)}")
        print("\n"*3)

if __name__ == "__main__":
    main()
