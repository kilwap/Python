# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


#Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
# write your update damages function here:

def update_damages(damages):
    updated_damages = []
    conversion = {'M': 1000000, 'B': 1000000000}
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        elif damage[-1] == 'M':
            updated_damages.append(float(damage[:-1]) * conversion['M'])
        
        elif damage[-1] == 'B':
            updated_damages.append(float(damage[:-1]) * conversion['B'])
    return updated_damages

updated_damages = update_damages(damages)

#Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
# write your construct hurricane dictionary function here:

def all_in_one(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
  return hurricanes

hurricanes = all_in_one(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)



#Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
# write your construct hurricane by year dictionary function here:

def by_year(hurricanes):
  hurricanes_by_years = {}
  for hurricane in hurricanes.values():
    current_year = hurricane.get('Year')
    current_cane = hurricane
    if current_year in hurricanes_by_years.keys():
      hurricanes_by_years[current_year].append(current_cane)
    else:
      hurricanes_by_years[current_year] = []
      hurricanes_by_years[current_year].append(current_cane)
  return hurricanes_by_years   



#Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
# write your count affected areas function here:

def count_areas(hurricanes):
  affected_areas = {}
  for hurricane in hurricanes.values():
    for area in hurricane['Areas Affected']:
      if area in affected_areas.keys():
        affected_areas[area] += 1
      else:
        affected_areas[area] = 1
  return affected_areas


#Write a function that finds the area affected by the most hurricanes, and how often it was hit.
# write your find most affected area function here:


def most_affected_area(areas):
  for area in areas:
    if areas[area] < max(areas.values()):
      continue
    else:
      max_area = area
      max_area_count = areas[area]
    print(f'The most affected area is {area} it was affected {max_area_count} times')
    return max_area, max_area_count



# write your greatest number of deaths function here:


def max_num_deaths(hurricanes):
    max_mortality_cane = 'Cuba I'
    max_mortality = 0
    for hurricane in hurricanes.values():
      if max_mortality < hurricane['Deaths']:
        max_mortality = hurricane['Deaths']
        max_mortality_cane = hurricane['Name'] 
      else:
        continue
    return max_mortality_cane, max_mortality   



#Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating. Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.
# write your catgeorize by mortality function here:


def cat_mortal(hurricanes):
  mortality_scale = {0: 0,
                     1: 100,
                     2: 500,
                     3: 1000,
                     4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes.values():
    if hurricane['Deaths'] > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricane)
    elif hurricane['Deaths'] > mortality_scale[3]:
      hurricanes_by_mortality[4].append(hurricane)
    elif hurricane['Deaths'] > mortality_scale[2]:
      hurricanes_by_mortality[3].append(hurricane)
    elif hurricane['Deaths'] > mortality_scale[1]:
      hurricanes_by_mortality[2].append(hurricane)
    elif hurricane['Deaths'] > mortality_scale[0]:
      hurricanes_by_mortality[1].append(hurricane)
    elif hurricane['Deaths'] == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricane)
  return hurricanes_by_mortality



#Write a function that finds the hurricane that caused the greatest damage, and how costly it was. Test your function on your hurricane dictionary.
# write your greatest damage function here:


def max_num_deaths(hurricanes):
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for hurricane in hurricanes.values():
    if hurricane['Damage'] == "Damages not recorded":
      continue
    elif max_damage <= hurricane['Damage']:
      max_damage = hurricane['Damage']
      max_damage_cane = hurricane['Name'] 
    elif max_damage > hurricane['Damage']:
      continue
  return max_damage_cane, max_damage  


#Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating. Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
# write your catgeorize by damage function here:


ef cat_mortal(hurricanes):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes.values():
    if hurricane['Damage'] == 'Damages not recorded':
      continue
    elif hurricane['Damage'] > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricane)
    elif hurricane['Damage'] > damage_scale[3]:
      hurricanes_by_damage[4].append(hurricane)
    elif hurricane['Damage'] > damage_scale[2]:
      hurricanes_by_damage[3].append(hurricane)
    elif hurricane['Damage'] > damage_scale[1]:
      hurricanes_by_damage[2].append(hurricane)
    elif hurricane['Damage'] > damage_scale[0]:
      hurricanes_by_damage[1].append(hurricane)
    elif hurricane['Damage'] == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricane)
  return hurricanes_by_damage