from django.utils.deprecation import MiddlewareMixin

class ClearSessionMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.path.startswith('/Quiz/'):
            request.session.flush()
        return response
