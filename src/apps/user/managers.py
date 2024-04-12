from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('The email must be set')

        kwargs['is_staff'] = True
        kwargs['is_active'] = True

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, *args, **kwargs):
        kwargs['is_superuser'] = True

        return self.create_user(*args, **kwargs)