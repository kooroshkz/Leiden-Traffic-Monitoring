import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

url_template = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"

coords = [
    (52.1548439, 4.4721623), (52.1683388, 4.4860599), (52.1476338, 4.4752352),
    (52.1686146, 4.4931477), (52.1519037, 4.5206045), (52.1632703, 4.4582134),
    (52.1417215, 4.4768956), (52.156569, 4.4950595), (52.1635883, 4.4580728),
    (52.1597215, 4.4968029), (52.1549858, 4.4949476), (52.1681008, 4.4864105),
    (52.1521453, 4.5208762), (52.1544488, 4.440454)
]

for lat, lon in coords:
    params = {
        "key": API_KEY,
        "point": f"{lat},{lon}"
    }
    r = requests.get(url_template, params=params)
    data = r.json()
    
    speed = data["flowSegmentData"]["currentSpeed"]
    free = data["flowSegmentData"]["freeFlowSpeed"]
    conf = data["flowSegmentData"]["confidence"]
    
    print(f"{lat},{lon} → {speed} / {free} km/h | Confidence: {conf}")
