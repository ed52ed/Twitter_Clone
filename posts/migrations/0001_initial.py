# Generated by Django 4.0.3 on 2022-04-06 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Name')),
                ('body', models.CharField(db_index=True, max_length=140, verbose_name='body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
