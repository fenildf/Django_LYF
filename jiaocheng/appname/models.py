from django.db import models
from django.utils.encoding import python_2_unicode_compatible

APP_LABEL = 'mysql'

@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()

    class Meta:
        db_table = '20171025_author'
        #managed = 'False'
        #app_label = APP_LABEL

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Article_Houtai(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间',
                                    auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间',
                                       auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '20171025_article_houtai'
        #managed = 'False'
        app_label = APP_LABEL


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    class Meta:
        db_table = '20171025_article'
        #managed = 'False'
        #app_label = APP_LABEL


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '20171025_tag'
        #managed = 'False'
        #app_label = APP_LABEL

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = '20171025_person'
        #managed = 'False'
        #app_label = APP_LABEL

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = '20171025_blog'
        #managed = 'False'
        #app_label = APP_LABEL

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        db_table = '20171025_entry'
        #managed = 'False'
        #app_label = APP_LABEL

    def __str__(self):
        return self.name