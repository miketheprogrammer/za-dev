import pymongo

class BaseModel(object):
    def __init__(self, *args, **kwargs):
        self.fields = self.__dict__.copy()
        del self.fields['fields']
        dbname = 'za' if 'dbname' not in kwargs else kwargs.get('dbname')
        for key in kwargs:
            if key in self.fields:
                setattr(self,key,kwargs.get(key))

        self._connection = pymongo.Connection('localhost', 27017)
        self._db = self._connection['main']
        self._query = {}
        self._db = self._db[dbname]

        for k in kwargs:
            if k in self.fields:
                self._query[k] = kwargs.get(k)

        if self._query:
            self._populate_fields()

    def find(self, query):
        result = db.find(query)

    def __unicode__(self):
        return self.__class__.__name__ + "_unicode"

    def save(self):
        if self._id is None:
            del self.fields['_id']
        result = self._db.save( self.fields, True, True)
        self.fields['_id'] = result
        return True


    def __setattr__(self, name, value):
        if 'fields' not in self.__dict__:
            self.__dict__['fields'] = {}
        if name in self.fields:
            self.fields[name] = value
        self.__dict__[name] = value
        return True if self.__dict__[name] == value else False

    def _populate_fields(self):
        if self._query:
            result = self._db.find(self._query)
            if result.count() > 1:
                obj = self._db.find(self._query)[0]
            else:
                return False
            for k,v in enumerate(obj):
                setattr(self,v,obj[v])
        else:
            return False

class Weapon(BaseModel):
    def __init__(self, *args, **kwargs):
        self._id = None
        self.type = None
        self.range = None
        self.accuracy = None
        self.FireRate = None
        super(self.__class__, self).__init__(dbname='weapons', **kwargs)

class Player(BaseModel):
      def __init__(self, *args, **kwargs):
        self._id = None
        self._user_id
        self._inventory_id

        super(self.__class__, self).__init__(dbname='player', **kwargs)  
class User(BaseModel):
    def __init__(self, *args, **kwargs):
        self._id = None
        self.username = None
        super(self.__class__, self).__init__(dbname='users', **kwargs)

