from django.db import models
# Review model
class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    COURSES = [
        ("web_dev_1", "Web Development Course - 1"),
        ("adv_web_tech_2", "Advanced Web Technology Course - 2"),
        ("python_prog", "Python Programming Course"),
        ("digital_marketing", "Diploma in Digital Marketing"),
        ("data_science_powerbi", "Data Science & Analytics with Power BI"),
        ("autoCAD", "AUTOCAD"),
        ("tally_gst", "Tally Prime with GST"),
        ("adv_excel", "Advanced Excel"),
        ("financial_mgmt", "Diploma in Financial Management"),
        ("cert_computer", "Certificate Course in Computer"),
        ("cert_dtp", "Certificate in DTP (Desktop Publishing)"),
        ("graphic_design", "Diploma in Graphic Designing"),
        ("dbms", "Database Management System (DBMS)"),
        ("sketchup", "Diploma in Google SketchUp"),
        ("hardware_and_networking", "Diploma Hardware & Networking"),
        ("acc", "Awareness in Computer Concepts"),
        ("data-entry", "Certified Data Entry Operator/Call Center Executive"),
        ("spoken_english", "Spoken English Course"),



    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    intrested_course = models.CharField(max_length=50, choices=COURSES, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.first_name} {self.last_name}"

    
class Course(models.Model):
    title = models.CharField(max_length=255)
    institute_name = models.CharField(max_length=255, default="Decent Institute")
    short_description = models.TextField(default="No short description available.")  # ✅ Default value added
    full_description = models.TextField(default="Full course details coming soon.")  # ✅ Default value added
    additional_info = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/', default='courses/default.jpg')

    def __str__(self):
        return self.title
