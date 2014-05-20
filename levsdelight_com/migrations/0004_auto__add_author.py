# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'levsdelight_com_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'levsdelight_com', ['Author'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'levsdelight_com_author')


    models = {
        u'levsdelight_com.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'levsdelight_com.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images_id': ('django.db.models.fields.IntegerField', [], {}),
            'postText': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'levsdelight_com.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '7000'}),
            'commenter_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['levsdelight_com.BlogPost']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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