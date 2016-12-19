from django.shortcuts import render
from . import models

# Create your views here.
def post_list(request):

	return render(request,'myblog/post_list.html',{})