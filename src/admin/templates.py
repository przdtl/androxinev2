from sqladmin import ModelView

from models import WorkoutTemplate


class WorkoutTemplateAdmin(ModelView, model=WorkoutTemplate):
    pass
