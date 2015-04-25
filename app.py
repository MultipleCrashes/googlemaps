''' @author : Harish '''

from flask import Flask
import GoogleMapRelated
import json
 
app=Flask(__name__)
@app.route('/')
def index():
	obj=GoogleMapRelated.GoogleMapsClass()
        lat_long=obj.getLocation(address="BTM Stage 2 Bangalore karnataka") 
        	
	nearByPlaces=obj.getNearbyPlaces(lat=lat_long["lat"],long=lat_long["lng"],type='school',name='school',key='AIzaSyCxuL9ReVu19BS2ZaFuMxB-3E2uPVo2ZHM')
	return "Latitued and Longitude of the location  "+str(lat_long)+ str(nearByPlaces)
	


if __name__=='__main__':
	app.run(debug=True)






