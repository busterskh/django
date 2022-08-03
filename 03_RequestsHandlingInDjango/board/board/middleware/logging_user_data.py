import datetime


class LoggingDataMiddleware:
    def __init__(self, get_responce):
        self.get_responce = get_responce

    def __call__(self, request):
        with open('./board/middleware/user_data.txt', 'a', encoding='utf=8') as file:
            info = f'{datetime.datetime.now()}\t{request.META.get("HTTP_HOST")}{request.META.get("PATH_INFO")}\t' \
                   f'{request.META.get("REQUEST_METHOD")}'
            file.write(f'{info}\n')
        return self.get_responce(request)
