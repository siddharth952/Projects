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

#Feature Groups
fgV = folium.FeatureGroup(name= "Volcanoes")
fgP = folium.FeatureGroup(name= "Population")

#MARK: Marker Layer
#zip func to interate through two lists at the same time
for lt,ln,el in zip(lat,lon,elev):
    fgV.add_child(folium.CircleMarker(location = [lt,ln],radius= 5 ,popup=str(el)+"  m" , fill_color = color_gen(el),color = 'grey', fill_opacity = 0.7  ))
    
#MARK: Json Layer
fgP.add_child(folium.GeoJson(data = open('world.json','r', encoding = 'utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'
}
))




mymap.add_child(fgV)
mymap.add_child(fgP)
mymap.add_child(folium.LayerControl())
mymap.save("Mapfile.html")


