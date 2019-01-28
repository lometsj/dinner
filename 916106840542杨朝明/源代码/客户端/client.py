
# -*- coding: utf-8 -*-
from suds.client import Client
from datetime import datetime, timedelta

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import send_file

s = Client('http://localhost:8000/?wsdl')

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('datetime')

parser2 = reqparse.RequestParser()
parser2.add_argument('book_num')
parser2.add_argument('datetime')

parser3 = reqparse.RequestParser()
parser3.add_argument('phone_num')

parser4 = reqparse.RequestParser()
parser4.add_argument('datetime')
parser4.add_argument('book_num')
parser4.add_argument('phone_num')





class q_phone(Resource):
    def post(self):
        ret = {}
        args = parser3.parse_args()
        phone_num = str(args['phone_num'])
        ret['ret'] = s.service.query_order(phone_num)
        return ret

class q_date(Resource):
    def post(self):
        ret = {}
        args = parser.parse_args()
        print ("post:" + str(args['datetime']))
        date = datetime.strptime(args['datetime'], '%Y-%m-%d')
        ret['ret'] = s.service.query_date(date)
        return ret

class q_num(Resource):
    def post(self):
        ret = {}
        args = parser2.parse_args()
        print ('!!!!!!!!:' + str(args))
        book_num = int(args['book_num'])
        date = datetime.strptime(args['datetime'], '%Y-%m-%d')
        ret['ret'] = s.service.query_num(date, book_num)
        return ret


class s_order(Resource):
    def post(self):
        ret = {}
        args = parser4.parse_args()
        book_num = int(args['book_num'])
        date = datetime.strptime(args['datetime'], '%Y-%m-%d')
        phone_num = str(args['phone_num'])
        ret['ret'] = s.service.submit_order(date, book_num, phone_num)
        return ret

class d_phone(Resource):
    def post(self):
        ret = {}
        args = parser3.parse_args()
        phone_num = str(args['phone_num'])
        ret['ret'] = s.service.delete_by_phone(phone_num)
        return ret

@app.route('/')#首页
def index():
    return send_file("./index.html")


api.add_resource(q_date, '/query_date')
api.add_resource(q_num, '/query_num')
api.add_resource(q_phone, '/query_order')
api.add_resource(s_order, '/submit_order')
api.add_resource(d_phone, '/delete_by_phone')


app.run(debug=True)
# a = datetime.now()
# a + timedelta(days=1)
# print (s.service.query_date(a))
# print (s.service.query_num(a,3))
# print (s.service.query_order('13700962560'))
# print (s.service.submit_order(a,3,'13700962560'))

