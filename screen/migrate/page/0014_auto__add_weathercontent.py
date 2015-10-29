# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeatherContent'
        db.create_table('page_page_weathercontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['page.Page'], related_name='weathercontent_set')),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['WeatherContent'])


    def backwards(self, orm):
        # Deleting model 'WeatherContent'
        db.delete_table('page_page_weathercontent')


    models = {
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['medialibrary.Category']", 'related_name': "'children'", 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'blank': 'True', 'to': "orm['medialibrary.Category']"}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'newswall.source': {
            'Meta': {'ordering': "['ordering', 'name']", 'object_name': 'Source'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        },
        'page.announcementcontent': {
            'Meta': {'db_table': "'page_page_announcementcontent'", 'ordering': "['ordering']", 'object_name': 'AnnouncementContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'announcement': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'announcementcontent_set'"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.facebookimagepostscontent': {
            'Meta': {'db_table': "'page_page_facebookimagepostscontent'", 'ordering': "['ordering']", 'object_name': 'FacebookImagePostsContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'facebookimagepostscontent_set'"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'youthhostel.ch'"})
        },
        'page.mediafilecontent': {
            'Meta': {'db_table': "'page_page_mediafilecontent'", 'ordering': "['ordering']", 'object_name': 'MediaFileContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']", 'related_name': "'+'"}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'mediafilecontent_set'"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'default'"})
        },
        'page.newswallcontent': {
            'Meta': {'db_table': "'page_page_newswallcontent'", 'ordering': "['ordering']", 'object_name': 'NewswallContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'newswallcontent_set'"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['newswall.Source']"})
        },
        'page.oembedcontent': {
            'Meta': {'db_table': "'page_page_oembedcontent'", 'ordering': "['ordering']", 'object_name': 'OembedContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'oembedcontent_set'"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'default'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'page.page': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Page'},
            '_cached_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True', 'default': "''", 'blank': 'True'}),
            '_ct_inventory': ('feincms.contrib.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'Basel, Switzerland'"}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['page.Page']", 'related_name': "'children'", 'blank': 'True'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'template_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'screen.html'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'page.simplegallerycontent': {
            'Meta': {'db_table': "'page_page_simplegallerycontent'", 'ordering': "['ordering']", 'object_name': 'SimpleGalleryContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medialibrary.Category']"}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'simplegallerycontent_set'"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.textcontent': {
            'Meta': {'db_table': "'page_page_textcontent'", 'ordering': "['ordering']", 'object_name': 'TextContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'textcontent_set'"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '6', 'default': "'medium'"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'page.weathercontent': {
            'Meta': {'db_table': "'page_page_weathercontent'", 'ordering': "['ordering']", 'object_name': 'WeatherContent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['page.Page']", 'related_name': "'weathercontent_set'"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['page']