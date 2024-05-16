
import json
# Path to the JSON file
file_path='default.json'
# Open and load the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
    
'''fruit1={"name":"apple","country":"india","type":{"genus":"1","species":"2"}}
print(fruit1["type"]["species"])
fruit1["type"]["species"]='3'
print(fruit1)'''

'''JSON access, update, saving
Add “back” to side supported list in all countries with name starting with A'''

'''data['alb']['dl']['supportedSide'].append("back")
print(data['alb'])
output:-{'dl': {'supportedSide': ['front', 'back']'''

'''for country in data:
    if country[0]=='a':
        for document in data[country]:
            data[country][document]['supportedSide'].append('back')
print(data['usa'])'''

#Add a new country “sww” which has same configuration as “alb” and save the json as a new text file
## Copy the configuration of 'alb'
new_country_config=data['alb']
#Add a new country 'sww'
data['sww']=new_country_config

# Path to the new JSON file
new_file_path = 'new default_with_sww.txt'

# Save the new JSON data to a new file
with open(new_file_path, 'w') as new_file:
    json.dump(data, new_file)
print(data.keys())
print(len(data.keys()))


