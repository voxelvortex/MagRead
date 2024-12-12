#! /usr/bin/env python3

from read import *
from parse import *
from files import *

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

def get_card_data(raw_data):
    card_data = parse_raw_data(raw_data)
    return card_data

def main():
    print(get_intro())
    readers = get_readers()
    device = get_device_from_readers(readers)
    if device is None:
        return
    while True:
        print("-"*49)
        raw_data = read(device)
        #raw_data = get_clean_data()

        null = b'\x00'
        
        print(f"{raw_data.replace(null,b'')}\n\n")
        card_data = get_card_data(raw_data)
        print(f"\nTrack1: {card_data["1"]}\nTrack2: {card_data["2"]}\nTrack3: {card_data["3"]}")
        check_for_save(raw_data,card_data)

        print("\n"*3)


def get_clean_data():
    return b'%+PAN123456789012345^NAMENAMENAME^DATA^SHOULDNTBREAK?X;PAN123456789012345=DATACVV?;+PAN123456789012345=DATABLAH?X'
        

if __name__ == "__main__":
    main()
