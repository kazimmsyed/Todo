# Generated by Django 4.2.11 on 2024-05-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0006_alter_todo_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
    ]