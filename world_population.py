import json 
filename = 'population_data.json'
from country_codes import get_country_code
with open(filename) as f:
	pop_data = json.load(f)

for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population =int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			
		print(country_name+':'+ str(population))