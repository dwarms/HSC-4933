import requests

# API request URL
# https://api.census.gov/data/{year/{dataset}?get={variables}&for={georgraphy}

YEAR = 2020
DATASET = "dec/pl"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "4bc3146799ea47dcbd8405e6c90b078e9a94ef93"

params = {
    "get": "NAME,P1_001N",
    "for": "state:*",
    "key": API_KEY,

}


response = requests.get(URL, params=params)
response.raise_for_status()

if response.status_code != 200:
    print(f"Request failed ({response.status_code})")
    print(response.text)
    raise SystemExit(1)


data = response.json()

# The API returns a list of lists.


print(f"Got {len(data) -1} rows back.")

for i in data:
    print(i)