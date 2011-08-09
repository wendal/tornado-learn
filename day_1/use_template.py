#!/usr/bin/python3.2

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["China", "GuangDong", "GuangZhou"]
        self.render("index.tpl", title="Wendal X!", items=items)
        
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()