from newsextraction.modules.utils import initial_check
from newsextraction.modules.utils import *
from newsextraction.modules import newstotext
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import NameForm,SearchForm
from .models import *
from .methods import *
from django.db.models import Q #object used to encapsulate a collection of keyword arguments specified as in “Field lookups”.

def index(request):
	initial_check()
	news_list = rssdata.objects.all().order_by("-date")
	page = request.GET.get('page', 1)

	paginator = Paginator(news_list, 5)
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)
	print(list(news_list)[0].date)
	return render(request, 'newsextraction/index.html', {
			'newsList': list(news_list),
			'isHome':True,
		}
	)



def searchView(request):
    

    checks=[]
    posts=[]
    queries=[]




    if request.method == 'POST':
        search_main =request.POST.get('search_main')
        all = request.POST.get('all')
        header = request.POST.get('header')
        body = request.POST.get('body')
        source = request.POST.get('source')
        death_no = request.POST.get('death_no')
        injury_no = request.POST.get('injury_no')
        location = request.POST.get('location')
        date = request.POST.get('date')
        year = request.POST.get('year')
        month = request.POST.get('month')
        day = request.POST.get('day')
        search_text = request.POST.get('search_text')

        

        if search_main != None:
            search=search_main
        else:
            search = search_text

        try: 
            int(search)
            flag = 1

                    
        except ValueError:
            flag = 0

        if (all=='on' and flag ==0):
            queries = rssdata.objects.filter(Q(header__icontains=search)| Q(body__icontains=search)|Q(source__icontains=search)\
                |Q(location__icontains=search)| Q(date__iexact=search)\
                    | Q(day__icontains=search) | Q(month__icontains=search))
            for query in queries:
                posts.append(query)

        elif(all == 'on' and flag == 1):
            queries = rssdata.objects.filter(Q(header__icontains=search)| Q(body__icontains=search)|Q(source__icontains=search)\
                |Q(death_no__iexact=int(search))|Q(location__icontains=search)| Q(injury_no__iexact=int(search))| Q(date__iexact=search)\
                    |Q(year__iexact=int(search))| Q(day__icontains=search) | Q(month__icontains=search))
            for query in queries:
                posts.append(query)

        else:

            if header=='on':
                queries = rssdata.objects.filter(Q(header__icontains=search))
                for query in queries:
                    posts.append(query)

            if body=='on':
                queries = rssdata.objects.filter(Q(body__icontains=search))
                for query in queries:
                    posts.append(query)
            if source=='on':
                queries = rssdata.objects.filter(Q(source__icontains=search))
                for query in queries:
                    posts.append(query)

            if (death_no=='on' or flag == 1):
                queries = rssdata.objects.filter(Q(death_no__iexact=int(search)))
                for query in queries:
                    posts.append(query)
            
            if location=='on':
                queries = rssdata.objects.filter(Q(location__icontains=search))
                for query in queries:
                    posts.append(query)

            if (injury_no=='on' and flag == 1):
                queries = rssdata.objects.filter(Q(injury_no__iexact=int(search)))
                for query in queries:
                    posts.append(query)

            if date=='on':
                queries = rssdata.objects.filter(Q(date__iexact=search))
                for query in queries:
                    posts.append(query)

            if (year=='on' or flag == 1):
                queries = rssdata.objects.filter(Q(year__iexact=int(search)))
                for query in queries:
                    posts.append(query)

            if day=='on':
                queries = rssdata.objects.filter(Q(day__icontains=search))
                for query in queries:
                    posts.append(query)
            if month=='on':
                queries = rssdata.objects.filter(Q(month__icontains=search))
                for query in queries:
                    posts.append(query)
        
        posts= list(set(posts))

        context ={}
        context['form']= SearchForm()
        context['posts']=posts
        context['search'] =search

        return render(request, 'newsextraction/search.html', context)
    
    else:
        context ={}
        context['form']= SearchForm()
        return render(request, 'newsextraction/search.html', context)





def extraction(request):
	return render(request, 'newsextraction/extraction.html', {'isHome':False})


def about_us(request):
	return render(request, 'about_us.html')


def contact_us(request):
	return render(request, 'contact_us.html')

def searchquery(request):
	if request.POST:
		query = request.POST.get('query', None)
		querylist = rssdata.objects.values('body').filter(Q(body__icontains=query))

		return render(request, 'searchquery.html',{'searchquery':querylist,
													'query':query,})