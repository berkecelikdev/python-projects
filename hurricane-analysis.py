# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(damages):
    updated = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated.append(damage)
        else:
            last_char = damage[-1]
            number = float(damage[:-1])
            updated.append(number * conversion[last_char])
    return updated

# test function by updating damages
updated_damages = update_damages(damages)
#print(updated_damages)

# 2
# Create a Table
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}

    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name" : names[i],
            "Month" : months[i],
            "Year" : years[i],
            "Max Sustained Winds" : max_sustained_winds[i],
            "Areas Affected" : areas_affected[i],
            "Damages" : damages[i],
            "Deaths" : deaths[i],
        }
    return hurricanes

# Create and view the hurricanes dictionary
hurricanes = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(f"Hurricanes: {hurricanes}")
print(f"Cuba I: {hurricanes["Cuba I"]}")
print(f" Katrina: {hurricanes["Katrina"]}")

# 3
# Organizing by Year
def hurricanes_by_year(hurricanes):
    by_year = {}

    for hurricane in hurricanes.values():
        year = hurricane["Year"]
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(hurricane)
    return by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year_dict = hurricanes_by_year(hurricanes)
print(f"Hurricanes in 1932: {hurricanes_by_year_dict[1932]}")
print(f"Hurricanes in 2005: {hurricanes_by_year_dict[2005]}")

# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes):
    area_counts = {}

    for hurricane in hurricanes.values():
        for area in hurricane["Areas Affected"]:
            if area not in area_counts:
                area_counts[area] = 0
            area_counts[area] += 1
    return area_counts

# create dictionary of areas to store the number of hurricanes involved in
area_counts = count_affected_areas(hurricanes)
print(f"Area counts: {area_counts}")

# 5
# Calculating Maximum Hurricane Count
def most_affected_area(area_counts):
    max_area = max(area_counts, key = lambda area: area_counts[area])
    return max_area, area_counts[max_area]

# find most frequently affected area and the number of hurricanes involved in
area, count = most_affected_area(area_counts)
print(f"Most affected area: {area} ({count} hurricanes)")

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
    max_hurricanes = max(hurricanes.values(), key = lambda h: h["Deaths"])
    return max_hurricanes["Name"], max_hurricanes["Deaths"]

# find highest mortality hurricane and the number of deaths
name, deaths = deadliest_hurricane(hurricanes)
print(f"Deadliest hurricane: {name} ({deaths} deaths)")

# 7
# Rating Hurricanes by Mortality
mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000}

def rate_by_mortality(hurricanes):
    mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes.values():
        deaths = hurricane["Deaths"]
        rating = 0
        for level, upper_bound in mortality_scale.items():
            if deaths > upper_bound:
                rating = level + 1
        mortality_dict[rating].append(hurricane)
    return mortality_dict

# categorize hurricanes in new dictionary with mortality severity as key
mortality_dict = rate_by_mortality(hurricanes)

for rating, hurricanes_list in mortality_dict.items():
    names = [h["Name"] for h in hurricanes_list]
    print(f"Rating: {rating}: {names}")

# 8 Calculating Hurricane Maximum Damage
def most_damaging_hurricane(hurricanes):
    max_hurricane = max(
        (h for h in hurricanes.values() if h["Damages"] != "Damages not recorded"),
        key = lambda h: h["Damages"]
    )
    return max_hurricane["Name"], max_hurricane["Damages"]

# find highest damage inducing hurricane and its total cost
name, damage = most_damaging_hurricane(hurricanes)
print(f"Most damaging hurricane: {name} (${damage:,.0f})")

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def rate_by_damage(hurricanes):
    damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes.values():
        damage = hurricane["Damages"]
        if damage == "Damages not recorded":
            continue
        rating = 0
        for level, upper_bound in damage_scale.items():
            if damage > upper_bound:
                rating = level + 1
        damage_dict[rating].append(hurricane)
    return damage_dict

# categorize hurricanes in new dictionary with damage severity as key
damage_dict = rate_by_damage(hurricanes)

for rating, hurricanes_list in damage_dict.items():
    names = [h["Name"] for h in hurricanes_list]
    print(f"Rating: {rating} : {names}")

