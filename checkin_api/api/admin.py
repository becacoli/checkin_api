from django.contrib import admin
from .models import User, Classroom, UserClassroom, Frequency

# Register your models here.
admin.site.register(User)
admin.site.register(Classroom)
admin.site.register(UserClassroom)
admin.site.register(Frequency)