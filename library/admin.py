from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExampleModel, OsfaUser, OsfaDepartment

#    Extend UserAdmin
class OsfaUserAdmin(UserAdmin):
     fieldsets = (
          *UserAdmin.fieldsets,
          (
               'Custom Fields', {'fields': ('department',)}
          ),
     )
     
     add_fieldsets = (
          *UserAdmin.add_fieldsets,
          (
               'Custom Fields', {'fields': ('department',)}
          )
     )


#    Register your models here.
admin.site.register(ExampleModel)
admin.site.register(OsfaUser, OsfaUserAdmin)
admin.site.register(OsfaDepartment)
