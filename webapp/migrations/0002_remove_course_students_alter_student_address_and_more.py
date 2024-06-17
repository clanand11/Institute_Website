# Generated by Django 4.2.2 on 2023-07-02 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AlterField(
            model_name='student',
            name='mailid',
            field=models.EmailField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.course'),
        ),
    ]