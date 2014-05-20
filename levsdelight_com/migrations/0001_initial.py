# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slideshow'
        db.create_table(u'levsdelight_com_slideshow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('pictureLocation', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('isActive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slideshow_id', self.gf('django.db.models.fields.IntegerField')()),
            ('order_id', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'levsdelight_com', ['Slideshow'])

        # Adding model 'MonthMap'
        db.create_table(u'levsdelight_com_monthmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slideshow_id', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'levsdelight_com', ['MonthMap'])

        # Adding model 'BlogPost'
        db.create_table(u'levsdelight_com_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postText', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('images_id', self.gf('django.db.models.fields.IntegerField')()),
            ('comments_id', self.gf('django.db.models.fields.IntegerField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'levsdelight_com', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'Slideshow'
        db.delete_table(u'levsdelight_com_slideshow')

        # Deleting model 'MonthMap'
        db.delete_table(u'levsdelight_com_monthmap')

        # Deleting model 'BlogPost'
        db.delete_table(u'levsdelight_com_blogpost')


    models = {
        u'levsdelight_com.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'comments_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images_id': ('django.db.models.fields.IntegerField', [], {}),
            'postText': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
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