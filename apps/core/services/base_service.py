from django.db import DatabaseError
from rest_framework.exceptions import NotFound, ValidationError, APIException

class ServiceBase(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                attrs[attr_name] = ServiceBaseDecorator(attr_value)
        return super().__new__(cls, name, bases, attrs)

def ServiceBaseDecorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFound as e:
            raise e
        except ValidationError as e:
            raise e
        except DatabaseError as e:
            raise APIException(f'Erro no banco de dados. {str(e)}') from e
        except Exception as e:
            raise APIException(f'Erro inesperado. {str(e)}') from e
        
    return wrapper