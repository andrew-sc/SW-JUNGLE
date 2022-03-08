from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.swjungle

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/#', methods=['GET'])
def listing():
    articles = list(db.aticles.find({}, {'_id': False}))
    return jsonify({'all_aticles':articles})

@app.route('/#', methods=['POST'])
def saving():
    title_recive = request.form['title_give']
    content_recive = request.form['content_give']

    doc = {
        'title': title_recive,
        'content': content_recive
    }
    db.aticles.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route('/#', methods=['PUT'])
def editing():
    new-title_recive = request.form['new-title_give']
    new-text_recive = request.form['new-text_give']

  return jsonify({'msg':'수정 완료!'})

@app.route('/#', methods=['DELET'])
def deleting():

  return jsonify({'msg':'삭제 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)