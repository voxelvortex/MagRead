def save_data(loc, data):
    with open(loc,'wb') as file:
        file.write(data)

def read_data(loc):
    with open(loc, 'rb') as file:
        data = file.read()
    return data

def check_for_save(raw_data, card_data):
    uin = input(f"\nSave data? (y/n)")
    if uin.lower() == 'y':
        save_data('./card.bin', raw_data)
        save_data('./card.json', str(card_data).replace("'",'"').replace('b"','"').replace("None","null").encode())
    
    