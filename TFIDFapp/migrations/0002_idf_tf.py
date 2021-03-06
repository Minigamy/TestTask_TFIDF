# Generated by Django 3.2.7 on 2021-09-05 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TFIDFapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=50)),
                ('tf', models.FloatField()),
                ('doc_number', models.PositiveIntegerField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='IDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idf', models.FloatField()),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TFIDFapp.tf', unique=True)),
            ],
        ),
    ]
