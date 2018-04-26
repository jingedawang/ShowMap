# -*- coding: utf-8 -*-
import os
import json
import sys
import time
from flask import Flask, url_for, Response, jsonify, request, send_file
from flask_cors import *
app = Flask(__name__)
CORS(app, supports_credentials=True)

reload(sys)
sys.setdefaultencoding('utf8')

def doSomeThing(parameters):
    os.system('./')
    pass

@app.route('/')
def api_root():
    print(request.form)
    print(request.values)
    parameters = request.values.get('parameters')
    # doSomeThing(parameters)
    return 'finish'

@app.route('/index')
def api_index():
    return send_file('map-bin.html')

@app.route('/pathplanning')
def api_pathplanning():
    # path planning
    data = [[0,0,1],[5,5,1]]
    start = time.time()
    os.system(u'/home/wjg/projects/AntPathPlanning/cmake-build-debug/AntPathPlanning')
    # os.system(u'/home/wjg/projects/AStarPathPlanning/cmake-build-debug/AStarPathPlanning')
    end = time.time()
    dataFile = open(u'out.txt', 'r')
    #dataFile = open(u'D:/PathPlanning/out.txt', 'r')
    line = dataFile.read()
    print line
    print "time used " + str(end - start) + "s"
    #jsonText = json.dumps(data)
    return line

if __name__ == '__main__':
    app.run(port=11222)
