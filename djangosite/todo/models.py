from django.db import models

# Create your models here.
class TodoEntry(models.Model):
    class Meta:
        db_table = '20171024_todoentry_ceshi'
        managed = 'False'

    task = models.CharField(max_length= 200)
    status = models.IntegerField()
    create_date = models.DateTimeField('create date')

    def __unicode__(self):
        return self.task


class User(models.Model):
    class Meta:
        db_table = '20171024_user_ceshi'
        managed = 'False'

    html_id = models.CharField(max_length=255, db_column='html_id', primary_key=True)
    userName = models.CharField(max_length=200, db_column='username')
    passWord = models.CharField(max_length=200, db_column='password')
    cid = models.IntegerField(db_column='cid')


class Charactor(models.Model):
    class Meta:
        db_table = '20171024_charactor_ceshi'
        managed = 'False'
        app_label = ''

    html_id = models.CharField(max_length=255, db_column='html_id', primary_key=True)
    charactor = models.CharField(max_length=255, db_column='charactor')
    hGroup = models.IntegerField(db_column='h_group')