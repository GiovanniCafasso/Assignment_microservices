# Generated by Django 3.2.10 on 2021-12-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.IntegerField(default='', primary_key=True, serialize=False)),
                ('id_book', models.IntegerField()),
                ('id_customer', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
