from os import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import FormMixin

from . import forms
from . import models

# Create your views here.


@login_required
def home(request):
    reviews = models.Review.objects.all()
    tickets = models.Ticket.objects.all()
    return render(request, 'flux/home.html', context={'reviews': reviews, 'tickets': tickets})


@login_required
def review_upload(request):
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # Set the user before upload
            review.user = request.user

            # Now we save
            review.save()
            return redirect('home')
    return render(request, 'flux/review_upload.html', context={'form': form})


@login_required
def ticket_upload(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'flux/ticket_upload.html', context={'form': form})


@login_required
def ticket_and_review_upload(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            redirect('home')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'flux/create_review_post.html', context=context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'flux/view_review.html', {'review': review})


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Review, id=ticket_id)
    return render(request, 'flux/view_ticket.html', {'ticket': ticket})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home.html')
            if 'delete_blog' in request.POST:
                delete_form = forms.DeleteReviewForm(request.POST)
                if delete_form.is_valid():
                    review.delete()
                    return redirect('home.html')

    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'flux/edit_review.html', context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
    context = {
        'edit_form': edit_form,
}
    return render(request, 'flux/edit_ticket.html', context=context)

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    # delete_form = forms.DeleteTicketForm()
    ticket.delete()
    return redirect('home')
    # if request.method == 'POST':
    #     if delete_form in request.POST:
    #         delete_form = forms.DeleteTicketForm(request.POST)
    #         if delete_form.is_valid():
    #             ticket.delete()
    #             return redirect('home')
            
    # context = {'delete_form': delete_form,}
    # return render(request, 'flux/delete_ticket.html', context=context)
    

@login_required
def follow_users(request, user_id):
    
    # form = forms.FollowUserForm(instance=request.user)
    # print('request', request)
    # if request.method == 'POST':
    #     form = forms.FollowUserForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         followed = form.save(commit=False)
    #         followed.user = request.user
    #         followed.followed_user = request.followed_user
    #         followed.save()
    #         return redirect('home')

    return render(request, 'flux/follow_user_form.html', context={'form': form})
