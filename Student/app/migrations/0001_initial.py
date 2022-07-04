# Generated by Django 3.2.12 on 2022-05-27 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=199)),
                ('gender', models.CharField(choices=[('1', 'male'), ('2', 'female'), ('3', 'gender')], max_length=10)),
                ('course', models.CharField(choices=[('1', 'BCA'), ('2', 'B.Tech'), ('3', 'BSE')], max_length=10)),
                ('current_address', models.TextField(max_length=300)),
                ('marks_te', models.IntegerField()),
                ('percentage_te', models.FloatField()),
                ('passing_year_te', models.IntegerField()),
                ('marks_tw', models.IntegerField()),
                ('percentage_tw', models.FloatField()),
                ('passing_year_tw', models.IntegerField()),
                ('marks_ug', models.IntegerField()),
                ('percentage_ug', models.FloatField()),
                ('passing_year_ug', models.IntegerField()),
                ('marks_m', models.IntegerField()),
                ('percentage_m', models.FloatField()),
                ('passing_year_m', models.IntegerField()),
                ('marksheet_te', models.FileField(upload_to='document/10')),
                ('marksheet_tw', models.FileField(upload_to='document/12')),
                ('marksheet_ug', models.FileField(upload_to='document/UG')),
                ('marksheet_m', models.FileField(upload_to='document/PG')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
