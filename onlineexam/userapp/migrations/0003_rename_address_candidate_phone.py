# Generated by Django 4.0.3 on 2022-05-24 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_candidate_email_alter_candidate_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='address',
            new_name='phone',
        ),
    ]
