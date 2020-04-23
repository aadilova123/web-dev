from django.urls import path, re_path

from api.views.cbv import CompanyDetailAPIView, VacancyDetailAPIView

from rest_framework_jwt.views import obtain_jwt_token

from api.views.fbv import company_list, vacancy_list, comp_vacancies, top_ten

urlpatterns = [
    path('login/',obtain_jwt_token),
    path(r'companies/',company_list),
    path(r'companies/<int:id>/',CompanyDetailAPIView.as_view()),
    path(r'vacancies',vacancy_list),
    path(r'vacancies/<int:id>/',VacancyDetailAPIView.as_view()),
    path(r'companies/<int:id>/vacancies/',comp_vacancies),
    path(r'vacancies/top_ten/',top_ten)
]

