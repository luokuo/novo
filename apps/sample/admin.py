import xadmin

# Register your models here.
from sample.models import Panel, Sample


class PanelAdmin(object):
	list_display = ['ID', 'PanelName', 'PanelVersion', 'ExtField', 'PanelNote']
	serch_fields = ['ID', 'PanelName', 'PanelVersion', 'ExtField', 'PanelNote']
	list_filter = ['ID', 'PanelName', 'PanelVersion', 'ExtField', 'PanelNote']


class SampleAdmin(object):
	list_display = ['SampleID', 'Name', 'Gender', 'Panel', 'ExtField']
	serch_fields = ['SampleID', 'Name', 'Gender', 'Panel', 'ExtField']
	list_filter = ['SampleID', 'Name', 'Gender', 'Panel', 'ExtField']


xadmin.site.register(Panel, PanelAdmin)
xadmin.site.register(Sample, SampleAdmin)
