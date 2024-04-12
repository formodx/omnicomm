class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # response['Content-Length'] = 10_000
        # response['Content-Type'] = 'text/html; charset=utf-8'

        return response