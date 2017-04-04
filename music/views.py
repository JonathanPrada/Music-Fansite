from django.views import generic
# Enable forms
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# For user authentication
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Album
from .forms import UserForm


# Create a list view
class IndexView(generic.ListView):
    # When we get a list of albums, plug them here
    template_name = 'music/index.html'
    # Albums will get passed as object_list, rename here
    context_object_name = 'all_albums'

    # Queryset, query the db for the albums
    def get_queryset(self):
        return Album.objects.all()


# Create the details views
class DetailView(generic.DetailView):
    # Describe the model we are getting details from
    model = Album
    # When we get the album detail, plug details here
    template_name = 'music/detail.html'


# Create model form for adding
class AlbumCreate(CreateView):
    model = Album
    fields = [
        'artist',
        'album_title',
        'genre',
        'album_logo'
    ]


# Create model form for update
class AlbumUpdate(UpdateView):
    model = Album
    fields = [
        'artist',
        'album_title',
        'genre',
        'album_logo'
    ]


# Create model form for deleting
class AlbumDelete(DeleteView):
    model = Album
    # Redirect url
    success_url = reverse_lazy('music:index')


# Create the actual user form
class UserFormView(View):
    # Assign the blue print for the class
    form_class = UserForm
    # Specify the html file the form will be included in
    template_name = 'music/registration_form.html'

    # Built in function for get request
    # Display blank form
    def get(self, request):
        # Set it to the form we made in forms.py, don't pass nothing in
        form = self.form_class(None)
        # Render the form assigned to the template we assigned above
        return render(request, self.template_name, {'form': form})

    # Built in function for get request
    # Process form data
    def post(self, request):
        # When submit gets pressed, it gets stored in request.POST
        form = self.form_class(request.POST)

        # Validate the form data
        if form.is_valid():
            # Store the information locally to check on it
            user = form.save(commit=False)

            # Cleaned data, formatted properly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Set the password accordingly
            user.set_password(password)
            # Actually save it into the database
            user.save()

            # return user objects if credentials are correct
            # Takes username and password and checks against db if exists
            user = authenticate(username=username, password=password)

            # If user exists
            if user is not None:

                if user.is_active:
                    # Log them in
                    login(request, user)
                    # Access the details request.user.username
                    return redirect('music:index')

        # If user did not manage to log in then redirect back to form
        return render(request, self.template_name, {'form': form})


# Log the user out
def logout_view(request):
    logout(request)

