from django.urls import path
from api_app.views import *

urlpatterns = [
    path('Student-Create-List/',StudentCreateListApi.as_view(),name='Student_Create_List'),
    path('Student-Details-Api/<int:pk>/',StudentDetailsApi.as_view(),name='Student_Details_Api'),
]

