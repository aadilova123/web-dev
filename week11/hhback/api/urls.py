from django.urls import path

from api.views import company_detail, company_list, vacancy_bycompany, vacancy_detail,vacancy_list,top10_vacancy

urlpatterns = [
  path('api/companies' , company_list),
  path('api/companies/<int:id>', company_detail),
  path('api/companies/<int:id>/vacancies/' , vacancy_bycompany),
  path('api/vacancies/', vacancy_list),
  path('api/vacancies/<int:id>', vacancy_detail),
  path('api/vacancies/top_ten/',top10_vacancy)
]
