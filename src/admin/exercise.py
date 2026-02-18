from sqladmin import ModelView

from models import Exercise, Category


class CategoryAdmin(ModelView, model=Category):
    pass


class ExerciseAdmin(ModelView, model=Exercise):
    pass
