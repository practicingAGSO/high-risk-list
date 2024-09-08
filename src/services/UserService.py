from src.models.UserModel import User
from src.database.db_sql_server import ItemDatabase
from flask_jwt_extended import create_access_token

class UserService:
    def register(self, username, password):
        user = User(username=username, password=password)
        user_id = ItemDatabase().add_user(user)
        user.id = user_id
        return user

    def login(self, username, password):
        user = ItemDatabase().get_user_by_username(username)
        if user and user.password == password:
            access_token = create_access_token(identity=user.id)
            return {"jwt": access_token}
        else:
            return None