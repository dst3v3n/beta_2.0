# Generated by Django 4.2.7 on 2023-11-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administradores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='password',
            new_name='Password',
        ),
        migrations.AlterField(
            model_name='admin',
            name='Email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
