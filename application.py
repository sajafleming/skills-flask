from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")



@app.route("/application-form")
def show_application_form():
    """Show the application for the user to fill out"""

    return render_template("application-form.html")



@app.route("/application", methods=["POST"])
def application_response():
    """Render application response"""
    fname = request.form.get("firstname")
    lname = request.form.get("lastname")
    minsalary = request.form.get("salary")
    title = request.form.get("jobtitle")

    return render_template("application-response.html",
                            jobtitle=title,
                            salary=minsalary,
                            lastname=lname,
                            firstname=fname)



if __name__ == "__main__":
    app.run(debug=True)
