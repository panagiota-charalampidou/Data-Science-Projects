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

# write your update damages function here:
def updated_damages(damages):
  damages_updated = []
  for i in damages:
    if i[-1] == 'B':
      damages_updated.append(float(i[:-1]) * 1000000000)
    elif i[-1] == "M":
      damages_updated.append(float(i[:-1]) * 1000000)
    else:
      damages_updated.append(i)
  return damages_updated

damages_new = updated_damages(damages)


# write your construct hurricane dictionary function here:
def remake_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_new, deaths):
  hurricane_dictionary = {}
  for i in range(0, len(names)):
    key = names[i]
    value = {}
    value.update({"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages_new[i], "Deaths": deaths[i]})
    hurricane_dictionary.update({key:value})
  return hurricane_dictionary

hurricanes = remake_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_new, deaths)


# write your construct hurricane by year dictionary function here:
def hurricane_by_year(year):
   hurricane_by_year = {}
   value_list = []
   for value in hurricanes.values():
     if value.get('Year') == year:
        value_list.append(value)
        hurricane_by_year.update({year:value_list})
   print(hurricane_by_year) 
     
#hurricane_by_year(1932)


# write your count affected areas function here:
#print(hurricanes["Bahamas"]["Areas Affected"])
def count_affected_areas(country):
  new_dict = {}
  count_affected_areas = 0
  for value in hurricanes.values():
    for area in value.get('Areas Affected'):
      if area == country:
        count_affected_areas += 1
  new_dict.update({country: count_affected_areas})
  print(new_dict)

#count_affected_areas = count_affected_areas('Central America')     


# write your find most affected area function here:
areas_count={}
for areas in areas_affected:
    for i in areas:
        if i not in areas_count:
            areas_count[i] = 1
        else:
            areas_count[i] += 1
#print(areas_count)

def most_affected_area(areas_count):
   max_area = ""
   max_area_count = 0
   most_affected_area = {}
   for area in areas_count:
     if areas_count[area] == max(areas_count.values()):
       max_area_count += areas_count[area]
       max_area = area
       most_affected_area.update({max_area : max_area_count})
       print(most_affected_area)

#most_affected_area(areas_count)


# write your greatest number of deaths function here:
death_count = dict(zip(names, deaths))
#print(death_count)
def most_deaths(death_count):
  max_area = ""
  max_count = 0
  max_deaths = {}
  for area in death_count:
    if death_count[area] == max(death_count.values()):
      max_area = area
      max_count += death_count[area]
      max_deaths.update({max_area : max_count})
      print(max_deaths)

#most_deaths(death_count)


# write your catgeorize by mortality function here:
def mortality_scale(death_count):
  mortality_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for area in death_count:
    if death_count[area] == 0:
      mortality_dict[0].append(area)
    elif death_count[area] <= 100:
      mortality_dict[1].append(area)
    elif death_count[area] <= 500:
      mortality_dict[2].append(area)
    elif death_count[area] <= 1000:
      mortality_dict[3].append(area)
    elif death_count[area] <= 10000:
      mortality_dict[4].append(area)
    else:
      mortality_dict[5].append(area)
    print(mortality_dict)
#mortality_scale(death_count)


# write your greatest damage function here:
damages_count = {names:damages_new for (names,damages_new) in zip(names, damages_new) if damages_new != 'Damages not recorded'}
#print(damages_count)

def most_damages(damages_count):
  max_area = ""
  max_count = 0
  max_damages = {}
  for area in damages_count:
    if float(damages_count[area]) == max(damages_count.values()):
      max_area = area
      max_count += float(damages_count[area])
      max_damages.update({max_area:max_count})
      print(max_damages)
#most_damages(damages_count)


# write your catgeorize by damage function here:
def damage_rating(damages_count):
  damage_rating = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for area in damages_count:
    if damages_count[area] == 0:
      damage_rating[0].append(area)
    elif damages_count[area] <= 100000000:
      damage_rating[1].append(area)
    elif damages_count[area] <= 1000000000:
      damage_rating[2].append(area)
    elif damages_count[area] <= 10000000000:
      damage_rating[3].append(area)
    elif damages_count[area] <= 50000000000:
      damage_rating[4].append(area)
    else:
      damage_rating[5].append(area)
    print(damage_rating)

#damage_rating(damages_count)