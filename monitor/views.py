# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json,render_mako_tostring_context
from monitor.models import Chengfa
#from django.http import JsonHttpRespone


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/monitor/home.html')


def index(request,test_id):


    arr = [test_id,test_id,test_id]
    return render_mako_context(request, '/monitor/index.html',{'data':arr})

def jisuan(request):
	r = Chengfa.objects.all()
	return render_mako_context(request, '/monitor/index.html',{'all_record':r})

def mul(request):
	mul1 = request.POST.get('mul1')
	mul2 = request.POST.get('mul2')

	r = int(mul1)  * int(mul2)

	cf = Chengfa.objects.create(chengshu=mul1,beichengshu=mul2,cfresult=r)
	cf.save()
	ctx = {
		'chengshu':mul1,
		'beichengshu':mul2,
		'cfresult':r,
		'id':cf.id
	}
	html = render_mako_tostring_context(request,'/monitor/table.part',ctx)
	return render_json({'status':True,'result':r,'html':html})
	#return render_mako_context(request, '/monitor/index.html')
