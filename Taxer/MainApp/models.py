from django.db import models

class MainApp(models.Model):
    CustomerName = models.CharField(max_length =500)
    CustomerPAN = models.CharField(max_length = 10)
    Organization = models.CharField(max_length = 200)
    Contact = models.IntegerField(null = True)
    UploadedDate = models.DateField()
    Status = models.CharField(max_length = 200)
    UploadedDocuments = models.CharField(max_length =500)
