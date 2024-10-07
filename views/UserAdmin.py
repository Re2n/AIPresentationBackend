from sqladmin import ModelView

from schemas.Action import Action
from schemas.User import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.senderId]


class ActionAdmin(ModelView, model=Action):
    column_list = [Action.id, Action.senderId, Action.actionStart]
