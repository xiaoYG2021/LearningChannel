# Generated by Django 4.2.3 on 2023-07-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religion', '0004_religion_delete_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': '历程',
                'verbose_name_plural': '历程',
            },
        ),
    ]
