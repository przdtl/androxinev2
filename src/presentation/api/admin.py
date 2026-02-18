from sqladmin import Admin

from db.base import engine
from config import settings

from admin import (
    UserAdmin,
    ExerciseAdmin,
    WorkoutTemplateAdmin,
    SetAdmin,
    CategoryAdmin,
)

from .app import app

admin = Admin(app, engine)


admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(ExerciseAdmin)
admin.add_view(WorkoutTemplateAdmin)
admin.add_view(SetAdmin)
