# Generated by Django 4.1.7 on 2023-10-25 15:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note",
            old_name="sticky_note",
            new_name="notes",
        ),
    ]
