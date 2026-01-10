from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add/', views.add_expense, name="add_expense"),
    path('edit/<int:id>/', views.edit_expense, name="edit_expense"),
    path('delete/<int:id>/', views.delete_expense, name="delete_expense"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path("reports/", views.reports_page, name="reports"),
    path("reports/pdf/", views.download_pdf_report, name="download_pdf"),
    path("reports/excel/", views.download_excel_report, name="download_excel"),
    path("reports/csv/", views.download_csv_report, name="download_csv"),
    path("reports/pdf/", views.download_pdf_report, name="download_pdf"),
    path("reports/excel/", views.download_excel_report, name="download_excel"),
    path("profile/", views.profile_page, name="profile"),
    path("change-password/", views.change_password, name="change_password"),
    path("backup/", views.backup_page, name="backup"),
    path("backup/download/", views.download_backup, name="download_backup"),
    path("backup/restore/", views.restore_backup, name="restore_backup"),

]