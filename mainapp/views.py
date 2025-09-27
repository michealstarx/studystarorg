import requests
from requests.exceptions import ConnectionError
from django.shortcuts import render, redirect



def homePage(request):
    return render(request, 'mainapp/home.html')
def booksPage(request):
    return render(request, 'mainapp/books.html')
def gradePage(request):
    return render(request, 'mainapp/grade.html')
def tutorialsPage(request):
    return render(request, 'mainapp/tutorials.html')
def tutoPage(request):
    return render(request, 'mainapp/tuto.html')
def videosPage(request):
    return render(request, 'mainapp/videos.html')
def podcastsPage(request):
    return render(request, 'mainapp/podcasts.html')
def smartifyPage(request):
    api_url = "https://michealzsd.pythonanywhere.com/List/"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        data.reverse()
    except ConnectionError:
        # Redirect to a custom error page or home page
        return redirect('networkErrorPage')  # use URL pattern name or path here
    except requests.exceptions.HTTPError:
        # Handle other HTTP errors if needed
        data = []
    except Exception:
        data = []


    return render(request, 'mainapp/smartify.html', {'api_data': data})

def smartifyDetailsPage(request, id):
    url = f'https://michealzsd.pythonanywhere.com/Data/{id}'
    response = requests.get(url)
    data = response.json()

    
    return render(request, 'mainapp/smartifyDetails.html', {'item': data})


def aboutPage(request):
    return render(request, 'mainapp/about.html')
def biologyPage(request):
    return render(request, 'mainapp/biology.html')
def chemistryPage(request):
    return render(request, 'mainapp/chemistry.html')
def englishPage(request):
    return render(request, 'mainapp/english.html')
def mathematicsPage(request):
    return render(request, 'mainapp/mathematics.html')
def physicsPage(request):
    return render(request, 'mainapp/physics.html')
def networkErrorPage(request):
    return render(request, 'mainapp/networkErrorPage.html')

def sitemapPage(request):
    return render(request, 'mainapp/sitemap.txt')