from sqladmin import ModelView

from models import Set


class SetAdmin(ModelView, model=Set):
    pass
