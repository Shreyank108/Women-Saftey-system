import phonenumbers 
from phonenumbers import geocoder 
import opencage 
import folium 
import pywhatkit


number="+92"
p=phonenumbers.parse(number) 
location=geocoder.description_for_number(p,"en") 
print(location) 
from phonenumbers import carrier 
sercicer_pro=phonenumbers.parse(number) 
print(carrier.name_for_number(sercicer_pro,"en"))
from opencage.geocoder import OpenCageGeocode
key='e63e7abeb******missing****0'
    
geocoder=OpenCageGeocode(key) 
query=str(location) 
results=geocoder.geocode(query) 

lat=results[0]['geometry']['lat'] 
lng=results[0]['geometry']['lng'] 
print(lat,lng) 

mymap=folium.Map(location=[lat,lng],zoom_start=9) 
folium.Marker([lat,lng],popup=location).add_to(mymap)  

mymap.save("mylocation.html") 
pywhatkit.sendwhats_image('+9162',mymap)