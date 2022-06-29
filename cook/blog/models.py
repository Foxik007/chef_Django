import kwargs as kwargs
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    class MPTMeta:
        order_inserion_by = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='articles/')
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title[0:20]

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.category.slug,"post_slug":self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(Post,
                             related_name='recipe',
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_recipes(self):
        return self.recipes.all()

class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=30)
    message = models.TextField(max_length=100)
    post = models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'