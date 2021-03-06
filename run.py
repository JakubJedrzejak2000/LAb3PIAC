from flask import Flask, render_template, url_for, abort, make_response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/error_not_found")
def error_not_found():
    response = make_response(render_template('template.html', name="ERROR 404"), 404)
    response.headers['X-Something'] = 'A value'
    return response


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0")
