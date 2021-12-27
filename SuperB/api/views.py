from rest_framework import permissions, status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from core.models import Subscriber
from .serializers import UserSerializer

from product.models import Product, ProductVersion, Category, Review
from order.models import ShoppingCart, CartItem, Wishlist
from blog.models import Category as BlogCategory
from blog.models import Blog
from api.serializers import ProductSerializer, CardItemSerializer, WishlistSerializer, ProductVersionSerializer, CategorySerializer, BlogCategorySerializer, BlogSerializer, CardSerializer, SubscriberSerializer

# Register API


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer

# Products API


class ProductAPIView(APIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Product.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            qs = Product.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_product(self, data):
        return Product.objects.create(
            title=data.get('title'),
            price=int(data.get('price')),
            discount_price=int(data.get('discount_price')),
            category=data.get('product.Category'),
            brand=data.get('product.Brand'),
            description=data.get('Description'),
            # product_tag=data.get('product.Tag'),
        )

    def create_product_version(self, data):
        product = self.create_product(data)
        versions = []
        for version in data.get('versions'):
            version = ProductVersion(**version)
            version.product = product
            versions.append(version)
        ProductVersion.objects.bulk_create(versions)
        return product

    def post(self, request, *args, **kwargs):
        data = request.data

        """
        {
            "title":"Product #3",
            "price":55,
            "discount_price":42,
            "category":1,
            "brand":1,
            "description":"Some Desc Product #3",
            "versions" : [
                {
                    "color" : 2,
                    "size" : 2, 
                    "quantity" : 13,
                    "version_description": "Salam1",
                    "is_main" : true
                },
                {
                    "color" : 3,
                    "size" : 1, 
                    "quantity" : 3,
                    "version_description": "Salam2"
                }
            ]
        }
        """
        product = self.create_product_version(data)
        serializer = self.serializer_class(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductVersionsAPIView(APIView):
    serializer = ProductVersionSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('product_id'):
            obj = ProductVersion.objects.filter(
                product__id=kwargs.get('product_id'))
            stat = status.HTTP_200_OK
            result = self.serializer(obj, many=True).data
            if kwargs.get('pk'):
                obj = ProductVersion.objects.get(pk=kwargs.get('pk'))
                result = self.serializer(obj).data
        else:
            stat = status.HTTP_404_NOT_FOUND
            result = {'detail': 'Product does not exist.'}
        return Response(result, status=stat)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSingleAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Product.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            qs = Product.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Product.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            qs = Product.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Login API


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

# Proudct Categories Api


class CategoryAPIView(APIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Category.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            qs = Category.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class ListCategoryApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CreateCategoryApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategoryApiView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategoryApiView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Blog Categories Api


class BlogCategoryAPIView(APIView):
    serializer_class = BlogCategorySerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = BlogCategory.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            qs = BlogCategory.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class ListBlogCategoryApiView(ListAPIView):
#     queryset = BlogCategory.objects.all()
#     serializer_class = BlogCategorySerializer


class CreateBlogCategoryApiView(CreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class UpdateBlogCategoryApiView(UpdateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class DeleteBlogCategoryApiView(DestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

# Blogs Api


class BlogAPIView(APIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Blog.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            qs = Blog.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class ListBlogAPIView(ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


class CreateBlogAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class UpdateBlogAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DeleteBlogAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CardView(APIView):
    serializer_class = CardItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        ShoppingCart.objects.get_or_create(user=request.user, is_ordered=False)
        basket = CartItem.objects.filter(
            cart=ShoppingCart.objects.get(user=request.user, is_ordered=False))
        serializer = self.serializer_class(basket, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        action = request.data.get('action')
        quantity = request.data.get('quantity')

        product = ProductVersion.objects.filter(pk=product_id).first()
        serializer = ProductVersionSerializer(product)
        cart, created = ShoppingCart.objects.get_or_create(user=request.user, is_ordered=False)

        if product:
            if action == 'add':
                basket = ShoppingCart.objects.get(user=request.user, is_ordered=False)
                # product_version = product.main_product
                # product_version.quantity -= 1
                # product_version.save()
                cart_item, created = CartItem.objects.get_or_create(
                    cart=basket, product=product)
                cart_item.quantity += int(quantity)
                cart_item.save()
                ShoppingCart.objects.get(user=request.user, is_ordered=False).product.add(product)
                # request.user.user_cart.product.add(product)
                message = {'success': True,
                           'message': 'Product added to your card.'}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif action == 'update':
                basket = ShoppingCart.objects.get(user=request.user, is_ordered=False)
                cart_item, created = CartItem.objects.get_or_create(
                    cart=basket, product=product)
                cart_item.quantity = int(quantity)
                cart_item.save()
                ShoppingCart.objects.get(user=request.user, is_ordered=False).product.add(product)
                message = {'success': True,
                           'message': 'Product added to your card.'}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif action == 'remove':
                basket = ShoppingCart.objects.get(user=request.user, is_ordered=False)
                cart_item, created = CartItem.objects.get_or_create(
                    cart=basket, product=product)
                cart_item.quantity = 0
                cart_item.save()
                ShoppingCart.objects.get(user=request.user, is_ordered=False).product.add(product)
                CartItem.objects.filter(cart=basket, product=product).delete()
                message = {'success': True,
                           'message': 'Product removed to your card.'}
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message': 'Product not found.'}
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewAPIView(APIView):
    serializer_class = ProductVersionSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            obj = ProductVersion.objects.get(pk=kwargs.get("pk"))
            serializer = self.serializer_class(obj)
            stat = status.HTTP_200_OK
        return Response(serializer.data, status=stat)

    # def post(self, request, *args, **kwargs):
    #     product_id = request.data.get('product_id')


class WishlistAPIView(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pro_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        serializer = self.serializer_class(pro_wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        product = ProductVersion.objects.filter(pk=product_id).first()
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)

        if product and product not in wishlist.product.all():
            wishlist.product.add(product)
        else:
            wishlist.product.remove(product)
        message = {'success': True,
                   'message': 'Product added to your wishlist.'}
        return Response(message, status=status.HTTP_201_CREATED)


class SubscriberAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer()  # create a serializer
        email =  request.data['email']
        if email and Subscriber.objects.filter(email=email).exists() == False:
            subscribe = Subscriber(
                email = email
            )
            subscribe.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)