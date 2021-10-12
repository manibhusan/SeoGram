from django.db import models
from django_extensions.db.fields import AutoSlugField

from .enums import CATEGORIES


# Create your models here.


class Seo(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


class SeoTeam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'SEO Team'
        verbose_name_plural = 'SEO Teams'

    def __str__(self):
        return self.title


class Plan(models.Model):
    pricing_type = models.CharField(max_length=255)
    dollar = models.DecimalField(max_digits=19, decimal_places=2)
    month = models.CharField(max_length=255)
    campaign = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    reviews = models.CharField(max_length=255)
    optimization = models.CharField(max_length=255)
    support = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        return self.pricing_type


class Category(models.Model):
    name = models.CharField(choices=CATEGORIES, max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.first_name


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email
