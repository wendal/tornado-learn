#!/usr/bin/python3.2

import tornado.ioloop
import tornado.web
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This Main Page, Time now=" + str(time.time()))
        
class BlogHandler(tornado.web.RequestHandler):
    def get(self,blog_id):
        self.write("This is my blog , id="+blog_id)
        
    def post(self,blog_id):
        self.write('Great!! you own it !! Id = '+ blog_id)
        
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/blog/([0-9]+)", BlogHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()