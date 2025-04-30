from django.urls import path
from .views import faculty, courses, events, index, CourseDetailView, ContactView, EventDetailView

urlpatterns = [
    path('faculties/', faculty, name='faculties'),
    path('courses/', courses, name='courses'),
    path('events/', events, name='events'),
    path('event_detail/', events, name='event_detail'),
    path('templates/main/index/', index, name='index'),
    path('', index, name='index'),
    path('course/<slug:course_slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('event/<slug:event_slug>/', EventDetailView.as_view(), name='event_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    # Add other paths for your views if needed
]
