# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tag'
        db.create_table('tagger_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80, db_index=True)),
        ))
        db.send_create_signal('tagger', ['Tag'])


    def backwards(self, orm):
        
        # Deleting model 'Tag'
        db.delete_table('tagger_tag')


    models = {
        'tagger.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80', 'db_index': 'True'})
        }
    }

    complete_apps = ['tagger']
