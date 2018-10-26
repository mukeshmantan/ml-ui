# -*- coding: utf-8 -*-
# ================================================================================
# ACUMOS
# ================================================================================
# Copyright © 2017 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ================================================================================
# This Acumos software file is distributed by AT&T and Tech Mahindra
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ================================================================================


#!flask/bin/python
from __future__ import print_function
from flask import Flask,jsonify
import json
import requests
from flask import request, render_template
import sys
import model_pb2 as pb
# import the standard JSON parser
import json
from google.protobuf.json_format import MessageToJson
import json
import requests
from werkzeug.utils import secure_filename
import os



restURL = "http://127.0.0.1:9092/classify"

app = Flask(__name__)

APP_ROOT = '/Users/liule/att/lei-connector-cooler/'
UPLOAD_FOLD = 'test'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return render_template('connector_cooler.html')
      

@app.route('/')
def index():
    print ('Hello world****')
    return "Hello, World!"


@app.route('/connectorcooler', methods=['POST']) #GET requests will be blocked
def json_example():

    print ('Connector Cooler is called.')
    req_data = request.get_json()
    print("==============req_data:%s",  req_data)

    SR_REQUEST_DESC = None
    IMAGE = None
    if 'Image' in req_data:
        IMAGE  = req_data['Image']
    
    df = pb.ImageFrame()
    df.Image = IMAGE 
   
    dfs = pb.ImageFrameSet()
    dfs.frames.extend([df])
    input = dfs.SerializeToString()
    
    res = requests.post(restURL, input)
    print("#############result status:%s", res)
    of = pb.ClassifyOut()
    of.ParseFromString(res.content)
    list = []
    for result in of.value:
        print("#############Image Classification Result=%s",result)
        list.append(result)
    return json.dumps(list) 
     

if __name__ == '__main__':
    #app.run(debug=True)
    app.debug = True
    app.run(host='127.0.0.1', port=8081)
