''' @author : Harish '''
import pygmaps
import os 
import requests
import json 
import ast
import time 


class GoogleMapsClass:
		def __init__(self,clientKey="AIzaSyCxuL9ReVu19BS2 \
                                            ZaFuMxB-3E2uPVo2ZHM"):
			self.clientKey=clientKey
		        	
		def getLocation(self,address=None):
			'''Function to get latitue and longitude of an address'''

			r=requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='   \
					+address+'&key=AIzaSyCxuL9ReVu19BS2ZaFuMxB-3E2uPVo2ZHM')
			responseString=json.dumps(json.loads(r.text))
			time.sleep(2)
			resp=ast.literal_eval(responseString)		
			
			#print "The Latitude and Longitude for the given address is "+str(resp['results'][0]['geometry']['location'])
			lat=resp['results'][0]['geometry']['location']['lat']
			long=resp['results'][0]['geometry']['location']['lng']
			locationmap=pygmaps.maps(lat,long,10)
			locationmap.draw('./locationmap.html')
			return resp['results'][0]['geometry']['location']



		def getNearbyPlaces(self,latitude=None,longitude=None,type=None,
                                    name="None",radius=None,key='AIzaSyCxuL9ReVu19BS2ZaFuMxB-3E2uPVo2ZHM'):
	
			'''Function to get different types of things in certain areas'''
			print "The place name is-> ",name
			placesQuery="https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+   \
				     str(lat)+","+str(long)+"&radius="+str(radius)+"&types="+str(type)+"&name="+  \
                                     str(name)+"&key="+str(key)
			#placesQuery="https://maps.googleapis.com/maps/api/place/nearbysearch/json?"+str(lat)+","+str(long)
			print "---------->",placesQuery
			#placesQuery="https://www.google.co.in/maps/search/json/"+placeName+"/@"+str(lat)+","+str(long)+",1z"	
			resp=requests.get(placesQuery)
			try:
				print "The places near the current place is --->", str(json.dumps(json.loads(resp.text),indent=4))
			except Exception as e:
				print "Exception found "	
			return json.dumps(json.loads(resp.text))
			
			



if __name__=='__main__':
	obj=GoogleMapsClass()
	#obj.getNearbyPlaces(lat=12.9,long=77.6,placeName='school')
	Location = obj.getLocation(address="BTM Bangalore")
	print "Location ->",Location
	print "Latitute ->",Location["lat"]
	print "Longitued ->",Location["lng"]
	lat = Location["lat"]
	long =Location["lng"]
	obj.getNearbyPlaces(latitude=12.9,longitude=77.6,type="hotels",name="oxford Mens",radius=500)

