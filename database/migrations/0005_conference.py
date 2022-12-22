# Generated by Django 4.1.3 on 2022-12-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_rename_publisther_journal_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('title', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('typeOfPublication', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('publisher', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('isbn', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('yearOfPublication', models.IntegerField(blank=True, default=None, null=True)),
                ('doi', models.CharField(blank=True, default=None, max_length=300, null=True)),
            ],
        ),
    ]