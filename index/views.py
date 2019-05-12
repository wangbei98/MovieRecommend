from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from recommender.recommender import recommend
from Utils import util

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
		Id = int(request.POST.get('id'))
		id_list = recommend(Id)
		movie_dic = {}
		for id in id_list:
			# movie_dic[id] = util.getMovieInfo(id)
			if id not in movie_dic:
				movie_dic[id] = {}
			info = util.getMovieInfo(id)
			movie_dic[id] = {'movie_id':info[0],'name':info[1].decode('utf-8'),'genres':info[2].decode('utf-8')}
		# return HttpResponse(movie_dic)
		# return HttpResponse(util.getMovieInfo(Id))
		return render_to_response('index.html',{
			'name':name,
			'movie_dic':movie_dic,
			'flag':True
		})
	return render_to_response('index.html',{
		'name':name
	})
def main(request):
	return render_to_response('index.html')

if __name__ =='__main__':
	id_list = recommend(1)
	movie_dic = {}
	for id in id_list:
		if id not in movie_dic:
			movie_dic[id] = {}
		info = util.getMovieInfo(id)
		movie_dic[id] = {'movieId': info[0], 'name': info[1], 'genres': info[2]}
	print(movie_dic)