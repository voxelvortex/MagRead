
def save_data(loc, data):
    with open(loc,'wb') as file:
        file.write(data)

def read_data(loc):
    with open(loc, 'rb') as file:
        data = file.read()
    return data

def check_for_save():
    pass
    