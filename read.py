#! /usr/bin/python
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
    return device.read(256)[3:]

def parse_raw_data(raw_data):
    END_CHAR = ";"
    START_CHAR = "%"
    SPLIT_CHAR = b"?"

    print(raw_data)
    tracks = raw_data.split(SPLIT_CHAR)

    print(tracks)
    return

    data = raw_data.decode()



    end = end if end != -1 else len(data)
    tracks = data[start:end].replace('\x00','').replace("\x10","").split(SPLIT_CHAR)
    final_output = [track for track in tracks if len(track)!=0]

    return final_output

def main():
    readers = get_readers()
    device = get_device_from_readers(readers)
    if device is None:
        return
    while True:
        raw_data = read(device)
        print(parse_raw_data(raw_data))
        print()

if __name__ == "__main__":
    main()
