from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _



@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('photo', 'bio',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Degree)
admin.site.register(Discount)
admin.site.register(More)
admin.site.register(Our_services)
admin.site.register(Phone)
admin.site.register(Search_course)
admin.site.register(Thought)
admin.site.register(Upcoming_events)
admin.site.register(Course)
admin.site.register(News)
admin.site.register(Contact)
admin.site.register(Comment)



