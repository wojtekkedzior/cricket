import csv
# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt

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

with open('clubs.csv') as f:
     reader = csv.reader(f)
     header_row = next(reader)
     print(header_row)

     with open('clubsInRange.csv', 'w', encoding='UTF8') as clubsInRange:
        writer = csv.writer(clubsInRange)
        writer.writerow(header_row)

        #   colechester - CO1 1RQ  - 51.89548,0.89597
        centerLatitude = 51.89548
        centerLongitude = 0.89597

        limit = 20

        writer.writerow(["Center", "", "","","","","","","","",centerLatitude, centerLongitude])

        for row in reader:
            clubLatitude = float(row[10])
            clubLongitude = float(row[11])

            if distance(centerLatitude, clubLatitude, centerLongitude, clubLongitude) < limit:
                print(centerLatitude, clubLatitude, centerLongitude, clubLongitude)
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], clubLatitude, clubLongitude])




# header = ['name', 'area', 'country_code2', 'country_code3']
# data = ['Afghanistan', 652090, 'AF', 'AFG']



#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)


     
     
# # driver code
# lat1 = 53.32055555555556
# lat2 = 53.31861111111111
# lon1 = -1.7297222222222221
# lon2 =  -1.6997222222222223

