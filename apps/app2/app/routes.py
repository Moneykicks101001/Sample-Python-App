import socket 
import platform 
from flask import Blueprint, jsonify 

api = Blueprint("api", __name__) 

@api.route("/") 
def home(): 
    hostname = socket.gethostname() 
    return jsonify({ 
        "application": "azure-demo-app-2", 
        "hostname": hostname, 
        "platform": platform.system(), 
        "status": "running" 
    }) 


@api.route("/health") 
def health(): 
    return jsonify({ "status": "healthy" })