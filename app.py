from flask import Flask, jsonify, Response
import time
import fatility
import pedesMotorCycle
import seriousInjury

app = Flask(__name__)


@app.route('/<arunsahu>')
def call_me_test(arunsahu):
    #returnObject = fatility.fatilityMethod()
    #print (returnObject)
    #return jsonify({"message": "Welcome to Gov Hackthon 2018. This is just beginning, much more to come. Version 5:"+arunsahu}, mimetype='application/json')

    ret = '{"message": "Welcome to Gov Hackthon 2018. This is just beginning, much more to come. Version 7 and : '+arunsahu+'"}'

    resp = Response(response=ret,status=200,mimetype="application/json")

    return resp


@app.route('/execute/<timing>/<accidentTime>/<geometry>/<alcoholTime>/<speedZone>/<nodeType>/<latitude>/<longitude>/<priority>')
def call_me(timing, accidentTime, geometry, alcoholTime, speedZone, nodeType, latitude, longitude, priority):
    returnValue = ""
    timing = timing.replace("@@","/")
    accidentTime = accidentTime.replace("@@","/")
    geometry = geometry.replace("@@","/")
    alcoholTime = alcoholTime.replace("@@","/")
    speedZone = speedZone.replace("@@","/")
    nodeType = nodeType.replace("@@","/")
    latitude = latitude.replace("@@","/")
    longitude = longitude.replace("@@","/")
    priority = priority.replace("@@","/")
    
    if priority.lower() == "fatality":
        returnValue = fatility.fatilityMethod(timing, accidentTime, geometry, alcoholTime, speedZone, nodeType, latitude, longitude)
    elif priority.lower() == "serious injury":
        returnValue = seriousInjury.seriousInjury(timing, accidentTime, geometry, alcoholTime, speedZone, nodeType, latitude, longitude)
    else:
        returnValue = pedesMotorCycle.pedesMotor(timing, accidentTime, geometry, alcoholTime, speedZone, nodeType, latitude, longitude)

    print("Returning: "+returnValue)
    #time.sleep(5)
    ret = '{"result": "'+returnValue+'"}'
    resp = Response(response=ret,status=200,mimetype="application/json")
    return resp
    