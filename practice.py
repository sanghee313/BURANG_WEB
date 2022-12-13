import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db
from ast import literal_eval
import json


cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
	'databaseURL' : 'https://bumrang-36405-default-rtdb.asia-southeast1.firebasedatabase.app'
})

ref = db.reference("Total_Data")

waterdata= ref.get()
print(waterdata)
print(type(waterdata)) #이미 사전 객체

wol_value  =  waterdata ['Wolpyeongdong']
shin_value  =  waterdata ['shintanjin']
song_value  =  waterdata ['songchondong']
semi_value  =  waterdata ['semisosa']


wol_NTU = wol_value.get("NTU")
wol_chroline = wol_value.get("chroline")
wol_pH = wol_value.get("pH")

shin_NTU = shin_value.get("NTU")
shin_chroline = shin_value.get("chroline")
shin_pH = shin_value.get("pH")

song_NTU = song_value.get("NTU")
song_chroline = song_value.get("chroline")
song_pH = song_value.get("pH")

semi_temperature = semi_value.get("temperature")
semi_tubility = semi_value.get("tubility")


print(wol_NTU)
print(wol_chroline)
print(wol_pH)

print(shin_NTU)
print(shin_chroline)
print(shin_pH)

print(song_NTU)
print(song_chroline)
print(song_pH)

print(semi_temperature)
print(semi_tubility)


