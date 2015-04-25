''' @author : Harish '''

from flask import Flask
import GoogleMapRelated
 
app=Flask(__name__)
@app.route('/')
def index():
	obj=GoogleMapRelated.GoogleMapsClass()
        lat_long=obj.getLocation(address="BTM Stage 2 Bangalore karnataka") 
	return "Latitued and Longitude of the place is "+str(lat_long)

if __name__=='__main__':
	app.run(debug=True)


