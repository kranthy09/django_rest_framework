from django.urls import path


from .views import dummy_view

urlpatterns = [
    path('dummy_view/v1/', dummy_view)
]