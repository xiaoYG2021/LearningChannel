# Generated by Django 4.2.3 on 2023-07-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religion', '0003_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
    ]
