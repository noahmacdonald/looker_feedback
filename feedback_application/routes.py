from flask import render_template, url_for, flash, redirect, request
from feedback_application import application
from feedback_application.forms import feedback_form

@application.route("/", methods=['GET', 'POST'])
def index():
	form = feedback_form()
	return render_template('index.html', form=form)

