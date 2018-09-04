import json

from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# from sample.forms import SampleCreateForm
from .models import Sample, Panel
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView


class SampleCreate(CreateView):
	model = Sample
	fields = ['SampleID', 'Name', "Gender", "Panel"]
	# fields = '__all__'
	template_name = "sample/sample_form.html"

	def get_success_url(self):
		return reverse('sample_list')

	def form_valid(self, form):
		extStr = ''
		for k, v in form.data.items():
			if k not in self.fields and k != '_save' and k != 'csrfmiddlewaretoken':
				extStr += k + '=' + v + ';'
		form.instance.ExtField = extStr
		return super(SampleCreate, self).form_valid(form)


class SampleUpdate(UpdateView):
	model = Sample
	fields = ['SampleID', 'Name', "Gender", "Panel"]

	# template_name = 'sample/sample_change.html'

	def dispatch(self, *args, **kwargs):
		return super(SampleUpdate, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		extStr = ''
		for k, v in form.data.items():
			if k not in self.fields and k != '_save' and k != 'csrfmiddlewaretoken':
				extStr += k + '=' + v + ';'
		form.instance.ExtField = extStr
		return super(SampleUpdate, self).form_valid(form)

	def get_success_url(self):
		return reverse('sample_list')


class SampleList(ListView):
	# model = Sample
	paginate_by = 50

	def dispatch(self, *args, **kwargs):
		return super(SampleList, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		queryset = Sample.objects.all()
		q = self.request.GET.get('q')
		if q is not None: queryset = Sample.objects.filter(ID__contains=q)
		return queryset


def getPanelFields(request):
	# 通过前端get请求获取Panelid
	panel_id = request.GET.get('panel', '')
	# sample = request.GET.get('SampleID','')
	# 获取数据库Panel
	panel = Panel.objects.get(ID=int(panel_id))
	ext1 = ''
	opts = "<option value="" selected>---------</option>"
	if panel:
		# panel.Extfield 指panel的额外字段，并对其转化成json形式
		extfields = json.loads(panel.ExtField)
		for extfield in extfields:
			# if sample.ExtField.find(extfield["Label"]):
			# 	value = '这是一个输入框'

			# 通过后端传递给前端的标签，插入到form表单中
			# ext1 += (
			# 		"<tr><th><label for=" + extfield["Label"] + ">" + extfield[
			# 	"Label"] + "</label></th><td><input type=" +
			# 		extfield["Type"] + " name=" + extfield["Label"] + " required id=" + extfield[
			# 			"Label"] + " maxlength='32' ></td></tr>")

			if extfield['Type'] != 'radio':
				ext1 += (
						"<tr><th><label for=" + extfield["Label"] + ">" + extfield[
					"Label"] + "</label></th><td><input type=" +
						extfield["Type"] + " name=" + extfield["Label"] + " required id=" + extfield[
							"Label"] + " maxlength='32' ></td></tr>")

				# opts = "<option value="" selected>---------</option>"
				# for opt in extfield['Radio']:
				# 	opts += ("<option value=" + opt + ">" + opt + "</option>")
				# 	return opts
				# print(opts)
				#
				# ext1 += (
				# 		"<tr><th><label for=" + extfield["Label"] + ">" + extfield[
				# 	"Label"] + "</label></th><td><select name=" +
				# 		extfield["Type"] + " name=" + extfield["Label"] + " required id=" + extfield[
				# 			"Label"] + " >"+ opts +"</td></tr>")
			else:

				for opt in extfield['Radio']:
					opts += ("<option value=" + opt + ">" + opt + "</option>")
					return opts
				print(opts)

				ext1 += (
						"<tr><th><label for=" + extfield["Label"] + ">" + extfield[
					"Label"] + "</label></th><td><select name=" +
						extfield["Type"] + " required id=" + extfield[
							"Label"] + " >" + opts + "</td></tr>")
				# ext1 += (
				# 		"<tr><th><label for=" + extfield["Label"] + ">" + extfield[
				# 	"Label"] + "</label></th><td><input type=" +
				# 		extfield["Type"] + " name=" + extfield["Label"] + " required id=" + extfield[
				# 			"Label"] + " maxlength='32' ></td></tr>")


		return HttpResponse(ext1)
	else:
		return Http404
