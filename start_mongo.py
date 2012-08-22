import pymongo
import tornado.web

class Handler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        conn = pymongo.Connection('localhost', 27017)
        db = connection.za

        print db.za.find()
