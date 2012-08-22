import tornado.ioloop
import tornado.web
import models
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class UserHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        x = models.User(username=self.request.arguments.get('username')[0])
        if x._id is None:
            x.save()
            print x.fields

class UserCreationHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        arguments = self.request.arguments.copy()
        if not 'username' in arguments:
            self.write("404 Error: Page or Resource Not Found")
        else:
            za = models.BaseModel('za')
            za.find('')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/get/za", UserHandler),
    (r"/user/create", UserCreationHandler)
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()