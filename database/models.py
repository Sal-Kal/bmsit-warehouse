from django.db import models

# Create your models here.
class journal(models.Model):
    authorName = models.CharField(max_length=500, blank=True, default=None, null=True)
    title = models.CharField(max_length=500, blank=True, default=None, null=True)
    typeOfPublication = models.CharField(max_length=500, blank=True, default=None, null=True)
    publisher = models.CharField(max_length=500, blank=True, default=None, null=True)
    isbn = models.CharField(max_length=500, blank=True, default=None, null=True)
    yearOfPublication = models.IntegerField(blank=True, default=None, null=True)
    doi = models.CharField(max_length=300, blank=True, default=None, null=True)

    def __str__(self) -> str:
        return self.title