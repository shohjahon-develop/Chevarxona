from django.urls import path
from .views import (BezakRoyxatView,BezaklarDetailAPIView,MatoRoyxatView
                    ,MatoDetailAPIView,MahsulotlarRoyxatView,
                    MahsulotlarDetailAPIView,BezakchiqmDetailAPIView,
                    BezakchqimRoyxatView,BezakkirimRoyxatView,
                    BezakkirmDetailAPIView,MatokrimDetailAPIView,
                    MatokirimRoyxatView,MahsulotkrimRoyxatView,
                    MahsulotkrimDetailAPIView,SotuvRoyxatView,
                    SotuvDetailAPIView,MatochqimRoyxatView,MatochqimDetailAPIView,MatoNewApi)
urlpatterns = [
    path('matonew/<int:pk>',MatoNewApi.as_view()),

    path('bezaklar/',BezakRoyxatView.as_view()),
    path('bezaklar/<int:pk>',BezaklarDetailAPIView.as_view()),

    path('bezakchqim/',BezakchqimRoyxatView.as_view()),
    path('bezakchqim/<int:pk>',BezakchiqmDetailAPIView.as_view()),

    path('bezakkirm/',BezakkirimRoyxatView.as_view()),
    path('bezakkirm/<int:pk>',BezakkirmDetailAPIView.as_view()),

    path('matolar/',MatoRoyxatView.as_view()),
    path('matolar/<int:pk>',MatoDetailAPIView.as_view()),

    path('matokrim/',MatokirimRoyxatView.as_view()),
    path('matokrim/<int:pk>',MatokrimDetailAPIView.as_view()),

    path('matochqim/',MatochqimRoyxatView.as_view()),
    path('matochqim/<int:pk>',MatochqimDetailAPIView.as_view()),

    path('mahsulot/',MahsulotlarRoyxatView.as_view()),
    path('mahsulot/<int:pk>',MahsulotlarDetailAPIView.as_view()),

    path('mahsulotkrim/',MahsulotkrimRoyxatView.as_view()),
    path('mahsulotkrim/<int:pk>',MahsulotkrimDetailAPIView.as_view()),

    path('sotuv/',SotuvRoyxatView.as_view()),
    path('sotuv/<int:pk>',SotuvDetailAPIView.as_view())
    ]