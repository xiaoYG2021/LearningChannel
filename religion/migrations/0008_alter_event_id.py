# Generated by Django 4.2.3 on 2023-07-28 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religion', '0007_alter_event_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
