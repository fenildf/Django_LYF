# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-28 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
            ],
            options={
                'db_table': '20171025_article',
            },
        ),
        migrations.CreateModel(
            name='Article_Houtai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': '20171025_article_houtai',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qq', models.CharField(max_length=10)),
                ('addr', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': '20171025_author',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': '20171025_blog',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField()),
                ('n_comments', models.IntegerField()),
                ('n_pingbacks', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('authors', models.ManyToManyField(to='appname.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appname.Blog')),
            ],
            options={
                'db_table': '20171025_entry',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': '20171025_person',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '20171025_tag',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appname.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='appname.Tag'),
        ),
    ]