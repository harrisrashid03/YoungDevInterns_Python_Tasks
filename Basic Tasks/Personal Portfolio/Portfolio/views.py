from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

# Views for the Portfolio

def home(request):
    return render(request, 'home.html', {
        'name': "Muhammad Harris Rashid",
        'summary': "Biotechnologist with a solid background in molecular biology, currently pursuing a Bachelor of Science in Biotechnology."
    })

def skills(request):
    skills = [
        "Molecular Biology Techniques",
        "Python Development",
        "Data Analysis and Visualization using R, SPSS, and Power BI",
        "Scientific Writing and Communication",
        "Machine Learning Applications",
    ]
    return render(request, 'skills.html', {'skills': skills})

def experience(request):
    experiences = [
        {
            'role': "Intern",
            'duration': "Jul 2024 - Aug 2024",
            'organization': "University of Veterinary and Animal Sciences (UVAS), Lahore, Pakistan",
            'details': [
                "Gained hands-on experience in molecular biology and cell culture techniques.",
                "Conducted RT-PCR experiments.",
                "Developed skills in genotyping and molecular analysis.",
            ]
        },
        {
            'role': "Python Developer",
            'duration': "Apr 2024 - May 2024",
            'organization': "YoungDev Intern, Lahore, Pakistan",
            'details': [
                "Developed visually appealing resume templates for end-users in Python.",
                "Created and visualized trigonometric functions (sine and cosine graphs).",
            ]
        },
    ]
    return render(request, 'experience.html', {'experiences': experiences})

def publications(request):
    publications = [
        {
            'title': "Spatio-Temporal Analysis of High Pathogenic Avian Influenza outbreaks reveal persistent and emerging subtypes.",
            'journal': "Journal of Epidemiology and Infection Biology",
            'year': 2024,
            'link': "https://jepibio.com/wp-content/uploads/2024/11/07_final_spatial_clustering.pdf"
        }
    ]
    return render(request, 'publications.html', {'publications': publications})

def certifications(request):
    certifications = [
        "ICH GOOD CLINICAL PRACTICE E6 (R2)",
        "R Language (Issued: July 2024)",
        "IBM Certified Specialist – SPSS (Issued: July 2023)",
        "Analyzing and Visualizing data with Microsoft Power BI (Issued: July 2023)",
    ]
    return render(request, 'certifications.html', {'certifications': certifications})

def education(request):
    education = [
        {
            'degree': "BSc (Hon.) Biotechnology",
            'year': "2021 – 2025",
            'institution': "Forman Christian College University, Lahore, Pakistan"
        },
        {
            'degree': "Intermediate – Pre-Medical",
            'year': "2019 – 2021",
            'institution': "Government College University (GCU), Lahore, Pakistan"
        }
    ]
    return render(request, 'education.html', {'education': education})

def contact(request):
    contact_info = {
        'email': "harrisrashid03@gmail.com",
        'phone': "+923058111785",
        'linkedin': "http://www.linkedin.com/in/muhammad-harris-rashid-ab49b123a",
    }
    return render(request, 'contact.html', {'contact_info': contact_info})

# URL Configuration

urlpatterns = [
    path('', home, name='home'),
    path('skills/', skills, name='skills'),
    path('experience/', experience, name='experience'),
    path('publications/', publications, name='publications'),
    path('certifications/', certifications, name='certifications'),
    path('education/', education, name='education'),
    path('contact/', contact, name='contact'),
]

# Templates

# home.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Muhammad Harris Rashid</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container text-center mt-5">
        <h1>Welcome to My Portfolio</h1>
        <p>{{ summary }}</p>
    </div>
</body>
</html>
"""

# skills.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skills - Muhammad Harris Rashid</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Skills</h2>
        <ul>
            {% for skill in skills %}
                <li>{{ skill }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

# experience.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Experience - Muhammad Harris Rashid</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h2>Experience</h2>
        {% for exp in experiences %}
        <div class="mb-4">
            <h4>{{ exp.role }} ({{ exp.duration }})</h4>
            <p><strong>Organization:</strong> {{ exp.organization }}</p>
            <ul>
                {% for detail in exp.details %}
                    <li>{{ detail }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

# Similar templates for publications.html, certifications.html, education.html, and contact.html can be created following this structure.
