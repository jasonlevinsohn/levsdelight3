# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.pub_date'
        db.add_column(u'levsdelight_com_blogpost', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 15, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.pub_date'
        db.delete_column(u'levsdelight_com_blogpost', 'pub_date')


    models = {
        u'levsdelight_com.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'comments_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images_id': ('django.db.models.fields.IntegerField', [], {}),
            'postText': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'levsdelight_com.monthmap': {
            'Meta': {'object_name': 'MonthMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slideshow_id': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'levsdelight_com.slideshow': {
            'Meta': {'object_name': 'Slideshow'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {}),
            'pictureLocation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slideshow_id': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['levsdelight_com']