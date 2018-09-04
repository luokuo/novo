import json

from django.db import models


class CMode(models.Model):
	@classmethod
	def create(self, ID, AttrDict={}):
		obj = self(pk=ID)
		for f in self._meta.fields:
			if f.verbose_name in AttrDict:
				if not f.is_relation:
					obj.__setattr__(f.name, AttrDict[f.verbose_name])
		return obj

	def getLabel(self):
		fields = self._meta.fields
		data = list()
		for f in fields:
			data.append(f.verbose_name)
		return data

	def getData(self):
		fields = self._meta.fields
		data = list()
		for f in fields:
			data.append([f.name, f.verbose_name, f.value_to_string(self)])
		return data

	class Meta:
		abstract = True


class Panel(CMode):
	ID = models.CharField("ID", max_length=24, primary_key=True)
	PanelName = models.CharField("Panel名称", max_length=32)
	PanelVersion = models.CharField("版本号", max_length=32)
	ExtField = models.TextField("额外字段", blank=True)
	PanelNote = models.CharField("备注", max_length=32)

	class Meta:
		verbose_name = '试剂盒'
		verbose_name_plural = verbose_name
		db_table = 'panel'

	def __str__(self):
		return self.PanelName


class Sample(CMode):
	SampleID = models.CharField("样本编号", max_length=32)
	Name = models.CharField("姓名", max_length=32)
	Gender = models.CharField("性别", max_length=1, choices=(('男', '男'), ('女', '女'),))
	Panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
	ExtField = models.TextField("额外字段", blank=True)

	class Meta:
		verbose_name = '样本'
		verbose_name_plural = verbose_name
		db_table = 'sample'

	def __str__(self):
		return self.SampleID + '_' + self.Name
