from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'directors', DirectorViewSet, basename='director_list'),
router.register(r'genre', GenreViewSet, basename='genre_list'),
router.register(r'rating', RatingViewSet, basename='rating_list'),
router.register(r'history', HistoryViewSet, basename='history_list'),
router.register(r'favorite', FavoriteViewSet, basename='favorite_list'),


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('users/', ProfileListAPIView.as_view(), name='user_detail'),
    path('users/<int:pk>', ProfileEditAPIView.as_view(), name='user_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor _detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]