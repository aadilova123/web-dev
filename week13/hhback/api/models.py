from django.db import models

# Create your models here.
class Company(models.Model):
  name = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание', blank=True)
  city = models.CharField(max_length=100, verbose_name='Город')
  address = models.TextField(verbose_name='Адрес', blank=True)

  class Meta:
    verbose_name = 'Компания'
    verbose_name_plural = 'Компании'


class Vacancy(models.Model):
  name = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание', blank=True)
  salary = models.FloatField(verbose_name='Зарплата')
  company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Вакансия'
    verbose_name_plural = 'Вакансии'
#
# class Company(models.Model):
#   name = models.CharField(max_length=300)
#   description = models.CharField(max_length=300)
#   city = models.CharField(max_length=250)
#   address = models.CharField(max_length=300)
#
#   def to_json(self):
#     return {
#       'id': self.id,
#       'name': self.name,
#       'description': self.description,
#       'city': self.city,
#       'address': self.address
#     }
#
#
# class Vacancy(models.Model):
#   name = models.CharField(max_length=300)
#   description = models.TextField(default='')
#   salary = models.FloatField()
#   company_id = models.ForeignKey(Company, on_delete=models.CASCADE, default=1, related_name='vacancies')
#
#   def __str__(self):
#     return f'Vacancy id: {self.id}'
#
#   def to_json(self):
#     return {
#       'id': self.id,
#       'name': self.name,
#       'price': self.price,
#       'company_id': self.company_id.to_json()
#     }
#
#   def full(self):
#     return {
#       'id': self.id,
#       'name': self.name,
#       'description': self.description,
#       'salary': self.salary,
#       'company_id': self.company_id
#     }

