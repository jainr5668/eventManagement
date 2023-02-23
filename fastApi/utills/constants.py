import enum
class MetaConstant(type):
    def __getattr__(cls, key):
        try:
            if key in cls:
                return cls[key]
            else:
                raise Exception(f'Invalid Constant: "{key}" is not in "{cls}"')
        except Exception:
            raise Exception(f'Invalid Constant: "{key}" is not in "{cls}"')

    def __setattr__(cls, key, value):
        raise TypeError


class Constants(object, metaclass=MetaConstant):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError

class DatabaseQueryStringSelect(Constants):
    pass


class DatabaseTableCreationQueries(enum.Enum):
    pass