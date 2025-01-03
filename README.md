Dev Careers Job Portal
Welcome to the Dev Careers Job Portal, a platform that connects developers with the best job opportunities tailored to their skills. This project showcases a dynamic job application system integrated with a MySQL database and a Flask backend.

Features
🎯 Core Features
Dynamic job listings retrieved from the MySQL database.
Job application form with advanced fields for candidates.
Resume upload functionality.
Email notification upon successful job application.
Search functionality for jobs based on keywords and location.
📋 Admin Features
View all submitted applications.
Manage job listings and candidate data.
🎨 Frontend Features
Responsive and interactive UI designed for ease of use.
Clean and intuitive layout for job seekers.
Interactive buttons for signing in, creating accounts, and adding favorites.
Technologies Used
Backend
Python: Core programming language.
Flask: Lightweight web framework for routing and handling requests.
MySQL: Relational database for storing job and application data.
Frontend
HTML/CSS: Markup and styling.
Bootstrap (optional): For responsive design.
Flask Templates: To dynamically render job and application data.
Other Tools
Werkzeug: For secure file uploads.
Flask-Mail: For sending email notifications.
Pycharm: IDE for development.
Git/GitHub: Version control and repository hosting.
Setup Instructions
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/dev-careers-portal.git
cd dev-careers-portal
Step 2: Set Up Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Configure the Database
Create a MySQL database using the name devcareers.
Update the database credentials in database.py:
python
Copy code
connection = mysql.connector.connect(
    host='your-database-host',
    database='devcareers',
    user='your-username',
    password='your-password'
)
Step 5: Run Database Scripts
Open your MySQL workbench.
Execute the scripts to create the jobs and applications tables.
Populate the jobs table with sample data.
Step 6: Run the Application
bash
Copy code
python main.py
The application will be accessible at: http://127.0.0.1:8080

Folder Structure
php
Copy code
dev-careers-portal/
│
├── static/
│   ├── styles.css         # Custom styles
│   ├── uploads/           # Uploaded resumes
│   └── images/            # Static images
│
├── templates/
│   ├── home.html          # Homepage
│   ├── application.html   # Job application form
│   ├── applications.html  # Admin view for applications
│   └── application_success.html  # Success page
│
├── database.py            # Database connection and helper functions
├── main.py                # Core Flask application
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
└── .gitignore             # Files to ignore in version control
How It Works
Job Listings
Jobs are dynamically fetched from the MySQL database.
Each job includes details such as title, location, salary, requirements, and responsibilities.
Job Application
Candidates can apply for jobs through a detailed form.
Resumes are securely uploaded and stored in the /static/uploads directory.
Applications are saved in the applications table in the database.
Admin View
Admins can:

View all submitted applications.
Search for applications based on job titles.
Screenshots
Homepage

Job Application Form

Admin Applications View

Future Enhancements
Add user authentication for both job seekers and admins.
Implement job posting functionality for recruiters.
Integrate third-party APIs for job search (e.g., LinkedIn, Indeed).
Add analytics for tracking applications.
Contributing
Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit changes: git commit -m 'Add feature'.
Push to the branch: git push origin feature-name.
Submit a pull request.
License
This project is licensed under the MIT License.
