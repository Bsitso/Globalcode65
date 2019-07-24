'''import requests
r = requests.get("https://maker.ifttt.com/trigger/Beautiful/with/key/p0jWqMouy0MlwbXYQ6oQeSjaHnAcmIrLJhqzwRXciJ2")
c = r.status_code
print(c)'''


'''import requests
r = requests.get("https://maker.ifttt.com/trigger/HTU/with/key/p0jWqMouy0MlwbXYQ6oQeSjaHnAcmIrLJhqzwRXciJ2")

c = r.status_code
print(c)'''



import requests

name = "Bridget"
message = "Hi, how was lunch? you are splendid."

r = requests.get("https://maker.ifttt.com/trigger/message/messenger/with/key/2Kud4E0CUmxZX3JAbrzbl")

print(r)

requests()



