from django.urls import path
from store.views import UserAPIView, UserListAPIView, ProductCategoryListAPIView, ProductCategoryAPIView, \
    ProductListAPIView, ProductAPIView, BasketItemAPIView, BasketAPIView

urlpatterns = [path("user/", UserAPIView.as_view()),
               path("user/<int:pk>", UserAPIView.as_view()),
               path("users/", UserListAPIView.as_view()),

               path("categories/", ProductCategoryListAPIView.as_view()),
               path("category/", ProductCategoryAPIView.as_view()),
               path("category/<int:pk>", ProductCategoryAPIView.as_view()),

               path("products/", ProductListAPIView.as_view()),
               path("product/", ProductAPIView.as_view()),
               path("product/<int:pk>", ProductAPIView.as_view()),

               path("basket/<int:user>", BasketAPIView.as_view()),
               path("basket/item/", BasketItemAPIView.as_view()),
               path("basket/item/<int:pk>", BasketItemAPIView.as_view()),
               ]
