from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def home(request):
    return render(request, 'flux/home.html')

# @login_required
# def blog_and_photo_upload(request):
#     blog_form = forms.BlogForm()
#     if request.method == "POST":
#         context = {
#             'blog_form': blog_form,
#         }
#     return render(request, 'blog/create_blog_post.html', context=context)