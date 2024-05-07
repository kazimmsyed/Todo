# Generated by Django 4.2.11 on 2024-05-03 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0012_alter_todo_status_alter_todo_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="user",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks.user",
            ),
        ),
    ]
