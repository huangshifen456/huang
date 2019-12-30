from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    list_filter = ('sex', 'status', 'created_time')
    search_fields = ('name', 'profession')
    list_per_page = 3
    fieldsets = (
        (None, {
         'fields': (
                 'name',
                 ('sex', 'profession'),
                 'email',
                 'qq',
                 'phone',
                 'status',
                 )
         }),
    )
    actions_on_bottom = True
    actions_on_top = False


# admin.site.register(Student, StudentAdmin)