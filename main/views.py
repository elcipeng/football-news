from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406406742',
        'name': 'Justin Dwitama Seniang',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
