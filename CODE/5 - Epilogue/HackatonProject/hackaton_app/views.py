from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Post

class Pages:
	def home(request) -> object:
		return render(request, 'hackaton_app/index.html')

	#####################
	### ITALIAN PAGES ###
	#####################
	def problem(request) -> object:
		return render(request, 'hackaton_app/problems.html') 
	def solution(request) -> object:
		return render(request, 'hackaton_app/solutions.html') 

	def about(request) -> object:
		return render(request, 'hackaton_app/about.html')
	
	def post(request) -> object:
		data = {
			'posts': Post.objects.all()
		}
		return render(request, 'hackaton_app/forum.html', data)

# Necessarly for the post creation form
class PostCreate (CreateView):
	model = Post
	fields = ['author', 'content']
	template_name = 'hackaton_app/create.html'
	def form_valid(self, form):
		form.save()
		return redirect('post forum')
