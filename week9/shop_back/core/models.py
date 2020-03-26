from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField(default='')

    def to_json(self):
      return{
        'id':self.id,
        'name':self.name,
        'price':self.price,
        'description':self.description
      }


