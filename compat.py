import sys


if sys.version_info < (3,):
    def get_unicode(s):
        return s.decode('UTF-8')

    def set_unicode(s):
        return s.encode('UTF-8')
else:
    def get_unicode(s):
        return s

    def set_unicode(s):
        return s
