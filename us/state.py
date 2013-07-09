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

def to_json(flat=True):
    """
    
    @param flat: If True, return a JSON string which has minimal structure. See state_json1.sjon
                 If False, return a JSON string that has JavaScript objects. See state_json2.sjon
    """
    ret = []
    for line in iter(states.splitlines()):
        if line == '':
            continue
        full_name, abbrev = _normalize(line)
        if flat is True:
            ret.append([full_name, abbrev])
        else:
            ret.append({'name': full_name, 'abbrev': abbrev})
    return json.dumps(ret)

def to_sql(name_field='name', abbrev_field='abbrev'):
    '''
    Table schema (PostgreSQL)
    
    CREATE TABLE us_states (sid SERIAL NOT NULL, name VARCHAR(30), abbrev CHAR(2))
    '''
    sql = 'INSERT INTO us_states (%s, %s) VALUES ' % (name_field, abbrev_field)
    values = []
    for line in iter(states.splitlines()):
        if line == '':
            continue
        full_name, abbrev = _normalize(line)
        values.append("('%s', '%s')" % (full_name, abbrev))
    return sql + ','.join(values)

def print_out():
    for line in iter(states.splitlines()):
        if line == '':
            continue
        full_name, abbrev = _normalize(line)
        print full_name, '-', abbrev

if __name__ == "__main__":
    print_out()
    print to_json(True)
    print to_sql()
