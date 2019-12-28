from schema import And, Optional


class UserViewSchemas:

    register_user = {
        "username": And(str),
        "password": And(str),
        "email": And(str),
        "first_name": And(str),
        "last_name": And(str)
    }

    login = {
        "username": And(str),
        "password": And(str)
    }

    update_user_info = {
        Optional("username"): And(str),
        Optional("password"): And(str),
        Optional("email"): And(str),
        Optional("first_name"): And(str),
        Optional("last_name"): And(str)
    }