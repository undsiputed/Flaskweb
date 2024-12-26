from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'deb458746@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'gkmm nkvb ziqh kcrl'  # Replace with your App Password

mail = Mail(app)

# Example job list
JOBS = [
    {'id': 1, 'title': 'Frontend Developer'},
    {'id': 2, 'title': 'Backend Developer'},
    {'id': 3, 'title': 'Full Stack Engineer'},
    {'id': 4, 'title': 'Data Scientist'},
    {'id': 5, 'title': 'Mobile App Developer'},
    {'id': 6, 'title': 'DevOps Engineer'},
    {'id': 7, 'title': 'Cybersecurity Analyst'},
    {'id': 8, 'title': 'Machine Learning Engineer'},
    {'id': 9, 'title': 'Cloud Architect'},
    {'id': 10, 'title': 'UI/UX Designer'},
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    # Find job by ID
    job = next((job for job in JOBS if job['id'] == job_id), None)
    if not job:
        return "Job not found", 404

    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        # Send confirmation email
        send_email(name, email, job['title'])

        # Render success page
        return render_template('application_success.html', name=name, job_title=job['title'])

    return render_template('application.html', job=job)

def send_email(name, recipient_email, job_title):
    """Send a confirmation email."""
    subject = f"Application Confirmation for {job_title}"
    body = f"""
    Dear {name},

    Thank you for applying for the {job_title} position! 
    We have received your application and our team will review it shortly.

    🎉 What's Next:
    - Our recruitment team will carefully assess your profile.
    - We will contact you if you're shortlisted.
    - Meanwhile, explore more opportunities on our portal!

    Best Regards,  
    The Careers Team
    """

    msg = Message(subject=subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
    msg.body = body
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
