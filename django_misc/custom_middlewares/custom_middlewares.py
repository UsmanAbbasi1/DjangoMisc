class LoggingMiddleWare():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #  Do what you want before view is called
        print('before calling view')
        response = self.get_response(request)
        # Do what you want after view is returned
        print(dir(response))
        print('after calling view')
        return response
