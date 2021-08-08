from newsextraction.modules.utils import initial_check
from newsextraction.modules.utils import *
from newsextraction.modules import newstotext
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import NameForm
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




def extraction(request):
	linkForm = NameForm()
	if request.method == 'POST':
		linkForm = NameForm(request.POST)
		if(linkForm.is_valid()):
			title, story, link = newstotext.story_extract(linkForm.cleaned_data['news_link'])
			return render(request, 'newsextraction/extraction.html', {'isHome':False, 'form':linkForm})
	return render(request, 'newsextraction/extraction.html', {'isHome':False, 'form':linkForm})


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