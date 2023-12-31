# Generated by Django 4.2.5 on 2023-10-14 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_topic_type_alter_course_topics'),
        ('estimator', '0005_respondentanswer_respondent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respondentanswer',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respondent_answers', to='course.topic'),
        ),
    ]
