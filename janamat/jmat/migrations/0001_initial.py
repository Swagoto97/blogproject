# Generated by Django 2.2 on 2020-06-01 14:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chellenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chellengeName', models.CharField(max_length=50)),
                ('chellengeDesc', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Chellenge',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='userAdmin/ProfileImage')),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.DateTimeField(auto_now=True)),
                ('usr_type', models.IntegerField(choices=[(1, 'Admin'), (2, 'User')], default=2)),
                ('usr_ip', models.GenericIPAddressField()),
                ('user_browser', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
            options={
                'db_table': 'UserProfile',
            },
        ),
        migrations.CreateModel(
            name='TopicList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=50)),
                ('TopicDesc', models.TextField(blank=True, max_length=1000, null=True)),
                ('Chellenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmat.Chellenge')),
            ],
            options={
                'db_table': 'TopicList',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_comment', models.DateTimeField(default=datetime.datetime.today)),
                ('message', models.TextField(verbose_name='Message Field')),
                ('chellenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jmat.Chellenge')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]
