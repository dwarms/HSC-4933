import requests

# API request URL
# https://api.census.gov/data/{year}/{dataset}?get={variables}&for={geography}

YEAR = 2024
DATASET = "acs/acs1"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "4bc3146799ea47dcbd8405e6c90b078e9a94ef93"

state_fips = input("Enter the State FIPS code(s) that you would like data for: ")

variables = input("Enter the variable names that you would like data for: ")

params = {
    "get": f"NAME,{variables}",
    "for": f"state:{state_fips}",
    "key": API_KEY
}

response = requests.get(URL, params=params)
response.raise_for_status()

if response.status_code != 200:
    print(f"Request failed ({response.status_code})")
    print(response.text)
    raise SystemExit(1)

data = response.json()

print(f"Found {len(data) - 1} Rows of Data.")

for i in data:
    print(i)