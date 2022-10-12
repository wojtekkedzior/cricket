import csv
import argparse
# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("la", help="Latitude.")
parser.add_argument("lo", help="Longitude.")
parser.add_argument("limit", help="max distance from centre in km")

args = parser.parse_args()
print(args)

def isWithInRange(latitude, longitude):
    print(latitude, longitude)

def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)

with open('currentClubs.csv') as f:
     reader = csv.reader(f)
     header_row = next(reader)

     with open('clubsInRange.csv', 'w', encoding='UTF8') as clubsInRange:
        writer = csv.writer(clubsInRange)
        writer.writerow(header_row)

        centerLatitude = float(args.la)
        centerLongitude = float(args.lo)
        limit = int(args.limit)

        writer.writerow(["Center","","","","","","","","","",centerLatitude, centerLongitude])

        for row in reader:

            if row[10] == "":
              continue
            
            clubLatitude = float(row[10])
            clubLongitude = float(row[11])

            if distance(centerLatitude, clubLatitude, centerLongitude, clubLongitude) < limit:
                print(row[0], clubLatitude, clubLongitude)
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], clubLatitude, clubLongitude])