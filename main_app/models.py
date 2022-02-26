from django.db import models
from django.urls import reverse

LOCATION = (
    ('M', 'Museum'),
    ('L', 'Libary'),
    ('S', 'Storage')
)

class Accessories(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Duck(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description =  models.TextField(max_length=250)
    price = models.IntegerField()
    accessories = models.ManyToManyField(Accessories)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'duck_id': self.id})

class Display(models.Model):
    from_date = models.DateField('from date')
    to_date = models.DateField('to date')
    location = models.CharField(max_length=1, choices=LOCATION, default=LOCATION[0][0])
    duck = models.ForeignKey(Duck, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_location_display()} on {self.date}'
