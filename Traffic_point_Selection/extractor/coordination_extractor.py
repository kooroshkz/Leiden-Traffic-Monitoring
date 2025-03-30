import json
import csv

with open('./export.geojson', 'r') as f:
    data = json.load(f)

coordinates = []

for idx, feature in enumerate(data['features']):
    if (idx + 1) % 26 == 0:
        coords = feature['geometry']['coordinates']
        lat, lon = coords[1], coords[0]
        coordinates.append([lat, lon])

with open('coordinates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Latitude', 'Longitude'])
    writer.writerows(coordinates)

print("CSV file with coordinates has been generated: coordinates.csv")
