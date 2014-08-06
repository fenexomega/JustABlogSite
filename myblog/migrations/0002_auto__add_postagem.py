# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Postagem'
        db.create_table(u'myblog_postagem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=20000)),
            ('data_de_postagem', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'myblog', ['Postagem'])


    def backwards(self, orm):
        # Deleting model 'Postagem'
        db.delete_table(u'myblog_postagem')


    models = {
        u'myblog.postagem': {
            'Meta': {'object_name': 'Postagem'},
            'data_de_postagem': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '20000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['myblog']