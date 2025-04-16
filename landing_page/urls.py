from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/homepage/', views.manage_homepage, name='manage_homepage'),
    path('dashboard/edit-pricing/', views.pricing_plans, name='pricing_plans'),
    path('dashboard/pricing/edit/<int:pk>/', views.edit_plan, name='edit_plan'),
    path('dashboard/pricing/delete/<int:pk>/', views.delete_plan, name='delete_plan'),
]
