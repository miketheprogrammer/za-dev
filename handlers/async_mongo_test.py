import asyncmongo
import tornado.web
class Handler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        db = asyncmongo.Client(pool_id='mypool', host='localhost', 
            port=27107, dbname='za')

        db.users.find(callback=self._on_response)

    def _on_response(self, response, error):
        if error:
            raise tornado.web.HTTPError(500)
        self.render('template', first_name=response['first_name'])
