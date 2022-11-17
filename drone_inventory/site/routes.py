from flask import Blueprint, render_template
from flask_login import login_required


site = Blueprint('site', __name__, template_folder='site_templates')

"""
Note that in the above code,
some arguements are specified when creating a blueprint object.
The first arguement, "site", is the Blueprint name as a string.
which is used my flask's routing mechanism.
The second arguement __name__ is the Blueprint's import name,
which Flask uses to locate the Blueprint's resources.
The third arguement is telling Flask where to find the html to render.
"""

@site.route('/') # this will go to home page
def home():
    return render_template('index.html')


@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')