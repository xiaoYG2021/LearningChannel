# Generated by Django 4.2.3 on 2023-07-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('religion', '0005_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Religion',
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': '事件', 'verbose_name_plural': '事件'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
