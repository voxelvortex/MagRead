# Lots of this is based on https://www.magtek.com/content/documentationfiles/d99800004.pdf

import re

def get_track_1(raw_data):

    # Define sentinels and seperators
    SS = b'%'
    FS = b'^'
    ES = b'?'
    # [ {SS} PAN:(FormatCode - 19 Chars) {FS} NAME:(26 Chars) {FS} DATA:(29 Chars) {ES} {LRC} ]

    regex_pattern = rb"%(.{0,19})\^(.{0,26})\^(.{0,29})\?"
    matches = re.findall(regex_pattern, raw_data)
    if len(matches) == 0:
        return None
    for match in matches:
        temp = list(match)
        data = {}
        #data["LRC"] = temp.pop()
        data["data"] = temp.pop()
        data["name"] = temp.pop()
        data["pan"] = temp.pop()
        return data

def get_track_2(raw_data):

    # Define sentinels and seperators
    SS = b';'
    FS = b'='
    ES = b'?'
    # [ {SS} PAN:(FormatCode - 19 Chars) {FS} DATA:(17 Chars) {ES} {LRC} ]

    regex_pattern = rb";(.{0,19})=(.{0,17})\?"
    matches = re.findall(regex_pattern, raw_data)
    if len(matches) == 0:
        return None
    for match in matches:
        temp = list(match)
        data = {}
        #data["LRC"] = temp.pop()
        data["data"] = temp.pop()
        data["pan"] = temp.pop()
        return data


def get_track_3(raw_data):

    # Define sentinels and seperators
    SS = b';'
    FS = b'='
    ES = b'?'
    # [ {SS} PAN:(FormatCode - 19 Chars) {FS} DATA:(84 Chars) {ES} {LRC} ]

    regex_pattern = rb";(.{0,19})=(.{0,84})\?(.{0,3})$"
    matches = re.findall(regex_pattern, raw_data)
    if len(matches) == 0:
        return None
    for match in matches:
        temp = list(match)
        data = {}
        data["LRC"] = temp.pop()
        data["data"] = temp.pop()
        data["pan"] = temp.pop()
        return data


def get_tracks_from_raw_data(raw_data):
    return [get_track_1(raw_data),get_track_2(raw_data),get_track_3(raw_data)]


def parse_raw_data(raw_data):
    #raw_data = raw_data.replace(b'\x00',b'')
    tracks = get_tracks_from_raw_data(raw_data)
    card_data={}
    card_data["3"] = tracks.pop()
    card_data["2"] = tracks.pop()
    card_data["1"] = tracks.pop()

    #tracknum = ["Track1", "Track2", "Track3"]
    #for i in range(len(tracknum)):
    #    card_data[tracknum[i]] = tracks[i]
    #    print(tracks[i])

    return card_data

