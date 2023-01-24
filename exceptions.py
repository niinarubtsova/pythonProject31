class BaseError(Exception):
    message = 'Неожиданная ошибка'


class RequestError(BaseError):
    message = 'Произошла ошибка обработки запроса'


class CourierError(BaseError):
    message = 'Произошла ошибка при доставке'


class NotEnoughSpace(CourierError):
    message = 'Недостаточно места на складе'


class NotEnoughProduct(CourierError):
    message = 'Недостаточно товара на складе'


class TooManyDifferentProducts(CourierError):
    message = 'Слишком много разных товаров'


class InvalidRequest(RequestError):
    message = 'Неправильный запрос, попробуй снова'


class InvalidStorageName(RequestError):
    message = 'Выбран несуществующий склад'