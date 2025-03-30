### Traffic Point Selection

Data gathered from the following sources:
- [Overpass-turbo](https://overpass-turbo.eu/)

Using the query:
```xml
[out:json][timeout:25];
area["name"="Leiden"]->.searchArea;
node
  ["highway"="traffic_signals"]
  (area.searchArea);
out body;
```

### Data selection:

As we have 364 traffic signals in the Leiden area, we will select 14 which is 364 mod(26)