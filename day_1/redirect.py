#!/usr/bin/python3.2

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('http://wendal.net', permanent=True)

    def post(self):
        self.redirect('http://nutzam.com', permanent=True)
        
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()