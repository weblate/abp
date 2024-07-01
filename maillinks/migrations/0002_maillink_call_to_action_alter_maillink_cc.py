# Generated by Django 4.2.13 on 2024-07-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maillinks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="maillink",
            name="call_to_action",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="maillink",
            name="cc",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]