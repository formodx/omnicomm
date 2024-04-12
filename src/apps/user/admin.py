from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            kwargs['exclude'] = kwargs.get('exclude', tuple()) + ('password',)

        return super().get_form(request, obj=obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(obj.password)

        super().save_model(request, obj, form, change)