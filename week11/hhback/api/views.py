from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from api.models import Company,Vacancy


def company_list(request):
  companies = Company.objects.all()
  companies_json = [company.to_json() for company in companies]
  return JsonResponse(companies_json, safe=False)


def company_detail(request, id):
  try:
    company = Company.objects.get(id=id)
  except Company.DoesNotExist as e:
    return JsonResponse({'error':str(e)})
  return JsonResponse(company.to_json())


def vacancy_list(request):
  vacancies = Vacancy.objects.all()
  vacancies_json = [vacancy.to_json() for vacancy in vacancies]
  return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, id):
  try:
    vacancy = Vacancy.objects.get(id=id)
  except Vacancy.DoesNotExist as e:
    return JsonResponse({'error':str(e)})
  return JsonResponse(vacancy.to_json())


def vacancy_bycompany(request, id):
  vacancies = Vacancy.objects.filter(company_id=id)
  vacancies_json = [vacancy.to_json() for vacancy in vacancies]
  return JsonResponse(vacancies_json, safe=False)

#List of top 10 vacancies sorted by
# decreasing salary

def top10_vacancy(request):
  vacancies = Vacancy.objects.order_by('-salary')[:10]
  vacancies_json = [vacancy.to_json() for vacancy in vacancies]
  return JsonResponse(vacancies_json, safe=False)
