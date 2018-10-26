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
import image_slicer
import glob
import json
import shutil



restURL = "http://127.0.0.1:9001/classify"

app = Flask(__name__)

APP_ROOT = '/Users/liule/att/lei-connector-cooler/'
UPLOAD_FOLD = 'test'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      #files = glob.glob('/Users/liule/att/lei-connector-cooler/test/*')
      #for f in files:
       #os.remove(f)
      #f.save(secure_filename(f.filename))
      #shutil.rmtree('/Users/liule/att/lei-connector-cooler/test')
      #os.mkdir('/Users/liule/att/lei-connector-cooler/test')
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      for root, dirs, files in os.walk("/Users/liule/att/lei-connector-cooler/test"):
        for filename in files:
          print(filename)
          tiles = image_slicer.slice('/Users/liule/att/lei-connector-cooler/test/' + filename, 4,save=False)
          image_slicer.save_tiles(tiles, directory='/Users/liule/att/lei-connector-cooler/test',prefix='slice'+filename)
      os.remove("/Users/liule/att/lei-connector-cooler/test/"+ secure_filename(f.filename))

      IMAGE = "/Users/liule/att/lei-connector-cooler/test"
     # if 'Image' in req_data:
      #  IMAGE  = req_data['Image']
      #print(request.headers)
      #data_headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

      # create slice files here
      return render_template('/pages/connector_cooler.html')
      #return redirect(url_for('/pages/connector_cooler.html'))
      

@app.route('/')
def index():
    print ('Hello world****')
    return render_template('index.html')

@app.route('/pages/index.html')
def page_index():
    print ('Hello world****')
    return render_template('/pages/index.html')

@app.route('/pages/connector_cooler.html')
def page_connector_cooler():
    print ('Hello world****')
    return render_template('/pages/connector_cooler.html')

@app.route('/pages/image_classifier.html')
def page_image_classifier():
    print ('Hello world****')
    return render_template('/pages/image_classifier.html')

@app.route('/pages/model.image.proto')
def page_image_proto():
    print ('Hello world****')
    return render_template('/pages/model.image.proto')

@app.route('/pages/model.tag.proto')
def page_image_tag_proto():
    print ('Hello world****')
    return render_template('/pages/model.tag.proto')

@app.route('/pages/vmpredictor-int.html')
def page_vmpredictor():
   # print ('Hello world****')
    return render_template('/pages/vmpredictor-int.html')

@app.route('/classify', methods=['POST']) #GET requests will be blocked
def json_example():
    print("==============request:%s",  request)
    #req_data = request.data
    #print("==============req_data:%s",  req_data)
    
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
    impurity = 'Red Bull'
    for result in of.value:
        #print("#############Image Classification Result=%s",result)
        #list.append(result)
        print("#############Image Classification Result=%s",result)
        types = result.split(':')[1]
        rate = result.split(':')[2][:-1]
        if (types == 'Non Redbull'):
           impurity = 'Non Redbull'
        list.append(rate)
    #return json.dumps(list)

    predicted = min(list)+'%'
    impurity1 = impurity

    print (predicted)
    print(impurity1)

   # json_string = json.dumps({'type': impurity, 'score': predicted})

    #files = glob.glob('/Users/liule/att/lei-connector-cooler/test/*')
    #for f in files:
       #os.remove(f)

    
    data = {}
    data['type'] = impurity1
    data['score'] = predicted 
    json_data = json.dumps(data)

    #shutil.rmtree('/Users/liule/att/lei-connector-cooler/test')
    #os.mkdir('/Users/liule/att/lei-connector-cooler/test')

    return json_data

@app.route('/delete', methods=['POST']) #GET requests will be blocked
def json_delete():
   #shutil.rmtree('/Users/liule/att/lei-connector-cooler/test')
   #os.mkdir('/Users/liule/att/lei-connector-cooler/test')
    files = glob.glob('/Users/liule/att/lei-connector-cooler/test/*')
    for f in files:
       os.remove(f)


    return render_template('/pages/connector_cooler.html') 
    
@app.route('/select', methods=['POST']) #GET requests will be blocked
def json_select():
    print("==============request:%s",  request)
    #req_data = request.data
    #print("==============req_data:%s",  req_data)
    
    req_data = request.get_json()
    print("==============req_data:%s",  req_data)
    
    imageURL = req_data['Image']
   
    print("==============selected image URL:%s",  imageURL)
    
    import urllib.request

    urllib.request.urlretrieve(imageURL, "/Users/liule/att/lei-connector-cooler/test/test.jpg")
    
    data = {}
    data['status'] = 'googd'
    json_data = json.dumps(data)
    return json_data
     

if __name__ == '__main__':
    #app.run(debug=True)
    app.debug = True
    app.run(host='0.0.0.0', port=9000)
