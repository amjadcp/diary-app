# Generated by Django 4.0.2 on 2022-03-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_diary_body_alter_diary_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]
