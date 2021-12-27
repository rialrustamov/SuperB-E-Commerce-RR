from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views
from django.db import router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import UserViewSet


router = DefaultRouter()
router.register('products-list', views.ProductViewSet)

product_patterns = [
    # Product Versions Api,
    path('', views.ProductAPIView.as_view(), name='products'),
    path('<int:pk>/', views.ProductAPIView.as_view(), name='prod_detail'),
    path('<product_id>/versions/', views.ProductVersionsAPIView.as_view(), name='product_versions'),
    path('<product_id>/versions/<int:pk>/', views.ProductVersionsAPIView.as_view(), name='product_version_detail'),
]

urlpatterns = [
    # Products Api
    path('products/', include(product_patterns)),
    # path('products/', views.ProductAPIView.as_view(), name='products'),
    # path('products/<int:pk>/', views.ProductAPIView.as_view(), name='product'),
    path('products/<int:pk>/', views.ProductSingleAPIView.as_view(), name='product'),
    path('create-product/', views.ProductCreateAPIView.as_view()),
    path('update-product/<int:pk>/', views.ProductUpdateAPIView.as_view()),
    path('delete-product/<int:pk>/', views.ProductDeleteAPIView.as_view()),
    path('create-user/', views.CreateUserView.as_view()),
    # path('', include(router.urls)), #viewset test ucun,

    # Product Categories Api,
    path('categories/', views.CategoryAPIView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryAPIView.as_view(), name='category'),
    # path('list_category/', views.ListCategoryApiView.as_view(), name='list_category'),
    path('create_category/', views.CreateCategoryApiView.as_view(), name='create_category'),
    path('update_category/<int:pk>/', views.UpdateCategoryApiView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', views.DeleteCategoryApiView.as_view(), name='delete_category'),

    # Blog Categories Api,
    path('blogcategories/', views.BlogCategoryAPIView.as_view(), name='blogcategories'),
    path('blogcategory/<int:pk>/', views.BlogCategoryAPIView.as_view(), name='blogcategory'),
    # path('list_blogcategory/', views.ListBlogCategoryApiView.as_view(), name='list_blogcategory'),
    path('create_blogcategory/', views.CreateBlogCategoryApiView.as_view(), name='create_blogcategory'),
    path('update_blogcategory/<int:pk>/', views.UpdateBlogCategoryApiView.as_view(), name='update_blogcategory'),
    path('delete_blogcategory/<int:pk>/', views.DeleteBlogCategoryApiView.as_view(), name='delete_blogcategory'),

    # Blogs Api,
    path('blogs/', views.BlogAPIView.as_view(), name='blogs'),
    path('blog/<int:pk>/', views.BlogAPIView.as_view(), name='blog'),
    # path('list_blog/', views.ListBlogAPIView.as_view(), name='list_blog'),
    path('create_blog/', views.CreateBlogAPIView.as_view(), name='create_blog'),
    path('update_blog/<int:pk>/', views.UpdateBlogAPIView.as_view(), name='update_blog'),
    path('delete_blog/<int:pk>/', views.DeleteBlogAPIView.as_view(), name='delete_blog'),

    # Login Api,
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('card/', views.CardView.as_view(), name='card'), #ShoppingCart post url
    path('wishlist/', views.WishlistAPIView.as_view(), name='wishlistss'), #Wishlist get url
    path('product-id/', views.CardView.as_view(), name='card'), #ShoppingCart get url
    path('productversion/<int:pk>/', views.ProductReviewAPIView.as_view(), name='product_review'), #ShoppingCart get url
    path('subscribe/', views.SubscriberAPIView.as_view(), name='subscribe'),
    
]

router.register('user', UserViewSet, basename='user')
urlpatterns += router.urls
