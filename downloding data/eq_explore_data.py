from pathlib import Path
import json
import plotly.express as px

path = Path("ep_data/eq_data_30_day_m1.geojson")
contents = path.read_text(encoding='utf8')
all_eq_data = json.loads(contents)

# create a more readable version of data 
#path = Path("ep_data/readable_eq_data.geojson")
#readable_content = json.dumps(all_eq_data , indent=4)
#path.write_text(readable_content ) 

#examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags , lons ,lats ,eq_titles =[] ,[] ,[] ,[] 
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(title)

print(mags[:5])
print(lons[:5])
print(lats[:5])

title = 'Global earthquakes'
fig = px.scatter_geo(lat = lats ,size = mags, lon = lons , title = title,color=mags,
color_continuous_scale='Viridis',
labels={'color':'Magnitude'},
projection='natural earth',
hover_name = eq_titles
 )
fig.show()
fig.show()