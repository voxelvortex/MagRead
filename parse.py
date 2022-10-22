def parse_trim_start(raw_data):
    for i in range(len(raw_data)):
        cur_byte = raw_data[i].to_bytes(1,"big")
        if cur_byte != b'\x00' and cur_byte!= b"\x10":
            return raw_data[i:]
    return b""

def parse_trim_end(raw_data):
    index = 0
    for i in range(len(raw_data)):
        if raw_data[i].to_bytes(1,"big") != b'\x00':
            index = i
    return raw_data[:index+1]



def get_tracks_from_raw_data(raw_data):
    SPLIT_CHAR = b"?"

    raw_data = parse_trim_end(parse_trim_start(raw_data))
    tracks = [parse_trim_end(parse_trim_start(track)) for track in raw_data.split(SPLIT_CHAR)]

    for track in tracks:
        print(f"\t{track}")

    return tracks


def parse_raw_data(raw_data):
    tracks = get_tracks_from_raw_data(raw_data)
    card_data = {}

    for item in ["Track1", "Track2", "Track3"]:
        card_data[item]={}
    
    # T1
    card_data["Track1"]["PAN"] = ""
    card_data["Track1"]["NAME"] = ""
    card_data["Track1"]["DATA"] = ""

    # T2
    card_data["Track2"]["PAN"]=""
    card_data["Track2"]["DATA"]=""

    # T3
    card_data["Track3"]["PAN"]= ""
    card_data["Track3"]["DATA"]=""

    return card_data
