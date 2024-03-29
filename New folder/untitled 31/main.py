import requests

MY_LAT = 19.180267
MY_LONG = 77.308044

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
    }

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(data)
