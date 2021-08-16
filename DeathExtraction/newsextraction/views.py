from newsextraction.modules.utils import initial_check
from newsextraction.modules.utils import *
from newsextraction.modules import newstotext
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, response
from newsextraction.modules.locationTree import LocationInformation
from .forms import NameForm,SearchForm
from .models import *
from .methods import *
from django.db.models import Q #object used to encapsulate a collection of keyword arguments specified as in “Field lookups”.

def index(request):
	initial_check()
	news_list = rssdata.objects.all().order_by("-date")
	return render(request, 'newsextraction/index.html', {
			'newsList': list(news_list),
			'isHome':True,
		}
	)




def extraction(request):
	linkForm = NameForm()
	if request.method == 'POST':
		linkForm = NameForm(request.POST)
		if(linkForm.is_valid()):
			title, story, link = newstotext.story_extract(linkForm.cleaned_data['news_link'])
			print(title, story, link,sep="\n")
			newsData = extract(link, story, title, "", "", False)	
			return render(request, 'newsextraction/extraction.html', {'isHome':False, 'form':linkForm, 'isData':True, 'news':newsData})
	return render(request, 'newsextraction/extraction.html', {'isHome':False, 'form':linkForm, 'isData':False})


def graph(request):
	alllocationlist, ktmlocationlist, ltplocationlist, bktlocationlist, outsideLocationList, locationCount = getLocations()	
	deathCount = getDeathCountLocation()
	context = {
		'allLocation': alllocationlist,
		'locationCount': locationCount,
		'deathCount': deathCount
	}
	return render(request, 'newsextraction/visualization.html', context=context) 



def searchView(request):
    

    checks=[]
    posts=[]
    queries=[]




    if request.method == 'POST':
        form = SearchForm(data=request.POST)
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
        search_text = request.POST.get('sname')

        
        

        if search_main != None:
            search=search_main

            SearchForm.all=True
            form= SearchForm
            all='on'
            
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

            if (year=='on' and flag == 1):
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
        context['form']= form
        context['posts']=posts
        context['search'] =search

        return render(request, 'newsextraction/search.html', context)
    
    else:
        
        
        print("bbb")
        context ={}
        context['form']= SearchForm()
        return render(request, 'newsextraction/search.html', context)







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