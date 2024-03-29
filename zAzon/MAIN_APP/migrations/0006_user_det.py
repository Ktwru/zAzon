# Generated by Django 2.2.4 on 2019-08-26 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MAIN_APP', '0005_delete_user_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, max_length=250, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
