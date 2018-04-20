# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


# https://docs.djangoproject.com/en/1.8/ref/migration-operations/
def forwards_func(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Category = apps.get_model('blog', 'Category')
    db_alias = schema_editor.connection.alias
    Category.objects.using(db_alias).bulk_create([
        Category(name='long'),
        Category(name='short'),
    ])
    for post in Post.objects.all():
        title = post.title
        title_length = len(title)

        cat_list_long = Category.objects.filter(name='long')
        cat_long = cat_list_long[0]
        cat_list_short = Category.objects.filter(name='short')
        cat_short = cat_list_short[0]

        # TODO: saving object
        if title_length > 8:
            post.category = cat_long
        else:
            post.category = cat_short
        post.save()


def reverse_func(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Category = apps.get_model('blog', 'Category')
    db_alias = schema_editor.connection.alias

    Category.objects.using(db_alias).filter(name='long').delete()
    Category.objects.using(db_alias).filter(name='short').delete()

    for post in Post.objects.all():
        post.category = None


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20170421_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='blog.Category', null=True),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]



