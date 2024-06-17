# Generated by Django 4.2.2 on 2023-07-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_course_students_alter_student_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='webapp.course'),
        ),
    ]