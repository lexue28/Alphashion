def locationweather():
    def getlocationcity():
        import geocoder
        g = geocoder.ip('me')
        coordinates = (g.latlng)
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="geoapiExercises")
        Latitude = str(coordinates[0])
        Longitude = str(coordinates[1])
        location = geolocator.reverse(Latitude+","+Longitude)
        address = location.raw['address']
        city = address.get('city', '')
        return city

    thecity = getlocationcity()

    def getTemp():
        import requests, json
        api_key = "4195daa4d106e8855516b85c32e56be9"
        url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = getlocationcity()
        complete_url = url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            celsius = current_temperature - 273.15
            far = celsius * 9/5 + 32
            return int(far), int(current_humidity), str(weather_description)

        else:
            print("what")

    return getTemp()

def locationweather2():
    x = []
    tempf, humidity, weather = locationweather()
    x.append(tempf)
    x.append(humidity)
    x.append(weather)
    return x
#print(locationweather2())

def recommendations():
    #from locationweatherget import locationweather

    recommendationlist = []

    tempf, humidity, weather = locationweather()

    if tempf >= 70:
        recommendationlist.append("t-shirt")
        recommendationlist.append("sandal")
        recommendationlist.append("skirt")
    elif tempf >= 40:
        recommendationlist.append("trousers")
        recommendationlist.append("sneakers")
        recommendationlist.append("shirt")
    elif tempf <= 40:
        recommendationlist.append("pullover shirt")
        recommendationlist.append("boots")
        recommendationlist.append("coat")

    print(recommendationlist)
    return(recommendationlist)
