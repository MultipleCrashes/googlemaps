
''' @author : Harish '''

import os 
import requests
import json 
import ast
import time 


class GoogleMapsRelated:
		def __init__(self,clientKey="AIzaSyCxuL9ReVu19BS2 \
                                            ZaFuMxB-3E2uPVo2ZHM"):
			self.clientKey=clientKey
		        	
		def getLocation(self,address=None):
			r=requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='   \
					+address+'&key=AIzaSyCxuL9ReVu19BS2ZaFuMxB-3E2uPVo2ZHM')
			responseString=json.dumps(json.loads(r.text))
			time.sleep(2)
			resp=ast.literal_eval(responseString)		
			
			print "The Latitude and Longitude for the given address is "+str(resp['results'][0]['geometry']['location'])
			return resp['results'][0]['geometry']['location']





if __name__=='__main__':
	obj=GoogleMapsRelated()
	obj.getLocation(address="1600+Amphitheatre+Parkway,+Mountain+View,+CA+")
