import hid


def get_readers():
    # Return a list of all HID devices that have a manufacturer string of 'Mag-Tek'
    return [item for item in hid.enumerate() if item["manufacturer_string"]=="Mag-Tek"]

def get_device_from_reader(reader):
    # convert from a json obj to an HID obj

    return hid.Device(reader["vendor_id"], reader["product_id"])

def get_device_from_readers(readers):
    # Convert the get_readers list into an actual device

    # if there are no readers
    if len(readers) == 0:
        print("No Mag-Tek reader detected - Quiting")
        return

    # if there's multiple readers
    elif len(readers) > 1:
        devices = []
        for i in range(len(readers)):
            try:
                a = readers[i]
                dev = get_device_from_reader(a)
                devices.append(dev)
                print(f"{i})\t\'{dev.manufacturer} {dev.product}\' - {'nonblocking' if dev.nonblocking else 'blocking'}")
                

            except:
                devices.append(None)

        return devices[int(input( "Enter desired reader number" ))]

    # if there's 1 reader
    return get_device_from_reader(readers[0])

def read(device):
    # read input from a device
    print("Waiting for swipe...")
    return device.read(256)

