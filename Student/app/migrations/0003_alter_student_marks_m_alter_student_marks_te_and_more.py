# Generated by Django 4.0.4 on 2022-05-30 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220529_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='marks_m',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='marks_te',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='marks_tw',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='marks_ug',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='passing_year_m',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='passing_year_te',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='passing_year_tw',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='passing_year_ug',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='percentage_m',
            field=models.FloatField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='percentage_te',
            field=models.FloatField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='percentage_tw',
            field=models.FloatField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='percentage_ug',
            field=models.FloatField(default=False),
        ),
    ]
