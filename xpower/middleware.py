from django import get_version
from django.conf import settings


HEADER = getattr(settings, 'X_POWERED_BY', 'Django/%(version)s') % {'version': get_version()}

class XPoweredByMiddleware(object):
    def process_response(self, request, response):
        response['X-Powered-By'] = HEADER
        return response