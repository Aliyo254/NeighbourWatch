from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import NewNeighbourhoodForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = current_user
            neighbourhood.save()
        return redirect('Home')

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})