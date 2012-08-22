import tornado.ioloop
import tornado.web
import pymongo
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class FindZaHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        conn = pymongo.Connection('localhost', 27017)
        db = conn.za

        results = db.za.find()
        print results
        print results[0]
        for result in results:
            print result
            self.write(result['username'])
        self.finish()
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/get/za", FindZaHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
