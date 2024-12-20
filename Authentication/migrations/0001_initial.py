# Generated by Django 3.2.18 on 2024-12-08 10:17

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('profile_img', models.ImageField(blank=True, default='/patient/account.png', null=True, upload_to='patient')),
                ('birth_date', models.DateField(null=True)),
                ('Organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Clinic', to='Authentication.organization')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('group_name', models.CharField(max_length=100)),
                ('Organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='Authentication.organization')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(blank=True, default='User', max_length=100)),
                ('profile_img', models.ImageField(default='/Admins/doctor.jpg', upload_to='Admins')),
                ('bio', models.CharField(blank=True, default='User Here', max_length=100)),
                ('SpecialInformation', models.TextField(blank=True, null=True)),
                ('GraduationFrom', models.CharField(max_length=100)),
                ('GraduationDate', models.DateField(max_length=100)),
                ('IsDoctor', models.BooleanField(default=0)),
                ('DoctorSpecializations', models.ManyToManyField(blank=True, null=True, related_name='administrators', to='Authentication.DoctorSpecialization')),
                ('Organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='administrators', to='Authentication.organization')),
                ('group_in', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='Authentication.grouppermission')),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
                'permissions': (('AddAdmin', 'Can add admin'),),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
