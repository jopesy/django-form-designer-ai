# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('form_designer_formlog', 'data', 'tmp_data')
        # Adding field 'FormLog.created_by'
        db.add_column('form_designer_formlog', 'created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm["%s.%s" % (User._meta.app_label, User._meta.object_name)], null=True, blank=True), keep_default=False)

        # Adding model 'FormValue'
        db.create_table('form_designer_formvalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_log', self.gf('django.db.models.fields.related.ForeignKey')(related_name='values', to=orm['form_designer.FormLog'])),
            ('field_name', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('value', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('form_designer', ['FormValue'])

    def backwards(self, orm):
        # Adding field 'FormLog.data'
        db.add_column('form_designer_formlog', 'data', self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True), keep_default=False)

        # Deleting field 'FormLog.created_by'
        db.delete_column('form_designer_formlog', 'created_by_id')

        # Deleting model 'FormValue'
        db.delete_table('form_designer_formvalue')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
         "%s.%s" % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'form_designer.formdefinition': {
            'Meta': {'object_name': 'FormDefinition'},
            'action': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'allow_get_initial': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_logged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'error_message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mail_from': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_uploaded_files': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'message_template': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'POST'", 'max_length': '10'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'private_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'public_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'require_hash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'save_uploaded_files': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'submit_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_clear': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'success_message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formdefinitionfield': {
            'Meta': {'ordering': "['position']", 'object_name': 'FormDefinitionField'},
            'choice_labels': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_model': ('form_designer.fields.ModelNameField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_model_empty_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_values': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_class': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'initial': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'max_digits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regex': ('form_designer.fields.RegexpExpressionField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formlog': {
            'Meta': {'object_name': 'FormLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "User", 'null': 'True', 'blank': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': "orm['form_designer.FormDefinition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'form_designer.formvalue': {
            'Meta': {'object_name': 'FormValue'},
            'field_name': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'form_log': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'values'", 'to': "orm['form_designer.FormLog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['form_designer']
