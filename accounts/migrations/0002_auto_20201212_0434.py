# Generated by Django 3.1.4 on 2020-12-12 04:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='username',
        ),
        migrations.AddField(
            model_name='newuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='about'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
