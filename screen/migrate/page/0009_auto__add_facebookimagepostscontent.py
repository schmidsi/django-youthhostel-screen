# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookImagePostsContent'
        db.create_table('page_page_facebookimagepostscontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(default='youthhostel.ch', max_length=100)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('night', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('boost_start', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_end', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='facebookimagepostscontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['FacebookImagePostsContent'])


    def backwards(self, orm):
        # Deleting model 'FacebookImagePostsContent'
        db.delete_table('page_page_facebookimagepostscontent')


    models = {
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'page.announcementcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'AnnouncementContent', 'db_table': "'page_page_announcementcontent'"},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'announcement': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'announcementcontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.facebookimagepostscontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'FacebookImagePostsContent', 'db_table': "'page_page_facebookimagepostscontent'"},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facebookimagepostscontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'youthhostel.ch'", 'max_length': '100'})
        },
        'page.mediafilecontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'MediaFileContent', 'db_table': "'page_page_mediafilecontent'"},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'related_name': "'+'", 'to': "orm['medialibrary.MediaFile']"}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mediafilecontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        },
        'page.newswallcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'NewswallContent', 'db_table': "'page_page_newswallcontent'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'newswallcontent_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newswall.Source']", 'symmetrical': 'False'})
        },
        'page.oembedcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'OembedContent', 'db_table': "'page_page_oembedcontent'"},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oembedcontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'page.page': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Page'},
            '_cached_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'db_index': 'True', 'blank': 'True'}),
            '_ct_inventory': ('feincms.contrib.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['page.Page']"}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'template_key': ('django.db.models.fields.CharField', [], {'default': "'screen.html'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'page.simplegallerycontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'SimpleGalleryContent', 'db_table': "'page_page_simplegallerycontent'"},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medialibrary.Category']"}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'simplegallerycontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.textcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'TextContent', 'db_table': "'page_page_textcontent'"},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'textcontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '6'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['page']