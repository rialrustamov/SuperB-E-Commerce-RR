from rest_framework import serializers
from django.db.models import fields

from product.models import Product, ProductVersion, Category, Review, Image
from order.models import ShoppingCart, Wishlist, CartItem
from blog.models import Category as BlogCategory, Blog
from django.contrib.auth import get_user_model
from user.models import *
from core.models import *

User = get_user_model()


class ProductOverviewSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_review(self, obj):
        qs = obj.product_review.all()
        return ReviewSerializer(qs, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    main_product = serializers.SerializerMethodField()
    versions = serializers.SerializerMethodField()
    main_image = serializers.SerializerMethodField()
    product_review = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'price', 'discount_price', 'category', 'brand', 'description',
                  'total_quantity', 'main_product', 'main_image', 'versions', 'product_tag', 'product_review']

    def get_total_quantity(self, obj):
        return obj.total_quantity

    def get_main_product(self, obj):
        return ProductVersionSerializer(obj.main_product).data

    def get_versions(self, obj):
        qs = obj.versions.exclude(id=obj.main_product.id)
        return ProductVersionSerializer(qs, many=True).data

    def get_main_image(self, obj):
        if obj.main_product.main_photo.image:
            return obj.main_product.main_photo.image.url
        return None

    def get_product_review(self, obj):
        qs = obj.product_review.all()
        return ReviewSerializer(qs, many=True).data


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductOverviewSerializer()
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductVersion
        fields = '__all__'

    def get_image(self, obj):
        qs = obj.product_photo.all()
        return ImageSerializer(qs, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['username'] = validated_data['email']
        user = super().create(validated_data=validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation',
                  'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class CardItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'