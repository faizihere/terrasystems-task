# Generated by Django 5.2 on 2025-04-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.TextField()),
                ('cta_text', models.CharField(max_length=100)),
                ('feature_title', models.CharField(max_length=200)),
                ('feature_description', models.TextField()),
                ('feature_button', models.CharField(max_length=100)),
                ('starter_title', models.CharField(max_length=100)),
                ('starter_price', models.CharField(max_length=50)),
                ('starter_features', models.TextField(help_text='Comma-separated list')),
                ('pro_title', models.CharField(max_length=100)),
                ('pro_price', models.CharField(max_length=50)),
                ('pro_features', models.TextField(help_text='Comma-separated list')),
                ('enterprise_title', models.CharField(max_length=100)),
                ('enterprise_price', models.CharField(max_length=50)),
                ('enterprise_features', models.TextField(help_text='Comma-separated list')),
                ('footer_tagline', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=20)),
            ],
        ),
    ]
