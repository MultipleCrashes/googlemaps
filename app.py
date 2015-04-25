''' @author : Harish '''

from flask import Flask
import GoogleMapRelated
import json
 
app=Flask(__name__)
@app.route('/')
def index():
	obj=GoogleMapRelated.GoogleMapsClass()
        lat_long=obj.getLocation(address="BTM Stage 2 Bangalore karnataka") 
        	
	obj.getNearbyPlaces(lat=lat_long["lat"],long=77.7,type='school',name='school',key='AIzaSyCxuL9ReVu19BS2ZaFuMxB-3E2uPVo2ZHM')
	return "Latitued and Longitude of the place is "+str(lat_long)

if __name__=='__main__':
	app.run(debug=True)


