from django.db import models

# Create your models here.


class Company(models.Model):
  name = models.CharField(max_length=300)
  description = models.TextField(default='Default')
  city = models.CharField(max_length=300)
  address = models.TextField(default='Baker Street 221B')

  def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'city': self.city,
      'address': self.address
    }


class Vacancy(models.Model):
  name = models.CharField(max_length=300)
  description = models.TextField(default='')
  salary= models.FloatField()
  company = models.ForeignKey(Company, on_delete=models.CASCADE)

  def to_json(self):
    return {
      'id':self.id,
      'name': self.name,
      'salary': self.salary,
      'description': self.description,
      'company': self.company.id
    }
