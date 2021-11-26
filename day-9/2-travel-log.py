travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visit, places):
    dico = {
        "country": country,
        "visits": visit,
        "cities": places
    }
    travel_log.append(dico)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
