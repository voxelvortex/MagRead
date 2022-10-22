import hid


def get_readers():
    return [item for item in hid.enumerate() if item["manufacturer_string"]=="Mag-Tek"]

def get_device_from_reader(reader):
    return hid.Device(reader["vendor_id"], reader["product_id"])

def get_device_from_readers(readers):
    if len(readers) == 0:
        print("No Mag-Tek reader detected - Quiting")
        return

    elif len(readers) > 1:
        devices = []
        for i in range(len(readers)):
            try:
                a = readers[i]
                dev = hid.Device(a["vendor_id"],a["product_id"])
                devices.append(dev)
                print(f"{i})\t\'{dev.manufacturer} {dev.product}\' - {'nonblocking' if dev.nonblocking else 'blocking'}")
                

            except:
                devices.append(None)

        return devices[int(input( "Enter desired reader number" ))]
    return get_device_from_reader(readers[0])

def read(device):
    print("Waiting for swipe...")
    return device.read(256)

