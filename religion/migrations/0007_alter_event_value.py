# Generated by Django 4.2.3 on 2023-07-28 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religion', '0006_delete_religion_alter_event_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='value',
            field=models.FloatField(),
        ),
    ]