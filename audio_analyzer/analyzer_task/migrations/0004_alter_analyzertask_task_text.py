# Generated by Django 5.1.2 on 2024-10-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer_task', '0003_alter_analyzertask_task_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzertask',
            name='task_text',
            field=models.TextField(),
        ),
    ]