#!/usr/bin/python3.2

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post" enctype="multipart/form-data">'
                   '信息:<input type="text" name="message"></input>'
                   '文件:<input type="file" name="pics"></input>'
                   '<input type="submit" value="Submit"></input>'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message") + "\n")
        self.write("You upload :\n")
        for name,files in self.request.files.items():
            self.write("param_name=" + name + "\n")
            for file_info in files:
                self.write("file_info=" + file_info['filename'] + "\n")
                self.write("content_type=" + file_info['content_type'] + "\n")
        #self.write(str(len(self.request.files)) + " " +str(type(self.request.files)))
        
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()