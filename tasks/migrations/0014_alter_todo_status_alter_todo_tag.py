# Generated by Django 4.2.11 on 2024-05-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0013_alter_todo_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Incomplete"), (1, "Completed")], default=""
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="tag",
            field=models.CharField(
                choices=[
                    ("0", ""),
                    ("health", "Health"),
                    ("study", "Study"),
                    ("fitness", "Fitness"),
                    ("errands", "Errands"),
                    ("mental_health", "Mental Health"),
                    ("academic", "Academic"),
                    ("professional", "Professional"),
                ],
                default="health",
                max_length=20,
            ),
        ),
    ]
