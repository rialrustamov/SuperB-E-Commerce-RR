from django.db import models
from ckeditor.fields import RichTextField

from SuperB.utils.base import BaseModel

class Blog(BaseModel):
    # image = models.ImageField(null = True, blank = True, verbose_name='Image', upload_to = 'blogs/image/')
    title = models.TextField(verbose_name='Title')
    # author_image = models.ImageField(null = True, blank = True, verbose_name='Author Image', upload_to = 'blogs/image/')
    author = models.CharField(max_length=50 ,verbose_name='Author')
    description = models.TextField(verbose_name='Description')
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE, verbose_name='Category')
    main_desc = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    @property
    def main_photo(self):
        return self.blog_photo.filter(is_main=True).first()

    @property
    def author_photo(self):
        return self.blog_author_photo.filter(is_main=True).first()



    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.TextField(verbose_name='Title')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title



class Comment(BaseModel):
    author = models.CharField(max_length=50 ,verbose_name='Author', null=True, blank=True) # User id ile Foreign Key
    message = models.TextField(verbose_name='Message')
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, verbose_name='Blog', related_name='blogs', null=True, blank=True)
    replied = models.ForeignKey('blog.Comment', on_delete=models.CASCADE, verbose_name='Replied', null=True, blank=True)
    # guest_name = models.CharField(max_length=50 ,verbose_name='Guest Name', null=True)
    # guest_email = models.EmailField(verbose_name='Guest Email', null=True)
    user_comment= models.ForeignKey('user.User', on_delete=models.CASCADE, related_name="user_comment", verbose_name="User", null=True, blank=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.author

    @property
    def comment_photo(self):
        return self.comment_author_photo.filter(is_main=True).first()

