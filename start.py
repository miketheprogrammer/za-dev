import tornado.ioloop
import tornado.web
import models
import events
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class UserHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        print 'hi'
        x = models.User(username=self.request.arguments.get('username')[0])
        if x._id is None:
            x.save()
            print x.fields
        self.finish()

class UserCreationHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        if not 'username' in self.request.arguments:
            self.write("404 Error: Page or Resource Not Found")
        else:
            user = models.User()

        arguments = {}
        for k,v in enumerate(self.request.arguments):
            arguments[v] = self.request.arguments.get(v)[0]
            setattr(user, v, self.request.arguments.get(v)[0])
        user.save()
        #evn = events.Event()
        self.finish()
    def post(self):
        if not 'username' in self.request.arguments:
            self.write("404 Error: Page or Resource Not Found")
        else:
            user = models.User()

        arguments = {}
        for k,v in enumerate(self.request.arguments):
            arguments[v] = self.request.arguments.get(v)[0]
            setattr(user, v, self.request.arguments.get(v)[0])
        user.save()
        self.finish()

class PusherTestChannelHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("""<!DOCTYPE html>
<head>
  <title>Pusher Test</title>
  <script src="http://js.pusher.com/1.12/pusher.min.js" type="text/javascript"></script>
  <script type="text/javascript">
    // Enable pusher logging - don't include this in production
    Pusher.log = function(message) {
      if (window.console && window.console.log) window.console.log(message);
    };

    // Flash fallback logging - don't include this in production
    WEB_SOCKET_DEBUG = true;

    var pusher = new Pusher('0ad923c1f1da378fe30b');
    var channel = pusher.subscribe('test_channel');
    channel.bind('my_event', function(data) {
      console.log(data);
    });
  </script>
</head><body>hello</body></html>""")
        self.finish()

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/get/za", UserHandler),
    (r"/user/create", UserCreationHandler),
    (r"/get/pusher/test_channel", PusherTestChannelHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()