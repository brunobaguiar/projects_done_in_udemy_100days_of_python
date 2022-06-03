from flask import Flask, render_template, request
import requests
import smtplib


MY_EMAIL = "your@email.com"
PASSWORD = "your_password"

app = Flask(__name__)

response = requests.get("https://api.npoint.io/e326a9bc8d63db470cca")
data = response.json()
titles = []
subtitles = []
bodies = []
authors = []
dates = []

for item in data:
    titles.append(item["title"])
    subtitles.append(item["subtitle"])
    bodies.append(item["body"])
    authors.append(item["author"])
    dates.append(item["date"])

@app.route('/')
def home():
    return render_template("index.html", titles=titles, subtitles=subtitles, dates=dates, authors=authors, num_items=int(len(titles)))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name_entry = request.form['name']
        email_entry = request.form['email']
        phone_entry = request.form['phone']
        message_entry = request.form['message']
        send_email(name_entry, email_entry, phone_entry, message_entry)
        title = "Successfully sent message"
        return render_template("contact.html", title=title)
    title = "Contact Me"
    return render_template("contact.html", title=title)


@app.route('/post/<int:num>')
def get_post(num):
    title = titles[num]
    subtitle = subtitles[num]
    body = bodies[num]
    author = authors[num]
    date = dates[num]
    return render_template("post.html", num=num, title=title, subtitle=subtitle, body=body, author=author, date=date)

# @app.route('/form-entry', methods=['GET', 'POST'])
# def receive_data():
#     if request.method == 'POST':
#         data = request.form
#         print(data["name"])
#         print(data["email"])
#         print(data["phone"])
#         print(data["message"])
#         return "<h1>Successfully sent your message</h1>"


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Encrypted message to secure our connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=email_message)

if __name__ == "__main__":
    app.run(debug=True)
