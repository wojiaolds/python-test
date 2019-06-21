
class Chain(object):

    def __init__(self, path=''):
        self._path = path


    def __getattr__(self, path):

        return Chain('%s/%s' % (self._path, path))

    def __call__(self, *args, **kwargs):

        if len(args) == 0 or args == None or args[0] == '':
            return Chain('%s' % (self._path))
        return Chain('%s/%s' % (self._path, args[0]))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user('lds').timeline.list)