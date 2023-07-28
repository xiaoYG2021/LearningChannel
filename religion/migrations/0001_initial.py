# Generated by Django 4.2.3 on 2023-07-27 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archbishop',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('introduction', models.TextField()),
            ],
            options={
                'verbose_name': '历届教主',
                'verbose_name_plural': '历届教主',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('introduction', models.TextField()),
            ],
            options={
                'verbose_name': '老教分部',
                'verbose_name_plural': '老教分部',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': '历程',
                'verbose_name_plural': '历程',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('effective', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '令牌',
                'verbose_name_plural': '令牌',
            },
        ),
    ]