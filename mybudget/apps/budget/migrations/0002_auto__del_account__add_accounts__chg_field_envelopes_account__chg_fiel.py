# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'budget_account')

        # Adding model 'Accounts'
        db.create_table(u'budget_accounts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('current_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
        ))
        db.send_create_signal(u'budget', ['Accounts'])


        # Changing field 'Envelopes.account'
        db.alter_column(u'budget_envelopes', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Accounts'], null=True))

        # Changing field 'RegularMonthlyExpenses.account'
        db.alter_column(u'budget_regularmonthlyexpenses', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Accounts'], null=True))

        # Changing field 'Incomes.account'
        db.alter_column(u'budget_incomes', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Accounts'], null=True))

    def backwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'budget_account', (
            ('current_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'budget', ['Account'])

        # Deleting model 'Accounts'
        db.delete_table(u'budget_accounts')


        # Changing field 'Envelopes.account'
        db.alter_column(u'budget_envelopes', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Account'], null=True))

        # Changing field 'RegularMonthlyExpenses.account'
        db.alter_column(u'budget_regularmonthlyexpenses', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Account'], null=True))

        # Changing field 'Incomes.account'
        db.alter_column(u'budget_incomes', 'account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget.Account'], null=True))

    models = {
        u'budget.accounts': {
            'Meta': {'object_name': 'Accounts'},
            'current_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.envelopes': {
            'Meta': {'object_name': 'Envelopes'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.Accounts']", 'null': 'True'}),
            'cash': ('django.db.models.fields.BooleanField', [], {}),
            'current_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_replenishment': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.expenses': {
            'Meta': {'object_name': 'Expenses'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'envelope': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.Envelopes']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.incomes': {
            'Meta': {'object_name': 'Incomes'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.Accounts']", 'null': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'budget.regularmonthlyexpenses': {
            'Meta': {'object_name': 'RegularMonthlyExpenses'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget.Accounts']", 'null': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['budget']