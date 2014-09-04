from django.shortcuts import render
from demoapp.models import DemoModel, SubModel
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.core import serializers as s

# Create your views here.

''' Render the Home page '''
def home(request):
	context = {}
	return render(request, 'index.html', context)

''' Simple API Request Handler'''
'''
PARAMS:
- function - name of functionality to call
'''
def api(request):

	''' currently supporting GET and POST '''
	method = request.method

	if method == "GET":
		function = request.GET.get('function')
		
		# various function handlers
		if function == "getDemoModel":
			return getDemoModel(request)

	elif method == "POST": 
		function = request.POST.get('function')

		# various POST function handlers
		if function == "addDemoModel":
			return addDemoModel(request)

	else:
		return str(method) + " -- Not Supported"
	return None

'''
Demo GET API Function call to retrieve DemoModel
'''
def getDemoModel(request):
	# The model to retrieve
	mname = request.GET.get('modelname')
	try:
		# retrieve it from the database
		model = DemoModel.objects.get(name=mname)
		# serialize the model 
		ser_model = s.serialize('json', [model])
		# return as http response
		return HttpResponse(ser_model, status=200)
	except ObjectDoesNotExist, e:
		return HttpResponse("Model Not Found", status=404)

'''
Demo POST API Function call to add a DemoModel
'''
def addDemoModel(request):
	try:
		mname = request.POST.get('modelname')
		modeldesc = request.POST.get('modeldesc')
		new_model = DemoModel(name=mname, desc=modeldesc)
		new_model.save()
		return HttpResponse(new_model.id, status=200)
	except Exception, e:
		print e
		return HttpResponse('Error', status=403)
	

