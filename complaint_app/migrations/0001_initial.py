# Generated by Django 4.1.7 on 2023-03-28 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=288)),
                ('description', models.TextField(max_length=1024)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Work in Progress', 'Work in Progress'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('solved_by', models.CharField(blank=True, max_length=128, null=True)),
                ('solved_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address1', models.CharField(max_length=400)),
                ('address2', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=20)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_pic')),
                ('user_type', models.CharField(choices=[('Customer', 'Customer'), ('Agent', 'Agent')], default='Customer', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='complaint_doc')),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint_app.complaint')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actions', models.TextField(max_length=1024)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint_app.complaint')),
            ],
        ),
    ]
