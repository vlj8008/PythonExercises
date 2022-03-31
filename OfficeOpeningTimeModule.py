
from datetime import datetime
from pytz import timezone
import pytz

def user_input():
    ans = input("Would you like to know which offices are open?")
    if ans == "yes":
        print_offices_open()
    else:
        exit()

def print_offices_open():
#create a variable to get Portland time now.
    portland_time = datetime.now(tz=pytz.UTC).replace(microsecond=0)
    Portland = portland_time.astimezone(pytz.timezone('US/Pacific'))

#create a variable to get NYC time now.

    nyc_time = datetime.now(tz=pytz.UTC).replace(microsecond=0)
    NYC = nyc_time.astimezone(pytz.timezone('US/Eastern'))

#create a variable to get London time now.

    london_time = datetime.now(tz=pytz.UTC).replace(microsecond=0)
    London = london_time.astimezone(pytz.timezone('Europe/London'))


#creating a dictionary
    cities = {'Portland Office': Portland,
          'New York City Office': NYC,
          'London Town Office': London}

#print(cities)

#create loop

    for city in cities:
        branchtime = int(cities[city].strftime('%H'))
        if branchtime >= 9 and branchtime <= 17:
            print(city, cities[city], 'OPEN now')
        else:
            print(city, cities[city], 'CLOSED now')

if __name__ == "__main__":

    user_input()

