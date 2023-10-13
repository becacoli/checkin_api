from django.urls import path
from .views import UserList, UserDetail, ClassroomList, ClassroomDetail, FrequencyList, FrequencyDetail, UserClassroomList, LoginView
urlpatterns = [
  path('user/', UserList.as_view()),
  path('user/<int:id>', UserDetail.as_view()),
  path('classroom/', ClassroomList.as_view()),
  path('classroom/<int:id>', ClassroomDetail.as_view()),
  path('frequency/', FrequencyList.as_view()),
  path('frequency/<int:id>', FrequencyDetail.as_view()),
  path('user_classroom/', UserClassroomList.as_view()),
  path('login/', LoginView.as_view())
]