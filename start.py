import tornado.ioloop
import tornado.web
import async_mongo_test
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class FindZaHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        conn = pymongo.Connection('localhost', 27017)
        db = connection.za

        print db.za.find()

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/get/za", FindZaHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()