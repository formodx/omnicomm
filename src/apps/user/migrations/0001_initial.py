# Generated by Django 5.0.2 on 2024-03-22 16:32

import apps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted at')),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('middle_name', models.CharField(max_length=40, verbose_name='Middle name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=apps.user.models.User.upload_to, verbose_name='Avatar')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
