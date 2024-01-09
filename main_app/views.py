from django.shortcuts import render
finches = [
  {'name': 'Willow', 'breed': 'bird', 'gender': 'female', 'color': 'red'},
  {'name': 'Jazzy', 'breed': 'bird', 'gender': 'female', 'color': 'yellow'},
  {'name': 'Sam', 'breed': 'bird', 'gender': 'male', 'color': 'blue'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def all_finches(request):
    return render(request, 'finches/all_finches.html', {'finches': finches})

