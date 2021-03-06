# Generated by Django 3.2.1 on 2021-06-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('article', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
