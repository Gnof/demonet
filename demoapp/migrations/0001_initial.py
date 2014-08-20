# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DemoModel'
        db.create_table(u'demoapp_demomodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'demoapp', ['DemoModel'])

        # Adding model 'SubModel'
        db.create_table(u'demoapp_submodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demoapp.DemoModel'])),
        ))
        db.send_create_signal(u'demoapp', ['SubModel'])


    def backwards(self, orm):
        # Deleting model 'DemoModel'
        db.delete_table(u'demoapp_demomodel')

        # Deleting model 'SubModel'
        db.delete_table(u'demoapp_submodel')


    models = {
        u'demoapp.demomodel': {
            'Meta': {'object_name': 'DemoModel'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'demoapp.submodel': {
            'Meta': {'object_name': 'SubModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demoapp.DemoModel']"})
        }
    }

    complete_apps = ['demoapp']