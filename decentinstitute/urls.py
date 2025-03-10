"""
URL configuration for decentinstitute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    #courses page
    path('course_detail.html/', views.course_details , name="course detail"),
    path('courses/', views.all_courses, name='courses'),
    path('tally/', views.tally_prime , name="tally_prime"),
    path('advance_excel/', views.advance_excel , name="advnce_excel"),
    path('DFM/', views.dfm , name="DFM"),
    path('ccc/', views.ccc , name="ccc"),
    path('dtp/', views.dtp , name="dtp"),
    path('graphic-design/', views.graphic , name="graphic design"),
    path('web-development/', views.webdev1 , name="webdev1"),
    path('Advance-web-development/', views.webdev2 , name="webdev2"),
    path('Python/', views.python , name="python"),
    path('Digital Marketing/', views.dm , name="Digital Marketing"),
    path('Data Science & Analytics With Power BI/', views.datascie , name="Data Science"),
    path('Database Management System/', views.dbms , name="Database Management System"),
    path('Diploma in Google SketchUp/', views.google_sketchup , name="Diploma in Google SketchUp"),
    path('Diploma in Hardware & Networking/', views.hardware , name="Diploma in Hardware & Networking"),
    path('AutoCAD/', views.autocad , name="AutoCAD"),
    path('Awareness in Computer Concepts (ACC)/', views.ACC , name="ACC"),
    path('Certified Data Entry Operator/Call Center Executive/', views.data_entry , name="data entry"),
    path('Spoken English Course', views.spoken , name="spoken english"),


    #static 
    path('reviews/', views.review_page, name='reviews'), 
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_view, name='contact'),
    
    # path('course/<int:course_id>/', views.course_detail, name='course_detail'),#dynamically add course 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)