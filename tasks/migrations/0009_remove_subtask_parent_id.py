# Generated by Django 4.2.11 on 2024-05-02 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0008_alter_subtask_subtask_desc_alter_user_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subtask",
            name="parent_id",
        ),
    ]
