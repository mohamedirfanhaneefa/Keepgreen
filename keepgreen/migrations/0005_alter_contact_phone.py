# Generated by Django 5.0 on 2023-12-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keepgreen', '0004_alter_contact_fname_alter_contact_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
    ]
