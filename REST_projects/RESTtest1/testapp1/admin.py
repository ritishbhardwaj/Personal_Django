from django.contrib import admin
from .models import Student
# Register your models here.


# admin.site.register(Student)   ''' This syntax is used to register all the attributes of the model in admin panel '''

@admin.register(Student)         #   this syntax is used to register only the selected fields into the admin panel
class  StudentAdmin(admin.ModelAdmin):
    list_display=["name","roll","city"]        # this list_display is the naming convention so it is as it is
    
      