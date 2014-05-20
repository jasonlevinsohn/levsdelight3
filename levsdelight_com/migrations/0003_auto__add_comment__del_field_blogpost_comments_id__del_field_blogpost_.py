# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'levsdelight_com_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commenter_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=7000)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['levsdelight_com.BlogPost'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'levsdelight_com', ['Comment'])

        # Deleting field 'BlogPost.comments_id'
        db.delete_column(u'levsdelight_com_blogpost', 'comments_id')

        # Deleting field 'BlogPost.pub_date'
        db.delete_column(u'levsdelight_com_blogpost', 'pub_date')

        # Deleting field 'BlogPost.author_id'
        db.delete_column(u'levsdelight_com_blogpost', 'author_id')

        # Adding field 'BlogPost.created_at'
        db.add_column(u'levsdelight_com_blogpost', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 5, 20, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'BlogPost.updated_at'
        db.add_column(u'levsdelight_com_blogpost', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 5, 20, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'levsdelight_com_comment')

        # Adding field 'BlogPost.comments_id'
        db.add_column(u'levsdelight_com_blogpost', 'comments_id',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'BlogPost.pub_date'
        db.add_column(u'levsdelight_com_blogpost', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 20, 0, 0)),
                      keep_default=False)

        # Adding field 'BlogPost.author_id'
        db.add_column(u'levsdelight_com_blogpost', 'author_id',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'BlogPost.created_at'
        db.delete_column(u'levsdelight_com_blogpost', 'created_at')

        # Deleting field 'BlogPost.updated_at'
        db.delete_column(u'levsdelight_com_blogpost', 'updated_at')


    models = {
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