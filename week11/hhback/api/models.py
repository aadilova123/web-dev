from django.db import models

#
# class Company(models.Model):
#   name = models.CharField(max_length=100, verbose_name='Название')
#   description = models.TextField(verbose_name='Описание', blank=True, null=True)
#   city = models.CharField(max_length=100, verbose_name='Город')
#   address = models.TextField(verbose_name='Адрес', blank=True, null=True)
#
#   class Meta:
#     verbose_name = 'Компания'
#     verbose_name_plural = 'Компании'
#
#
# class Vacancy(models.Model):
#   name = models.CharField(max_length=100, verbose_name='Название')
#   description = models.TextField(verbose_name='Описание', blank=True, null=True)
#   salary = models.FloatField(verbose_name='Зарплата')
#   company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)
#
#   class Meta:
#     verbose_name = 'Вакансия'
#     verbose_name_plural = 'Вакансии'
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
