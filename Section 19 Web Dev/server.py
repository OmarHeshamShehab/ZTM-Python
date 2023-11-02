import csv
from token import NEWLINE

from flask import Flask, redirect, render_template, request  # ,send_from_directory

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("./index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# get means browser wants us to send information
# post browser wants us to save information
@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    try:
        if request.method == "POST":
            data = request.form.to_dict()
            # save_data_txt(data)
            save_data_csv(data)
            return redirect("./thankyou.html")
    except:
        return "did not save to database"
    else:
        return "something went wrong, PLease try again later!"


def save_data_txt(data):
    with open("database.txt", mode="a") as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = db.write(f"\n{email},{subject},{message}")


def save_data_csv(data):
    with open("database.csv", mode="a", newline="") as db2:
        email = data["email"]

        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            db2, delimiter=",", quotechar=";", quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


# used in case of old browsers
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(
#         os.path.join(app.root_path, 'static'),
#         'favicon.ico',
#         mimetype='image/vnd.microsoft.icon',
#     )
