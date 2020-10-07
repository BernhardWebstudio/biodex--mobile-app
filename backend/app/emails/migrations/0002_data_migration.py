# Generated by Django 3.0.2 on 2020-01-23 14:16

from django.db import migrations


def populate_db(apps, schema_editor):
    # Email Types
    email_types = [
        {
            "key": "registration_email",
            "subject": "You have been invited to join BioDex!",
            "title": "You have been invited to join BioDex!",
            "template": "{{ value|linebreaks }}Welcome to BioDex The species identification tool for Taxonomists and Natural History Collections. See {{ 'biodex.ethz.ch'|urlize }} for more info or to get in contact.{{ value|linebreaks }}If you don't have the app yet, download it via App store and create a new account. You will need following validation code to register: {{code}}"
        },
        {
            "key": "password_reset_email",
            "subject": "Password reset",
            "title": "Password reset",
            "template": "{{ value|linebreaks }}This is the code to reset your password: {{code}}"
        },
    ]
    EmailType = apps.get_model('emails', 'EmailType')
    for email_type in email_types:
        EmailType(**email_type).save()


class Migration(migrations.Migration):
    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]
