from django.db import models

from SuperB.utils.base import BaseModel

# Create your models here.

class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Title', help_text='Max 255 chars')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=35.00)
    category = models.ForeignKey('product.Category', on_delete=models.CASCADE, related_name='category', verbose_name="Category")
    brand = models.ForeignKey('product.Brand', on_delete=models.CASCADE, verbose_name="Brand")
    description = models.TextField(verbose_name="Description", blank=True , null=True)
    product_tag = models.ManyToManyField('product.Tag', related_name="product_tags", verbose_name="Tag")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @property
    def main_product(self):
        return self.versions.filter(is_main=True).first()

    @property
    def total_quantity(self):
        return sum([version.quantity for version in self.versions.all()])


    def __str__(self):
        return self.title

class Color(BaseModel):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")
    hex_code = models.CharField(verbose_name="Hex Code", max_length=6, default="ffffff")

    def __str__(self):
        return self.title


class Size(BaseModel):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.")

    def __str__(self):
        return self.title

class ProductVersion(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name="Product Title")
    color = models.ForeignKey(Color, default=1, verbose_name='Color', on_delete=models.CASCADE, related_name='product_color')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=1, verbose_name='Size')
    quantity = models.IntegerField(verbose_name='Quantity', default=0)
    version_description = models.TextField(verbose_name="New_description", null=True, blank=True)
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product Version"
        verbose_name_plural = "Product Versions"

    @property
    def main_photo(self):
        return self.product_photo.filter(is_main=True).first()

    @property
    def other_photo(self):
        return self.product_photo.all()
    

    def __str__(self):
        return f'{self.product}'


class Category(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Title', help_text='Max 255 chars')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children", verbose_name="Category", null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    @property
    def is_parent(self):
        return not self.parent

    @property
    def has_children(self):
        return self.children.exists()

    def __str__(self):
        return f'{self.title}'


class Brand(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Brand', help_text='Max 255 chars')

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.title


class Tag(BaseModel):
    tag = models.CharField(max_length=255, verbose_name='Tag')

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.tag


class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_review", verbose_name="Product_Review", null=True, blank=True)
    user_review = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name="user_review", verbose_name="User", null=True, blank=True)
    price_rating = models.IntegerField(choices=(
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    ), default=5, verbose_name='price')
    value_rating = models.IntegerField(choices=(
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    ), default=5, verbose_name='value')
    quality_rating = models.IntegerField(choices=(
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    ), default=5, verbose_name='quality')
    nickname = models.CharField(max_length=255, verbose_name='Nickname', help_text='Max 255 chars')
    summary = models.CharField(max_length=255, verbose_name='Summary', help_text='Max 255 chars')
    review = models.TextField(verbose_name="Review")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'{self.product}'
    

class Image(BaseModel):
    image = models.ImageField(verbose_name="Image", null=True, blank=True, upload_to = 'images/image/')
    product_photo = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, related_name='product_photo', verbose_name="product_photo", null=True, blank=True,)
    blog_photo = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='blog_photo', verbose_name="blog_photo", null=True, blank=True,)
    comment_author_photo = models.ForeignKey('blog.Comment', on_delete=models.CASCADE, related_name='comment_author_photo', verbose_name="comment_author_photo", null=True, blank=True,)
    blog_author_photo = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='blog_author_photo', verbose_name="blog_author_photo", null=True, blank=True,)
    is_main = models.BooleanField(default=False)

