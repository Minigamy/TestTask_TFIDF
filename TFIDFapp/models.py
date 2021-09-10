from django.db import models


class AddFile(models.Model):
    file = models.FileField(upload_to='files/')


class TF(models.Model):
    term = models.CharField(max_length=50)
    tf = models.FloatField()
    doc_number = models.PositiveIntegerField()


class IDF(models.Model):
    term = models.CharField(max_length=50, primary_key=True)
    idf = models.FloatField()
