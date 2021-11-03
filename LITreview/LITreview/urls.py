"""LITreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import redirect
from django.urls import path

import authentication.views
import flux.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', authentication.views.login_page, name='login'),                  # Login page by function
    # path('', authentication.views.LoginPageView.as_view(), name='login'),     # Login page by class
    path('', LoginView.as_view(
        template_name='authentification/login.html',
        redirect_authenticated_user=True),
        name='login'),                                                          # Login page by generic view
    # path('logout/', authentication.views.logout_user, name='logout'),         # Logout page by function
    path('logout/', LogoutView.as_view(), name='logout'),                       # Logout page by generic
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentification\password_change_form.html'),
        name='password_change'
    ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentification/password_change_done.html'),
        name='password_change_done'
    ),
    path('signup', authentication.views.signup_page, name='signup'),
    path('home/', flux.views.home, name="home"),
    path('review/upload/', flux.views.review_upload, name='review_upload'),
    path('ticket/upload/', flux.views.ticket_upload, name='ticket_upload'),
    path('review/create/', flux.views.ticket_and_review_upload, name='review_create'),
    path('review/<int:review_id>', flux.views.view_review, name='view_review'),
    path('review/<int:ticket_id>', flux.views.view_ticket, name='view_ticket'),
    path('review/<int:review_id>/edit',
         flux.views.edit_review, name='edit_review'),
    path('ticket/<int:ticket_id>/edit',
         flux.views.edit_ticket, name='edit_ticket'),
    path('follow-users/', flux.views.follow_users, name='follow_users')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
