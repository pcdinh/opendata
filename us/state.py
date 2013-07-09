# coding: utf-8
'''
Created on Jul 9, 2013

@author: pcdinh
'''

import json

# Data source: http://www.50states.com/abbreviations.htm#.UdvqqrxSax0
states = '''
ALABAMA     AL
ALASKA     AK
ARIZONA     AZ
ARKANSAS     AR
CALIFORNIA     CA
COLORADO     CO
CONNECTICUT     CT
DELAWARE     DE
FLORIDA     FL
GEORGIA     GA
HAWAII     HI
IDAHO     ID
ILLINOIS     IL
INDIANA     IN
IOWA     IA
KANSAS     KS
KENTUCKY     KY
LOUISIANA     LA
MAINE     ME
MARYLAND     MD
MASSACHUSETTS     MA
MICHIGAN     MI
MINNESOTA     MN
MISSISSIPPI     MS
MISSOURI     MO
MONTANA     MT
NEBRASKA     NE
NEVADA     NV
NEW HAMPSHIRE     NH
NEW JERSEY     NJ
NEW MEXICO     NM
NEW YORK     NY
NORTH CAROLINA     NC
NORTH DAKOTA     ND
OHIO     OH
OKLAHOMA     OK
OREGON     OR
PENNSYLVANIA     PA
RHODE ISLAND     RI
SOUTH CAROLINA     SC
SOUTH DAKOTA     SD
TENNESSEE     TN
TEXAS     TX
UTAH     UT
VERMONT     VT
VIRGINIA     VA
WASHINGTON     WA
WEST VIRGINIA     WV
WISCONSIN     WI
WYOMING     WY
American Samoa    AS
District of Columbia    DC
Federated States of Micronesia    FM
Guam    GU
Marshall Islands    MH
Northern Mariana Islands    MP
Palau    PW
Puerto Rico    PR
Virgin Islands    VI
'''

def _normalize(line_):
    '''
    @return: a tuple (full state name, state abbreviation)
    '''
    most_right_ws = line_.rfind(' ')
    return line_[:most_right_ws].strip().lower().title(), line_[most_right_ws:].strip()

def to_json(states_, flat=True):
    """
    
    @param flat: If True, return a JSON string which has minimal structure
                    [["Alabama", "AL"], ["Alaska", "AK"], ["Arizona", "AZ"], ["Arkansas", "AR"], ["California", "CA"], ["Colorado", "CO"], ["Connecticut", "CT"], ["Delaware", "DE"], ["Florida", "FL"], ["Georgia", "GA"], ["Hawaii", "HI"], ["Idaho", "ID"], ["Illinois", "IL"], ["Indiana", "IN"], ["Iowa", "IA"], ["Kansas", "KS"], ["Kentucky", "KY"], ["Louisiana", "LA"], ["Maine", "ME"], ["Maryland", "MD"], ["Massachusetts", "MA"], ["Michigan", "MI"], ["Minnesota", "MN"], ["Mississippi", "MS"], ["Missouri", "MO"], ["Montana", "MT"], ["Nebraska", "NE"], ["Nevada", "NV"], ["New Hampshire", "NH"], ["New Jersey", "NJ"], ["New Mexico", "NM"], ["New York", "NY"], ["North Carolina", "NC"], ["North Dakota", "ND"], ["Ohio", "OH"], ["Oklahoma", "OK"], ["Oregon", "OR"], ["Pennsylvania", "PA"], ["Rhode Island", "RI"], ["South Carolina", "SC"], ["South Dakota", "SD"], ["Tennessee", "TN"], ["Texas", "TX"], ["Utah", "UT"], ["Vermont", "VT"], ["Virginia", "VA"], ["Washington", "WA"], ["West Virginia", "WV"], ["Wisconsin", "WI"], ["Wyoming", "WY"], ["American Samoa", "AS"], ["District Of Columbia", "DC"], ["Federated States Of Micronesia", "FM"], ["Guam", "GU"], ["Marshall Islands", "MH"], ["Northern Mariana Islands", "MP"], ["Palau", "PW"], ["Puerto Rico", "PR"], ["Virgin Islands", "VI"]]
                 If False, return a JSON string that has JavaScript objects
                    [{"abbrev": "AL", "name": "Alabama"}, {"abbrev": "AK", "name": "Alaska"}, {"abbrev": "AZ", "name": "Arizona"}, {"abbrev": "AR", "name": "Arkansas"}, {"abbrev": "CA", "name": "California"}, {"abbrev": "CO", "name": "Colorado"}, {"abbrev": "CT", "name": "Connecticut"}, {"abbrev": "DE", "name": "Delaware"}, {"abbrev": "FL", "name": "Florida"}, {"abbrev": "GA", "name": "Georgia"}, {"abbrev": "HI", "name": "Hawaii"}, {"abbrev": "ID", "name": "Idaho"}, {"abbrev": "IL", "name": "Illinois"}, {"abbrev": "IN", "name": "Indiana"}, {"abbrev": "IA", "name": "Iowa"}, {"abbrev": "KS", "name": "Kansas"}, {"abbrev": "KY", "name": "Kentucky"}, {"abbrev": "LA", "name": "Louisiana"}, {"abbrev": "ME", "name": "Maine"}, {"abbrev": "MD", "name": "Maryland"}, {"abbrev": "MA", "name": "Massachusetts"}, {"abbrev": "MI", "name": "Michigan"}, {"abbrev": "MN", "name": "Minnesota"}, {"abbrev": "MS", "name": "Mississippi"}, {"abbrev": "MO", "name": "Missouri"}, {"abbrev": "MT", "name": "Montana"}, {"abbrev": "NE", "name": "Nebraska"}, {"abbrev": "NV", "name": "Nevada"}, {"abbrev": "NH", "name": "New Hampshire"}, {"abbrev": "NJ", "name": "New Jersey"}, {"abbrev": "NM", "name": "New Mexico"}, {"abbrev": "NY", "name": "New York"}, {"abbrev": "NC", "name": "North Carolina"}, {"abbrev": "ND", "name": "North Dakota"}, {"abbrev": "OH", "name": "Ohio"}, {"abbrev": "OK", "name": "Oklahoma"}, {"abbrev": "OR", "name": "Oregon"}, {"abbrev": "PA", "name": "Pennsylvania"}, {"abbrev": "RI", "name": "Rhode Island"}, {"abbrev": "SC", "name": "South Carolina"}, {"abbrev": "SD", "name": "South Dakota"}, {"abbrev": "TN", "name": "Tennessee"}, {"abbrev": "TX", "name": "Texas"}, {"abbrev": "UT", "name": "Utah"}, {"abbrev": "VT", "name": "Vermont"}, {"abbrev": "VA", "name": "Virginia"}, {"abbrev": "WA", "name": "Washington"}, {"abbrev": "WV", "name": "West Virginia"}, {"abbrev": "WI", "name": "Wisconsin"}, {"abbrev": "WY", "name": "Wyoming"}, {"abbrev": "AS", "name": "American Samoa"}, {"abbrev": "DC", "name": "District Of Columbia"}, {"abbrev": "FM", "name": "Federated States Of Micronesia"}, {"abbrev": "GU", "name": "Guam"}, {"abbrev": "MH", "name": "Marshall Islands"}, {"abbrev": "MP", "name": "Northern Mariana Islands"}, {"abbrev": "PW", "name": "Palau"}, {"abbrev": "PR", "name": "Puerto Rico"}, {"abbrev": "VI", "name": "Virgin Islands"}]
    """
    ret = []
    for line in iter(states_.splitlines()):
        if line == '':
            continue
        full_name, abbrev = _normalize(line)
        if flat is True:
            ret.append([full_name, abbrev])
        else:
            ret.append({'name': full_name, 'abbrev': abbrev})
    return json.dumps(ret)

def print_out(states_):
    for line in iter(states_.splitlines()):
        if line == '':
            continue
        full_name, abbrev = _normalize(line)
        print full_name, '-', abbrev

if __name__ == "__main__":
    print_out(states)
    print to_json(states, True)
