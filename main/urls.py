from django.urls import path
from .views import faculty, courses, events,index,CourseDetailView,ContactView

urlpatterns = [
    path('faculties/', faculty, name='faculties'),
    path('courses/', courses, name='courses'),
    path('events/', events, name='events'),
    path('index/', index, name='index'),
    path('', index, name='index'),
    path('course/<slug:course_slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    # Add other paths for your views if needed
]
