from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from recommender.utils import recommend

from django.shortcuts import render,render_to_response


# def hello(request):
# 	context = {}
# 	context['a'] = 'hello world'
# 	return render(request,'index.html',context)

# def index(request):
	
# 	return render_to_response('index.html',{
# 		'bookdic':{},
# 		'name': 'wangbei',
# 		'color1':'red',
# 		'flag':True,
# 		})
# def hot(request):
# 	return HttpResponse('hot')


from django.shortcuts import render,render_to_response
# Create your views here.

def hello(request,name):
	return render_to_response('index.html',{
		'name',name
	})

@csrf_exempt
def index(request,name):
	if request.method == "POST":
		id = int(request.POST.get('id'))
		movie_list = recommend(id)

		return HttpResponse(movie_list)
	return render_to_response('index.html',{
		'name':name
	})
def main(request):
	return render_to_response('index.html')
