# Generated by Django 1.11.29 on 2020-04-10 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0040_page_draft_title"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="BibliographyItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ordering",
                    models.PositiveIntegerField(
                        help_text="The bibliography items on each referring page are sorted and numbered with this ordering number."
                    ),
                ),
                (
                    "content_key",
                    models.CharField(
                        help_text='The "key" with which this item was created, eg. "rfc" in [[rfc:3514]].',
                        max_length=127,
                    ),
                ),
                (
                    "content_identifier",
                    models.CharField(
                        help_text='The "value" with which this item was created, eg. "3514" in [[rfc:3514]].',
                        max_length=127,
                    ),
                ),
                ("content_long_title", models.CharField(blank=True, max_length=127)),
                (
                    "content_title",
                    models.CharField(
                        help_text='The link title for this item, eg. "RFC 7168" for [[rfc:7168]].',
                        max_length=127,
                    ),
                ),
                ("object_id", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        help_text="The page that this item links to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bibliography_items",
                        to="wagtailcore.Page",
                    ),
                ),
            ],
        ),
    ]
