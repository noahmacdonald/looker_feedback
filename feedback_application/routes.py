from flask import render_template, url_for, flash, redirect, request
from feedback_application import application
from feedback_application.forms import feedback_form

@application.route("/", methods=['POST'])
def index():
	print(request.form)
	print('Submitter name: ', request.form.get('sub_name'))
	print('Submitter email: ', request.form.get('sub_email'))
	print('Customer name: ', request.form.get('name'))
	print('Customer job title: ', request.form.get('job_title'))
	print('Customer Company: ', request.form.get('customer'))
	print('I want... : ', request.form.get('i_want'))
	print('So that...: ', request.form.get('so_that'))
	print('Addt Info: ', request.form.get('addt_info'))
	print('Priority: ', request.form.get('priority'))
	issue_url = "https://looker.atlassian.net/secure/CreateIssueDetails!init.jspa?pid=10610&issuetype=2&summary="
	issue_url = issue_url + str(request.form.get('i_want'))

	return redirect(issue_url)

