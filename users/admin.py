"""User admin classes"""

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Models
from django.contrib.auth.models import User
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile of user 
    """

    #mostrar campos
    list_display = ('user','phone_number','website','picture')
    
    #mostrar campos con link
    list_display_links = ('user',)

    #editar campos
    list_editable  = ('phone_number','website','picture')

    #campo de busqueda
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    # campos para filtrar
    list_filter = (
        'created',
        'modified',
        'user__is_staff'
    )

    fieldsets = (
        ('Profile', {
            "fields": (
                ('user', 'picture'),
            ),
        }),
        ('Extra info', {
            "fields": (
                ('website','phone_number'),
                ('biography'),
            ),
        }),
        ('Metadata',{
                "fields": (
                    ('created','modified'),
            ),
        })
    )
    readonly_fields = ('created','modified')



class ProfileInLine(admin.StackedInline):
    """
    Profile in-line admin for users.
    """
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """
    Add profile admin to baseuseradmin
    """

    inlines = (ProfileInLine,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)