from flask import Flask, redirect ,url_for, render_template
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
	'databaseURL' : 'https://bumrang-36405-default-rtdb.asia-southeast1.firebasedatabase.app'
})

app = Flask(__name__)
app.debug = True

ref = db.reference("Total_Data")

waterdata= ref.get()

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

@app.route("/all")
def phone_user():
    return render_template("all.html",wol_c = wol_chroline,wol_N = wol_NTU, wol_p = wol_pH,shin_c = shin_chroline,shin_p = shin_pH,shin_N = shin_NTU , song_c = song_chroline,song_N = song_NTU,song_p = song_pH,temperature = semi_temperature, tubility = semi_tubility )



@app.route("/semisosa_data")
def show_user():
    # Greet the user
    return render_template("semisosa_data.html",temperature = semi_temperature, tubility = semi_tubility)
  
# Pass the required route to the decorator.
@app.route("/QR")
def hello():
    return render_template("QR.html")
    
@app.route("/")
def index():
    return render_template("index.html")
  
if __name__ == "__main__":
    app.run()