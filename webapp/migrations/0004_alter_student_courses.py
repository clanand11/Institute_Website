# Generated by Django 4.2.2 on 2023-07-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_student_courses_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='webapp.course'),
        ),
    ]
