import json

with open('./export.geojson', 'r') as f:
    data = json.load(f)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Traffic Signals Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <style>
        #map { height: 600px; width: 100%; }
        .yellow { background-color: rgba(255, 255, 0, 0.3); }  /* 30% transparent yellow */
        .red { background-color: red; }
    </style>
</head>
<body>
    <h1>Traffic Signals</h1>
    <div id="map"></div>
    <script>
        var map = L.map('map').setView([52.141726, 4.4864872], 13); // Initial view set to first coordinates

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        var markers = [];

"""

marker_code = ""
for idx, feature in enumerate(data['features']):
    coords = feature['geometry']['coordinates']
    lat, lon = coords[1], coords[0]
    
    color = 'red' if (idx + 1) % 26 == 0 else 'yellow'
    
    marker_code += f"""
        var marker_{idx} = L.marker([{lat}, {lon}], {{icon: L.divIcon({{
            className: '{color}',
            html: '<div style="width: 10px; height: 10px; border-radius: 50%;"></div>'
        }})}}).addTo(map);
    """

html_template += marker_code + """
    </script>
</body>
</html>
"""

with open('traffic_signals_map.html', 'w') as f:
    f.write(html_template)

print("HTML file has been generated: traffic_signals_map.html")
