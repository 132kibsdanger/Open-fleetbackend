# Generated by Django 4.1.7 on 2023-05-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(db_column='password', max_length=256),
        ),
    ]
