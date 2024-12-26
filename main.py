from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message
from database import create_connection, execute_query, fetch_results
from werkzeug.utils import secure_filename
import os
# Import database functions

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with an app-specific password

mail = Mail(app)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Function to fetch jobs dynamically from the database
def get_jobs_from_db():
    connection = create_connection()
    if not connection:
        print("Failed to connect to the database")
        return []

    select_query = "SELECT id, title, location, salary_range, image_url, requirements, responsibilities FROM jobs;"
    jobs = fetch_results(connection, select_query)
    connection.close()

    # Convert jobs to a dictionary format for rendering
    jobs_list = []
    for job in jobs:
        jobs_list.append({
            'id': job[0],
            'title': job[1],
            'location': job[2],
            'salary': job[3],
            'image': job[4],
            'requirements': eval(job[5]),  # Assuming requirements are stored as a JSON string
            'responsibilities': eval(job[6])  # Assuming responsibilities are stored as a JSON string
        })
    return jobs_list

# Home route
@app.route("/")
def hello():
    jobs = get_jobs_from_db()  # Fetch jobs from the database
    return render_template("home.html", jobs=jobs)

# Route for the application form
@app.route('/apply/<int:job_id>', methods=['GET'])
def apply(job_id):
    # Fetch the job details based on job_id
    job = next((job for job in get_jobs_from_db() if job['id'] == job_id), None)
    if not job:
        return "Job not found", 404

    # Render the application form with job details
    return render_template('application.html', job=job)

# Route to handle form submission
@app.route('/submit-application', methods=['POST'])
def submit_application():
    form_data = request.form
    name = form_data['name']
    email = form_data['email']
    phone = form_data['phone']
    job_id = int(form_data['job_id'])
    internships = form_data.get('internships', None)
    portfolio_url = form_data.get('portfolio', None)
    linkedin_url = form_data.get('linkedin', None)
    github_url = form_data.get('github', None)

    # Save resume if uploaded
    if 'resume' in request.files:
        resume = request.files['resume']
        if resume.filename != '':
            filename = secure_filename(resume.filename)
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume.save(resume_path)
        else:
            resume_path = None
    else:
        resume_path = None

    # Save the application data to the database
    connection = create_connection()
    if connection:
        insert_query = f"""
        INSERT INTO applications (job_id, name, email, phone, internships, portfolio_url, linkedin_url, github_url, resume_url)
        VALUES ({job_id}, '{name}', '{email}', '{phone}', '{internships}', '{portfolio_url}', '{linkedin_url}', '{github_url}', '{resume_path}');
        """
        execute_query(connection, insert_query)
        connection.close()

    # Find the job title
    job = next((job for job in get_jobs_from_db() if job['id'] == job_id), None)
    job_title = job['title'] if job else "Unknown Job"

    # Send confirmation email
    send_email(name, email, job_title)

    return render_template("application_success.html", name=name, job_title=job_title)
# View applications route
@app.route('/applications', methods=['GET'])
def view_applications():
    conn = create_connection()
    if conn:
        query = """
        SELECT a.id, a.name, a.email, a.phone, j.title AS job_title, a.internships, 
               a.portfolio_url, a.resume_url
        FROM applications a
        INNER JOIN jobs j ON a.job_id = j.id;
        """
        applications = fetch_results(conn, query)
        conn.close()
        return render_template('applications.html', applications=applications)
    else:
        return "Database connection failed", 500

# Function to send confirmation email
def send_email(name, recipient_email, job_title):
    try:
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
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    print("Starting Flask application...")
    app.run(host="0.0.0.0", port=8080, debug=True)




