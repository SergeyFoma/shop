# Generated by Django 3.2.25 on 2024-10-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
