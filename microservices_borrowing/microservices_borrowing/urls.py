from django.contrib import admin
from django.urls import path#, include
from rest_framework.urlpatterns import format_suffix_patterns
from borrowing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('borrowing/', views.borrowing_list),
    path('borrowing/<int:pk>', views.borrowing_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)