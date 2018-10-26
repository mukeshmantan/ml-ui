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
from flask import request
import sys
# import the standard JSON parser
import json
from google.protobuf.json_format import MessageToJson
import json
import requests
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/vm-predictor-ui/directory'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    print ('Hello world****')
    return "Hello, World!"


@app.route('/upload')
def upload_file():
   return render_template('upload.html')
    
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return render_template('upload.html')
      
if __name__ == '__main__':
    #app.run(debug=True)
    app.debug = True
    app.run(host='127.0.0.1', port=8083)
