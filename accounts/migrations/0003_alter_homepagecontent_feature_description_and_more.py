# Generated by Django 5.2 on 2025-04-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_pricingplan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecontent',
            name='feature_description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='footer_tagline',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='homepagecontent',
            name='subtitle',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pricingplan',
            name='features',
            field=models.CharField(max_length=500),
        ),
    ]
