import pyowm

apiKey = '3c9eaf32882bfec545d09bbaaf1e59e8'


owm = pyowm.OWM (apiKey)
observation = owm.weather_at_place('Hong kong,China')
#observation_ho = owm.weather_at_place('Ho,Ghana')
w = observation.get_weather()
w = observation.get_weather()


print("The humidity in Hong kong is: " , w.get_humidity())
print("The clouds in Hong kong is: " ,w.get_clouds())