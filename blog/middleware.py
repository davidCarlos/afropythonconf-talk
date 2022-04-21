from blog.helper import DollarHelper


class DollarMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.dollar_today = DollarHelper.get_dollar_today()
        response = self.get_response(request)
        return response
