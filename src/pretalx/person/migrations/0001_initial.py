# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 15:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pretalx.common.mixins
import pretalx.person.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("nick", models.CharField(max_length=60, unique=True)),
                ("name", models.CharField(blank=True, max_length=120, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("locale", models.CharField(default="en", max_length=32)),
                ("timezone", models.CharField(default="UTC", max_length=30)),
                ("send_mail", models.BooleanField(default=False)),
                ("pw_reset_token", models.CharField(max_length=160, null=True)),
                ("pw_reset_time", models.DateTimeField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EventPermission",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("is_orga", models.BooleanField(default=True)),
                (
                    "invitation_token",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "invitation_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="permissions",
                        to="event.Event",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="permissions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(pretalx.common.mixins.models.LogMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SpeakerProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("biography", models.TextField(blank=True, null=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="event.Event",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profiles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(pretalx.common.mixins.models.LogMixin, models.Model),
        ),
    ]
