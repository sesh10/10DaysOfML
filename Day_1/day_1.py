import numpy as np
import matplotlib.pyplot as plt
import pycountry_convert as pc
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv(r'D:\time_series_2019-ncov-Confirmed.csv')

data_fin = pd.DataFrame(data)
data_date = pd.DataFrame(data)

print(data_fin)

cols = list(data_fin.columns.values)

print(cols)

ans = []

for i in cols[4:]:
    c = 0
    for j in range(487):
        if data_fin[i][j] == 0:
            c += 1
        else:
            continue
    if c/487 > 0.7:
        data_fin = data_fin.drop(columns=i)

print(data_fin)


# country plot for 22/3/20

plt.plot(data_fin['Country'].head(), data_fin['3/22/20'].head())
plt.xlabel('Country-wise')
plt.ylabel('No. of cases')
plt.show()

# date wise for Italy

req = data_date.loc[data_date['Country'] == 'Italy'].to_string(header=None).split()
plt.bar(cols[-5:], req[-5:])
plt.xlabel('Dates')
plt.ylabel('No. of cases')
plt.show()


# continent plot

country = [data_date['Country'][j] for j in range(data_date.shape[0])]
country_cases = [data_date['3/22/20'][j] for j in range(data_date.shape[0])]
world = {}

def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name


for i in range(90):
    continent_name = country_to_continent(country[i])
    if continent_name not in world:
        world[continent_name] = country_cases[i]
        
    elif continent_name in world:
        world[continent_name] += country_cases[i]
    else:
        continue



plt.bar(list(world.keys()), list(world.values()))
plt.xlabel('Continents')
plt.ylabel('Confirmed Cases')
plt.show()



