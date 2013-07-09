# coding: utf-8
'''
Created on Jul 9, 2013

@author: pcdinh
'''
'''
Created on Jul 9, 2013

@author: dinhpham
'''
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

if __name__ == "__main__":
    for line in iter(states.splitlines()):
        if line == '':
            continue
        most_right_ws = line.rfind(' ')
        print line[:most_right_ws].strip().lower().title(), '-', line[most_right_ws:]
