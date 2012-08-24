import pusher
import json
import customexceptions as ce


### Consider changing exception to ImplentationErrorException
class Event(object):
	def __init__(self, *args, **kwargs):
		pusher.app_id = '26330'
		pusher.key = '0ad923c1f1da378fe30b'
		pusher.secret = '5d4a3aa26a02cee66ef7'
		self.pusher = pusher.Pusher()

		##remove these when not testing
		self.channel = 'test_channel' if 'channel' not in kwargs else kwargs.get('channel')
		self.data = 'hello world from Event' if 'data' not in kwargs else kwargs.get('data')
		self.event = 'my_event' if 'event' not in kwargs else kwargs.get('event')

		if 'channel' not in self.__dict__:
			raise customexceptions.FieldRequiredError('You are missing a required field: <channel>', [])
		if 'data' not in self.__dict__:
			raise customexceptions.FieldRequiredError('You are missing a required field: <data>', [])
		if 'event' not in self.__dict__:
			raise customexceptions.FieldRequiredError('You are missing a required field: <event>', [])

		self._trigger()

	def _trigger(self):
		self.pusher[self.channel].trigger(self.event, {'sada':'asda'})


#### User Events #####
class UserCreatedEvent(Event):
	def __init__(self, *args, **kwargs):
		super(self.__class__, self).__init__(data=kwargs.get('data'), event='za:user:created')


#### World Event ####

class WorldSpawned(Event):
	def __init__(self, *args, **kwargs):
		super(self.__class__, self).__init__(data=kwargs.get('data'), event='za:world:spawned')