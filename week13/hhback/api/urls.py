# from django.urls import path
# #from api.views.views_CBV import VacancyListAPIView, VacancyDetailAPIView
# from api.views.fbv import company_list, company_one, vacancy_companyID
# from api.views.generic import VacancyListAPIView, VacancyDetailAPIView, CompanyWithVacancies
# from rest_framework_jwt.views import obtain_jwt_token
#
# urlpatterns = [
#     path('login/', obtain_jwt_token),
#     path('companies/', company_list),
#     path('companies/<int:company_id>/', company_one),
#     path('vacancies/', VacancyListAPIView.as_view()),
#     path('companies/<int:company_id>/vacancies/', vacancy_companyID),
#     path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),
#     path('companies/vacancies/', CompanyWithVacancies.as_view()),
#     # path('vacancies/<int:vacancy_id>/', vacancy_details),
#     # path('companies/<int:company_id>/vacancies/', company_vacancy)
# ]

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'vacancies', views.VacancyViewSet)

urlpatterns = [
    url(r'^users/', views.users, name='users'),
    url(r'^login/', obtain_jwt_token),
]

urlpatterns += router.urls

