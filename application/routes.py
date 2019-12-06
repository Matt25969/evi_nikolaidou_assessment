from flask import render_template
from application import app

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='Eurovision')

@app.route('/favorites')
def fsvorites():
    return render_template('favorites.html', title='Eurovision')

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('about'))

    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

        if next_page:
            return redirect(next_page)
        else:
            return redirect(url_for('about'))

    return render_template('login.html', title='Login', form=form)

@app.route('/signup')
def signup():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('about'))
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash
        user = Users(first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hashed_pw)
        db.session.add(user)
        db.session.commit
        return redirect(url_for('favorites'))
    return render_template('signup.html',title='Sign Up', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
