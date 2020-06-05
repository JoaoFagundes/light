from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='User')
router.register(r'salaries', views.SalaryViewSet, basename='Salary')
router.register(r'statistics', views.StatisticViewSet, basename='Statistic')
