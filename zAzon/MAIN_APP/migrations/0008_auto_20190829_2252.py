# Generated by Django 2.2.4 on 2019-08-29 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN_APP', '0007_auto_20190826_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='thread_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='thread_pic',
            new_name='pic',
        ),
    ]