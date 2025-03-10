from django.shortcuts import render, redirect ,get_object_or_404
from .models import Review, Contact , Course
from .forms import ReviewForm, ContactForm
from django.http import HttpResponse ,JsonResponse
from django.template import loader
from django.contrib import messages 

def index(request):
    # Fetch reviews and courses
    reviews = Review.objects.all().order_by('-created_at')
    courses = Course.objects.all()  # Fetch all courses from DB

    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if 'review_form' in request.POST:  # Handle Review Form
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                new_review = review_form.save()
                return JsonResponse({
                    'success': True,
                    'message': "Your review has been submitted successfully!",
                    'review': {
                        'name': new_review.name,
                        'review': new_review.review,
                        'initial': new_review.name[0].upper(),
                    }
                })
            return JsonResponse({'success': False, 'message': "Error submitting review."})

        elif 'contact_form' in request.POST:  # Handle Contact Form
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return JsonResponse({'success': True, 'message': "Your message has been sent successfully!"})
            return JsonResponse({'success': False, 'message': "Error submitting message."})

    else:
        review_form = ReviewForm()
        contact_form = ContactForm()

    return render(request, 'index.html', {
        'reviews': reviews,
        'review_form': review_form,
        'contact_form': contact_form,
        'courses': courses,  # Pass courses to template
    })

def review_page(request):
    reviews = Review.objects.all().order_by('-created_at')  # Get all reviews, ordered by creation date

    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        review_form = ReviewForm(request.POST)  # Get the form data from the POST request
        if review_form.is_valid():  # If the form is valid
            new_review = review_form.save()  # Save the review to the database
            # Return a JSON response with the success message and the new review data
            return JsonResponse({
                'success': True,
                'message': "Your review has been submitted successfully!",
                'review': {
                    'name': new_review.name,
                    'review': new_review.review,
                    'initial': new_review.name[0].upper(),
                }
            })
        return JsonResponse({'success': False, 'message': "Error submitting review."})

    else:
        review_form = ReviewForm()  # If not a POST request, create a new empty form

    # Render the reviews page, passing in the reviews and review form
    return render(request, 'reviews.html', {'reviews': reviews, 'review_form': review_form})

# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)  
#     return render(request, 'course_detail.html', {'course': course}) 



def course_details(req):
    course_details = loader.get_template('course_detail.html')
    return HttpResponse(course_details.render()) #static view for course detail


# all courses page 
def all_courses(req):
    return render(req, 'courses.html') 

def tally_prime(req):
    return render(req , 'Tally_Prime.html')

def advance_excel(req):
    return render(req, 'advance_excel.html')  

def dfm(req):
    return render(req, 'DFM.html')  

def ccc(req):
    return render(req, 'ccc.html')  

def dtp(req):
    return render(req, 'dtp.html') 

def about_us(req):
    return render(req, 'about.html')   

def graphic(req):
    return render(req, 'graphic.html')  

def webdev1(req):
    return render(req, 'webdev1.html')  

def webdev2(req):
    return render(req, 'webdev2.html')  


def python(req):
    return render(req, 'python.html')  

def dm(req):
    return render(req, 'digitalmarketing.html')  

def datascie(req):
    return render(req, 'data_sci_analytics_powerbi.html')  

def dbms(req):
    return render(req, 'dbms.html') 

def google_sketchup(req):
    return render(req, 'google_sketchup.html') 

def hardware(req):
    return render(req, 'hardware.html') 

def autocad(req):
    return render(req, 'autocad.html') 

def ACC(req):
    return render(req, 'acc.html') 

def data_entry(req):
    return render(req, 'data_entry.html') 

def spoken(req):
    return render(req, 'spoken_english.html') 


def contact_view(request):
    Contact.objects.all()
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return JsonResponse({'success': True, 'message': "Your message has been sent successfully!"})
        return JsonResponse({'success': False, 'message': "Error submitting message."})
    
    else:
        contact_form = ContactForm()

    return render(request, 'contact.html', {'contact_form': contact_form})
