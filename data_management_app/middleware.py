from django.shortcuts import redirect
from django.urls import reverse

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Redirect to the login page
            return redirect(reverse('login'))

        # Check if the user is a superuser
        if not request.user.is_superuser:
            # Redirect to a custom error page or just the homepage
            return redirect(reverse('error'))

        response = self.get_response(request)
        return response





class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('is_logged_in'):
            # User is not logged in, redirect to login page
            return redirect(reverse('login'))

        response = self.get_response(request)

        return response
