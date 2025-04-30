from django.shortcuts import get_object_or_404, render,redirect
from .models import Faculty,Course,Event
from django.views import View
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    faculties=Faculty.objects.all()
    courses = Course.objects.all()
    return render(request,'main/index.html',{'faculties': faculties ,'courses': courses})


def faculty(request):
    faculties = Faculty.objects.all()
    return render(request, 'main/faculty.html', {'faculties': faculties})


def courses(request):
    courses = Course.objects.all()
    return render(request, 'main/courses.html', {'courses': courses})

def events(request):
    events = Event.objects.all()
    return render(request, 'main/events.html', {'events': events})


class CourseDetailView(View):
    template_name = 'main/course_detail.html'

    def get(self, request, course_slug):
        course = get_object_or_404(Course, Course_slug=course_slug)
        return render(request, self.template_name, {'course': course})

class EventDetailView(View):
    template_name = 'main/event_detail.html'

    def get(self, request, event_slug):
        event = get_object_or_404(Event, Event_slug=event_slug)
        return render(request, self.template_name, {'event': event})

class ContactView(View):
    template_name = 'main/contact.html'

    def get(self, request, *args, **kwargs):
        # Render the contact form on a GET request
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Get form data from POST request
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Construct email message
        email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        # Send email using the configured email settings
        send_mail(
            'Contact Form Submission',
            email_message,
            settings.EMAIL_FROM,  # Use the configured sender email
            ['vaatsalya.app@gmail.com'],  # List of recipient email addresses
            fail_silently=False,
        )

        # Redirect after successful form submission
        return redirect('contact')