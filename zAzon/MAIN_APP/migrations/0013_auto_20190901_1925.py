# Generated by Django 2.2.4 on 2019-09-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN_APP', '0012_auto_20190901_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_det',
            name='pic',
            field=models.ImageField(default='users/default.jpg', upload_to='users'),
        ),
    ]
