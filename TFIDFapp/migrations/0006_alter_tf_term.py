# Generated by Django 3.2.7 on 2021-09-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFIDFapp', '0005_alter_tf_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tf',
            name='term',
            field=models.CharField(max_length=50),
        ),
    ]
