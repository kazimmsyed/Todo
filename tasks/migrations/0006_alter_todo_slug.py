# Generated by Django 4.2.11 on 2024-05-02 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_alter_subtask_subtask_desc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="slug",
            field=models.SlugField(blank=True, default="", editable=False),
        ),
    ]
