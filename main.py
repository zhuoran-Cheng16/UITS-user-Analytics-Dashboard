from flask import Flask, escape, url_for
from flask import request, render_template
import dash
import dash_html_components as html





server = Flask(__name__, template_folder='template')
app = dash.Dash(__name__, server=server, routes_pathname_prefix = '/dash/')

@server.route("/")
def index(name="Reuben"):
    return render_template("index.html", name=name)


app.layout = html.Div("My Dash App")


@server.route("/hello")
def hello(name=None):
    return render_template("hello.html", name=name)

@server.route("/projects")
def projects():
    return 'The project page'

@server.route("/notifications")
def notifications(name=None):
    return render_template("notifications.html", name=name)

@server.route("/about")
def about():
    return "The about page"

if __name__ == "__main__":
    app.debug= True
    app.run()
