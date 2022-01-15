from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.urls import reverse


class City(models.Model):
  title = models.CharField(max_length=200)
  url = models.TextField()

  class Meta:
    db_table = 'City'
    ordering = ['title']

  def get_url(self):
    return reverse('covidapp:covidreg', args=[self.City.slug])
  def __str__(self):
    return self.title