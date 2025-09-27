from django.urls import path

from .views import sitemapPage, homePage, booksPage, tutoPage, tutorialsPage, gradePage, biologyPage, chemistryPage, englishPage, mathematicsPage, physicsPage, videosPage, podcastsPage, smartifyPage, smartifyDetailsPage, aboutPage, networkErrorPage

urlpatterns = [
    path('', homePage, name='homePage'),
    path('books/', booksPage, name='booksPage'),
    path('tutorial/', tutoPage, name='tutoPage'),
    path('tutorials/', tutorialsPage, name='tutorialsPage'),
    path('grade/', gradePage, name='gradePage'),
    path('biology/', biologyPage, name='biologyPage'),
    path('chemistry/', chemistryPage, name='chemistryPage'),
    path('english/', englishPage, name='englishPage'),
    path('mathematics/', mathematicsPage, name='mathematicsPage'),
    path('podcasts/', podcastsPage, name='podcastsPage'),
    path('physics/', physicsPage, name='physicsPage'),
    path('videos/', videosPage, name='videosPage'),
    path('smartify/', smartifyPage, name='smartifyPage'),
    path('smartifyData/<int:id>/', smartifyDetailsPage, name='smartifyDetailsPage'),
    path('about/', aboutPage, name='aboutPage'),
    path('networkError/', networkErrorPage, name='networkErrorPage'),
    path('sitemap.txt/', sitemapPage, name="sitemapPage")
]