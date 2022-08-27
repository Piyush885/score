from flask import Flask
from flask import jsonify
import requests 


app = Flask(__name__)


@app.route('/')
def hello_world():
    a = requests.get('http://172.20.122.101:8000/track/api/630724cd116075e867c083fa')
    c = a.json()
    d = c['data']
    l = d['hardware_data']
    temp = []
    humidity = []
    for i in l:
        temp.append(i['temperature'])
        humidity.append(i['humidity'])
    lt = 26.00
    ut = 40.00
    lt1 = 20
    ut1 = 30
    count = 0
    count1 = 0
    for i in temp:
        if i>=lt and i<=ut:
            count+=1
    scoretemp = count/len(temp)
    for i in temp:
        if i>=lt1 and i<=ut1:
            count1+=1
    scorehumidity = count/len(humidity)   
    finalscore = ((scoretemp + scorehumidity)/2)*100
    
    return {"score":finalscore}


app.run(port=8000)      

              

    