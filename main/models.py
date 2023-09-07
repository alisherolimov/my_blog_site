from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Phone(models.Model):
    img1 = models.ImageField(upload_to='logo/')
    number = models.CharField(max_length=13)
    img = models.ImageField(upload_to='phone/')

    def __str__(self):
        return self.number


class Banner(models.Model):
    img = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class More(models.Model):
    img = models.ImageField(upload_to='more/')
    title = models.CharField(max_length=255)
    who = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Degree(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    img = models.ImageField(upload_to='course/')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    lesson = models.CharField(max_length=255, default='etc...')
    teacher = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ImageField(upload_to='author/')
    price = models.IntegerField()

    def __str__(self):
        return self.teacher


class Discount(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Search_course(models.Model):
    course_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class Our_services(models.Model):
    img = models.ImageField(upload_to='our_services/')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Thought(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to='student/')
    name = models.CharField(max_length=255)
    institute = models.CharField(max_length=255, default='.... student')

    def __str__(self):
        return self.name


class Upcoming_events(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='upcoming_events/')
    address = models.CharField(max_length=255)
    month_day = models.IntegerField()
    month = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Smm(models.Model):
    pinterest = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='news/')
    text1 = models.TextField()
    text2 = models.TextField()
    month = models.CharField(max_length=255)
    month_day = models.IntegerField()
    writer = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    text = models.TextField()
    new = models.ForeignKey(News, on_delete=models.CASCADE)
