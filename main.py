from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 101,
    'title': 'Frontend Developer',
    'location': 'New York, NY',
    'salary': '$85,000 - $110,000'
}, {
    'id': 102,
    'title': 'Backend Developer',
    'location': 'San Francisco, CA',
    'salary': '$95,000 - $130,000'
}, {
    'id': 103,
    'title': 'Full Stack Engineer',
    'location': 'Austin, TX',
    'salary': '$90,000 - $120,000'
}, {
    'id': 104,
    'title': 'Data Scientist',
    'location': 'Seattle, WA',
    'salary': '$110,000 - $150,000'
}, {
    'id': 105,
    'title': 'Mobile App Developer',
    'location': 'Chicago, IL',
    'salary': '$80,000 - $105,000'
}, {
    'id': 106,
    'title': 'DevOps Engineer',
    'location': 'Denver, CO',
    'salary': '$100,000 - $140,000'
}, {
    'id': 107,
    'title': 'Cybersecurity Analyst',
    'location': 'Washington, DC',
    'salary': '$95,000 - $125,000'
}, {
    'id': 108,
    'title': 'Machine Learning Engineer',
    'location': 'Boston, MA',
    'salary': '$120,000 - $160,000'
}, {
    'id': 109,
    'title': 'Cloud Architect',
    'location': 'Remote',
    'salary': '$115,000 - $150,000'
}, {
    'id': 110,
    'title': 'UI/UX Designer',
    'location': 'Los Angeles, CA',
    'salary': '$75,000 - $100,000'
}]


@app.route("/")
def hello():
    print(__name__
          )  # This will print the module name when the function is called
    return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":  # Fixed the typo in `if__name__`
    print("Wassup")  # Proper indentation
app.run(host="0.0.0.0", port=8080, debug=True)
# Add this to run the Flask app
