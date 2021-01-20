import pandas as pd
import requests
import googlemaps
import config


def addressToTract(address):
    key = config.googlemapsapikey
    
    #gets coordinates using google maps API
    #google bills me if more than 40,000 requests/month
    gmaps = googlemaps.Client(key = key)
    result = gmaps.geocode(ADDRESS)[0].get("geometry").get("location")
    lat = str(result.get("lat"))
    long = str(result.get("lng"))
    
    #FCC API URL
    FCCAPI1 = "https://geo.fcc.gov/api/census/block/find?latitude="
    FCCAPI2 = "&longitude="
    FCCAPI3 = "&showall=false&format=json"
    
    #Makes URL that works for our coordinates
    website = FCCAPI1 + lat + FCCAPI2 + long + FCCAPI3
    
    #gets data from FCC
    #This API uses the 2010 Census Tracts
    response = requests.get(website)
    
    #extracts geocode
    apiquerry = response.json() 
    df = pd.DataFrame.from_dict(apiquerry)
    geocode = df.iloc[0,0]
    
    #extracts tract from geocode
    tract = geocode[5:11]
    
    return tract



