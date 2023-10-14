# Generated by Django 4.2.5 on 2023-10-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_course_description_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='type',
            field=models.CharField(choices=[('hard', 'Hard skill'), ('soft', 'Soft skill')], default='hard', max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='topics',
            field=models.ManyToManyField(related_name='courses', to='course.topic'),
        ),
    ]