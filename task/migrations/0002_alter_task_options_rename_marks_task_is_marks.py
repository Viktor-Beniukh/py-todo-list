# Generated by Django 4.1.4 on 2022-12-20 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_marks", "-created_time"]},
        ),
        migrations.RenameField(
            model_name="task",
            old_name="marks",
            new_name="is_marks",
        ),
    ]
