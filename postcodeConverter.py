import csv
import requests
import time


with open('clubs-without-lat-long.csv') as f:
     reader = csv.reader(f)
     header_row = next(reader)
     print(header_row)


     with open('clubsInRange.csv', 'w', encoding='UTF8') as clubsInRange:
        writer = csv.writer(clubsInRange)
        writer.writerow(header_row)

        for row in reader:
            postcode = row[9]


            
            r =requests.get('https://geocode.xyz/'+postcode+'?json=1')
            print(r.text)
            time.sleep(30)

            # if distance(centerLatitude, clubLatitude, centerLongitude, clubLongitude) < limit:
                # print(centerLatitude, clubLatitude, centerLongitude, clubLongitude)
                # writer.writerow([centerLatitude, clubLatitude, centerLongitude, clubLongitude])