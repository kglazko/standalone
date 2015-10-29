from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from .forms import LoginForm, QASignOffForm
from .models import CLRelease
import time

@app.route('/', methods=['GET','POST'])
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

    form = LoginForm()
    if form.validate_on_submit():
    	print "HELLO"
    	release = CLRelease(form.release_num.data)
    	db.session.add(release)
    	db.session.commit()
    	session['release'] = form.release_num.data
    	return redirect(url_for('release'))

    else:
    	print "FMLLLL"

    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts,
                           form = form)


@app.route('/release', methods=['GET', 'POST'])
def release():
	release_name = session['release']
	release = CLRelease.query.filter_by(name="4477").first()
	qa_form = QASignOffForm()
	if qa_form.validate_on_submit():
		qa_sign = qa_form.qa_signoff.data
		release.qa_signoff(qa_sign)
		release.qa_signoff_date = time.strftime("%c")
		db.session.add(release)
		db.session.commit()


   	return render_template("index.html", title="Home", qa_form = qa_form,release_name=release_name)
