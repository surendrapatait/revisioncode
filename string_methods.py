name="Surendra"
print(name.zfill(2))

import sys
sys.exit(0)


name='Surendraddf 345455'
print(name.translate("name"))
import sys
sys.exit(0)

name='Dhruv'
print(name.ljust("Surendra","Patait="))
import sys
sys.exit(0)


name="Surendra"
lname="patait"
print(name.join('lname'))
import sys
sys.exit(0)



name ="53545413154145 44154544555"
print(name.isdigit())
print(name.islower())
print(name.isprintable())
print(name.isspace())   # only for Space
print(name.isupper())

import sys
sys.exit(0)
name='58855'
print(name.isalnum())
import sys
sys.exit(0)
name="052453665546.0"
print(name.isdecimal())
import sys
sys.exit(0)


name="definatiom 58"
print(name.isidentifier())
import sys
sys.exit(0)

name ="5WWW%`8"
print(name.isascii())
import sys
sys.exit(0)
name ="5354541315414544154544555"
print(name.isnumeric())    # space are not allowed
import sys
sys.exit(0)



name ="surendrapataitdhruVsurendrapatait"
print(name.isalpha())    # space are not allowed
import sys
sys.exit(0)


name="surendra b patait dhruv surendra patait"
print(name.index('surendra'))
import sys
sys.exit(0)

name="surendra b patait.\t\t \n \n dhruv surenda patait"
print(name.format())
print(name.format_map(name))
import sys
sys.exit(0)



name="surendra b patait.dhruv surenda patait"
print(name.find('patait'))   # give the index position
print(name.find('pataut'))

import sys
sys.exit(0)


name="surendra b patait.dhruv surenda patait"
print(name.endswith("it"))
import sys
sys.exit(0)

name="surendra b patait.dhruv surenda patait"
print(name.count('a'))
print(name.count('patait'))
print(name.count("Patait"))    # zero bcs python is case sensitive langasuge
import sys
sys.exit(0)



name="surendra b patait.dhruv surenda patait"
print(len(name))
print(name.center(50))
print(name.center(50,'@'))


import sys
sys.exit(0)


name="SURENDRA B PATAIT.DHRUV SURENDA PATAIT"
print(name.casefold())
import sys
sys.exit(0)

name="surendra b patait.dhruv surenda patait"
print(name.capitalize())



