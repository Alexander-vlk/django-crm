from django.contrib import admin


from auth_service.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'second_name', 'fiz_tin', 'email']
    list_display = [
        'id',
        'get_full_name', 
        'username',
        'email',
        'phone_number',
        'fiz_tin',
        'is_shop_owner',
        'is_supplier',
        'is_staff',
        ]
    list_display_links = ['id', 'get_full_name']
    fieldsets = [
        (
            'ФИО',
            {
                'fields': ['last_name', 'first_name', 'second_name'],
                'description': 'ФИО пользователя',
            }
        ),
        (
            'Контактные данные',
            {
                'fields': ['email', 'phone_number'],
                'description': 'Контактные данные',
            }
        ),
        (
            'Дополнительные сведения',
            {
                'fields': ['fiz_tin', 'is_shop_owner', 'is_supplier'],
                'description': 'Дополнительные сведения',
            }
        ),
        (
            None,
            {
                'fields': ['is_staff', 'is_active', 'date_joined', 'password', 'last_login']
            }
        )
    ]
    readonly_fields = ['password', 'date_joined', 'last_login']
