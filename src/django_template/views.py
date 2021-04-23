from django.shortcuts import render

# Create your views here.
def home_view(request):
    food = "Bread"
    return render(
        request,
        "home.html",
        {"food":food}
    )
