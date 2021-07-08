from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):


  title = 'Netflix | Home'

  search_movie = request.args.get('movie_query')

  if search_movie:
    return redirect('search')

  else:
    return render(request,'index.html')