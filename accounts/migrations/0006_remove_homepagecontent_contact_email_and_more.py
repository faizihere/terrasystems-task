# Generated by Django 5.2 on 2025-04-16 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_homepagecontent_contact_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagecontent',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='cta_button',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='feature_button',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='feature_description',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='feature_title',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='footer_tagline',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='homepagecontent',
            name='title',
        ),
    ]
