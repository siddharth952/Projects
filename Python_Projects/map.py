import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#Functions
def color_gen(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

    

tileset_id = "http://api.mapbox.com/v4/mapbox.light/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiaGFsZnBvbHlnb24iLCJhIjoiY2p5MGN4OG1qMDFyNzNubGFhdTJ5c3d6biJ9.zyGKocRJ0XJCUbhyCGfXCg" 

mymap = folium.Map(location=[38.58, -99.09], zoom_start=6,tiles= tileset_id, attr="any text here")

#Feature Group
fg = folium.FeatureGroup(name= "My Map")

#zip func to interate through two lists at the same time
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location = [lt,ln],radius= 5 ,popup=str(el)+"  m" , fill_color = color_gen(el),color = 'grey', fill_opacity = 0.7  ))
    

fg = add_child(folium.GeoJson())


mymap.add_child(fg)

mymap.save("Mapfile.html")


