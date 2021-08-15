# Generated by Django 3.1.4 on 2021-06-24 17:27

from django.db import migrations


def update_question_required(apps, schema_editor):
    Question = apps.get_model("submission", "Question")
    Question.objects.filter(required=True).update(question_required="required")


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0057_question_required_freeze"),
    ]

    operations = [
        migrations.RunPython(update_question_required, migrations.RunPython.noop)
    ]
