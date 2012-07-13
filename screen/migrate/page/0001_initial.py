# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table('page_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['page.Page'])),
            ('in_navigation', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('override_url', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('redirect_to', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('_cached_url', self.gf('django.db.models.fields.CharField')(default='', max_length=300, db_index=True, blank=True)),
            ('template_key', self.gf('django.db.models.fields.CharField')(default='screen.html', max_length=255)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('navigation_extension', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('_ct_inventory', self.gf('feincms.contrib.fields.JSONField')(null=True, blank=True)),
        ))
        db.send_create_signal('page', ['Page'])

        # Adding model 'RichTextContent'
        db.create_table('page_page_richtextcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('feincms.contrib.richtext.RichTextField')(blank=True)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('night', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('boost_start', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_end', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='richtextcontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['RichTextContent'])

        # Adding model 'MediaFileContent'
        db.create_table('page_page_mediafilecontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('night', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('boost_start', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_end', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mediafilecontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mediafile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='page_mediafilecontent_set', to=orm['medialibrary.MediaFile'])),
            ('position', self.gf('django.db.models.fields.CharField')(default='default', max_length=10)),
        ))
        db.send_create_signal('page', ['MediaFileContent'])

        # Adding model 'OembedContent'
        db.create_table('page_page_oembedcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('night', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('boost_start', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_end', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='oembedcontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.CharField')(default='default', max_length=20)),
        ))
        db.send_create_signal('page', ['OembedContent'])

        # Adding model 'SimpleGalleryContent'
        db.create_table('page_page_simplegallerycontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medialibrary.Category'])),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('night', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('boost_start', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_end', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='simplegallerycontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['SimpleGalleryContent'])

        # Adding model 'AnnouncementContent'
        db.create_table('page_page_announcementcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('announcement', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('night', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('boost_start', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_end', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('boost_priority', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='announcementcontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['AnnouncementContent'])

        # Adding model 'FeedContent'
        db.create_table('page_page_feedcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedcontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['FeedContent'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table('page_page')

        # Deleting model 'RichTextContent'
        db.delete_table('page_page_richtextcontent')

        # Deleting model 'MediaFileContent'
        db.delete_table('page_page_mediafilecontent')

        # Deleting model 'OembedContent'
        db.delete_table('page_page_oembedcontent')

        # Deleting model 'SimpleGalleryContent'
        db.delete_table('page_page_simplegallerycontent')

        # Deleting model 'AnnouncementContent'
        db.delete_table('page_page_announcementcontent')

        # Deleting model 'FeedContent'
        db.delete_table('page_page_feedcontent')


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
        'page.feedcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'FeedContent', 'db_table': "'page_page_feedcontent'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedcontent_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
            'mediafile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'page_mediafilecontent_set'", 'to': "orm['medialibrary.MediaFile']"}),
            'morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'night': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mediafilecontent_set'", 'to': "orm['page.Page']"}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '10'}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'navigation_extension': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['page.Page']"}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'template_key': ('django.db.models.fields.CharField', [], {'default': "'screen.html'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'page.richtextcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'RichTextContent', 'db_table': "'page_page_richtextcontent'"},
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'richtextcontent_set'", 'to': "orm['page.Page']"}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('feincms.contrib.richtext.RichTextField', [], {'blank': 'True'})
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
        }
    }

    complete_apps = ['page']