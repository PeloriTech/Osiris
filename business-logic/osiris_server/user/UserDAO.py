from django.contrib.auth.models import User


class UserDAO:

    def __init__(self, id: str, username: str, email: str, first_name: str, last_name: str, password: str,
                 groups, is_active: str, is_super_user: bool, last_login: str):
        self.id = id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.groups = groups
        self.is_active = is_active
        self.is_super_user = is_super_user
        self.last_login = last_login

    @staticmethod
    def model_to_dao(model: User):
        dao = UserDAO(
            id=model.id,
            username=model.username,
            email=model.email,
            first_name=model.first_name,
            password='',
            groups=[],
            last_name=model.last_name,
            is_active=model.is_active,
            is_super_user=model.is_superuser,
            last_login=str(model.last_login)
        )
        return dao

    @staticmethod
    def dao_to_model(dao):
        pass

    def dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "is_super_user": self.is_super_user,
            "last_login": self.last_login
        }
