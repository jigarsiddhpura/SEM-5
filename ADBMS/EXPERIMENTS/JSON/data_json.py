import json

# Read data from the JSON file
with open("D:\SEM-5\ADBMS\EXPERIMENTS\JSON\data.json", 'r') as file:
    data = json.load(file)

# Iterate through the records and print them
for record in data:
    print("Name:", record["name"])
    print("Location:", record["location"])
    print("Country:", record["country"])
    print()