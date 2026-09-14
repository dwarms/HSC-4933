# Import Libs

import json
import os
import datetime
from decimal import Decimal
from anonymate.anonymizer import Anonymizer
from cryptography.fernet import Fernet

# Pt profiles

profiles = [
    {'job': 'Agricultural engineer',
     'company': 'Phillips-Johnson',
     'ssn': '055-51-3629',
     'residence': '1107 Brian Coves\nSouth Jessica, UT 66862',
     'current_location': (Decimal('-81.6575675'), Decimal('111.794874')),
     'blood_group': 'B+',
     'website': ['https://hurley.com/', 'http://www.baker.info/', 'http://silva-jones.com/', 'https://www.mathews.com/'],
     'username': 'nnelson',
     'name': 'Oscar Newman',
     'sex': 'M',
     'address': '2574 Scott Manors\nPort Aprilfort, MI 13337',
     'mail': 'wgraham@hotmail.com',
     'birthdate': datetime.date(1927, 1, 19)},

    {'job': 'Engineer, civil (consulting)',
     'company': 'Guzman Inc',
     'ssn': '457-09-3674',
     'residence': '8014 Lambert Ways Apt. 285\nSouth Briannaside, KS 13217',
     'current_location': (Decimal('61.686331'), Decimal('-42.036583')),
     'blood_group': 'A-',
     'website': ['http://gregory-martin.org/', 'http://tanner.org/', 'https://www.carr.org/'],
     'username': 'lking',
     'name': 'Jeremy Wilson',
     'sex': 'M',
     'address': '9375 Thomas Alley Suite 536\nNorth Darren, AZ 22956',
     'mail': 'hdeleon@hotmail.com',
     'birthdate': datetime.date(1996, 10, 12)},

    {'job': 'Information officer',
     'company': 'Green Inc',
     'ssn': '230-42-2169',
     'residence': 'Unit 6625 Box 0858\nDPO AE 52466',
     'current_location': (Decimal('-78.802646'), Decimal('-47.996111')),
     'blood_group': 'A-',
     'website': ['https://www.watkins.com/', 'http://johnson.org/'],
     'username': 'timothycastro',
     'name': 'Kenneth Rhodes',
     'sex': 'M',
     'address': '7994 Pearson Square\nHannahmouth, FM 16699',
     'mail': 'sonya72@hotmail.com',
     'birthdate': datetime.date(2003, 6, 15)},

    {'job': 'Contracting civil engineer',
     'company': 'Smith-Williamson',
     'ssn': '796-76-1297',
     'residence': '0041 Brittany Mountains\nNorth Harryshire, MN 69202',
     'current_location': (Decimal('66.422320'), Decimal('107.124001')),
     'blood_group': 'AB+',
     'website': ['http://www.nolan.com/'],
     'username': 'debraphillips',
     'name': 'Nicole Richardson',
     'sex': 'F',
     'address': '303 Wong Trafficway Suite 883\nLake Kiara, MN 78039',
     'mail': 'andrew33@gmail.com',
     'birthdate': datetime.date(2003, 9, 7)},

    {'job': 'Engineer, technical sales',
     'company': 'Moody-Meza',
     'ssn': '574-63-6422',
     'residence': '74438 Moore Fall\nSouth Andrew, GA 64257',
     'current_location': (Decimal('38.089195'), Decimal('35.459581')),
     'blood_group': 'A+',
     'website': ['https://brooks-moore.com/'],
     'username': 'xlewis',
     'name': 'Gary Gamble',
     'sex': 'M',
     'address': '9929 Henderson Branch Suite 961\nLake Mary, AL 36478',
     'mail': 'ambercordova@yahoo.com',
     'birthdate': datetime.date(1968, 8, 19)}]

# Load or create persistent encryption key

KEY_FILE = "encryption.key"

if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        encryption_key = f.read()

else:
    encryption_key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(encryption_key)

# Initialize Anonymizer engine
anonymizer = Anonymizer(encryption_key)

# Define profiles
print("Patient Profiles:")

for profile in profiles:
    print(profile['name'])

# Prompt for specific profile
patient_name = input("Enter name of patient whose profile you would like to view:")

selected_profile = None

for profile in profiles:
    if profile['name'] == patient_name:
        selected_profile = profile

if selected_profile == None:
    print("Patient not found. Please try again.")

else:
    # Prompt for specific information
    profile_query = input("Profile information options: Name, DOB, Sex, Blood Type:")

    if profile_query == "Name":
        print(selected_profile["name"])

    elif profile_query == "DOB":
        print(selected_profile["birthdate"])

    elif profile_query == "Sex":
        print(selected_profile["sex"])

    elif profile_query == "Blood Type":
        print(selected_profile["blood_group"])

    else:
        print("Data not found. Please try again.")

# Create boolean for encryption

encrypt_decision = input("Would you like to encrypt patient data? (y/n):")
if encrypt_decision == "y":
    data_str = json.dumps(profiles, default=str)
    secure_data = anonymizer.encrypt_text(data_str)

    print("Encrypted Data: ")
    print(secure_data)

elif encrypt_decision == "n":
    print("Data not encrypted.")

else:
    print("Invalid input. Please try again.")