# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OembedContent.noon'
        db.add_column('page_page_oembedcontent', 'noon',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'AnnouncementContent.noon'
        db.add_column('page_page_announcementcontent', 'noon',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'SimpleGalleryContent.noon'
        db.add_column('page_page_simplegallerycontent', 'noon',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'MediaFileContent.noon'
        db.add_column('page_page_mediafilecontent', 'noon',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'FacebookImagePostsContent.noon'
        db.add_column('page_page_facebookimagepostscontent', 'noon',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'TextContent.noon'
        db.add_column('page_page_textcontent', 'noon',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'OembedContent.noon'
        db.delete_column('page_page_oembedcontent', 'noon')

        # Deleting field 'AnnouncementContent.noon'
        db.delete_column('page_page_announcementcontent', 'noon')

        # Deleting field 'SimpleGalleryContent.noon'
        db.delete_column('page_page_simplegallerycontent', 'noon')

        # Deleting field 'MediaFileContent.noon'
        db.delete_column('page_page_mediafilecontent', 'noon')

        # Deleting field 'FacebookImagePostsContent.noon'
        db.delete_column('page_page_facebookimagepostscontent', 'noon')

        # Deleting field 'TextContent.noon'
        db.delete_column('page_page_textcontent', 'noon')


    models = {
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'copyright': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
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
            'Meta': {'db_table': "'page_page_announcementcontent'", 'ordering': "['ordering']", 'object_name': 'AnnouncementContent'},
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
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'announcementcontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.facebookimagepostscontent': {
            'Meta': {'db_table': "'page_page_facebookimagepostscontent'", 'ordering': "['ordering']", 'object_name': 'FacebookImagePostsContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facebookimagepostscontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "'youthhostel.ch'"})
        },
        'page.mediafilecontent': {
            'Meta': {'db_table': "'page_page_mediafilecontent'", 'ordering': "['ordering']", 'object_name': 'MediaFileContent'},
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
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mediafilecontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'default'"})
        },
        'page.newswallcontent': {
            'Meta': {'db_table': "'page_page_newswallcontent'", 'ordering': "['ordering']", 'object_name': 'NewswallContent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'newswallcontent_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['newswall.Source']", 'symmetrical': 'False'})
        },
        'page.oembedcontent': {
            'Meta': {'db_table': "'page_page_oembedcontent'", 'ordering': "['ordering']", 'object_name': 'OembedContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oembedcontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'default'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'page.page': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Page'},
            '_cached_url': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'blank': 'True', 'max_length': '300', 'default': "''"}),
            '_ct_inventory': ('feincms.contrib.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '300'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': "orm['page.Page']", 'null': 'True', 'blank': 'True'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '300'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'template_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'screen.html'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'page.simplegallerycontent': {
            'Meta': {'db_table': "'page_page_simplegallerycontent'", 'ordering': "['ordering']", 'object_name': 'SimpleGalleryContent'},
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
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'simplegallerycontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.textcontent': {
            'Meta': {'db_table': "'page_page_textcontent'", 'ordering': "['ordering']", 'object_name': 'TextContent'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'boost_end': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'boost_priority': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'boost_start': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'noon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'textcontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '6', 'default': "'medium'"}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['page']