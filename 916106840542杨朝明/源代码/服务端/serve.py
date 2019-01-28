#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spyne import Application
from spyne import rpc
from spyne import ServiceBase
from spyne import Iterable, Integer, Unicode, String, DateTime, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from datetime import datetime, timedelta
from tool import dinner


data = dinner()

class DinnerService(ServiceBase):

    @rpc(DateTime,_returns=String)
    def query_date(self, query_time):
        rax = data.get_table(query_time)
        if rax != -1:
            return str(rax)
        else:
            return 'not the time'

    @rpc(DateTime,Integer,_returns=String)
    def query_num(self, book_date, book_num):
        rest = data.query_rest(book_date)
        if rest >= book_num:
            return 'ok:'+str(rest)
        else: 
            return 'no'

    @rpc(DateTime,Integer,String,_returns=String)
    def submit_order(self, book_date, book_num, phone_num):
        if not data.check_phone(phone_num):
            return 'phone num invalid'

        rax = data.get_table(book_date)
        if rax == -1:
            return "not the time"

        rest = data.query_rest(book_date)
        if rest < book_num:
            return 'no'
        rax = data.query_by_phone(phone_num)
        if rax == None:
            data.add_ord(book_date, book_num, phone_num)
            return 'book success'
        
        
    @rpc(String,_returns=String)
    def query_order(self, phone_num):
        if not data.check_phone(phone_num): 
            return 'phone num invalid'
        ret = data.query_by_phone(phone_num)
        return str(ret)

    @rpc(String,_returns=String)
    def delete_by_phone(self, phone_num):
        if not data.check_phone(phone_num): 
            return 'phone num invalid'
        ret = data.query_by_phone(phone_num)
        if ret != None:
            res = data.delete_by_phone(ret['phone'])
            if 'success' in res:
                return 'success'
        return 'failed'


 
soap_app = Application([DinnerService], 'spyne.examples.hello.soap',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())
 
wsgi_app = WsgiApplication(soap_app)
 
if __name__ == '__main__':
    import logging
 
    from wsgiref.simple_server import make_server
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
 
    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")
 
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()
    
