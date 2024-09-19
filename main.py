from flask import Flask, render_template, request, redirect, url_for, flash
from database import db

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db_name = "subscription.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db.init_app(app)


def create_db() -> None:
    """Create database tables."""
    with app.app_context():
        db.create_all()
        print("Database tables created.")


@app.route("/", methods=['GET', 'POST'])
def home():
    """Render the home page and handle subscription requests."""
    if request.method == "POST":
        email = request.form.get("Email")
        name = request.form.get("Name")
        subscription = request.form.get("subscription")
        existing_subscriber = Subscribe.query.filter_by(email=email).first()
        if existing_subscriber is not None:
            subscription_status_url = url_for("get_subscription_status", email=email)
            flash(
                f'User is already subscribed with email {email}. <a href="{subscription_status_url}">click here to see '
                f'subscription status</a>',
                'warning'
            )
            return redirect(url_for("home"))
            # Add new subscriber
        flash('User is successfully subscribed', 'success')
        new_subscription = Subscribe(name=name, email=email, subscription=subscription, is_active=True)
        db.session.add(new_subscription)
        db.session.commit()
        return redirect(url_for("get_subscription_status", email=email))
    return render_template("home.html")


@app.route("/subscription_status/<email>")
def get_subscription_status(email):
    """Display the subscription status for a given email."""
    subs = Subscribe.query.filter_by(email=email).first()
    if not subs:
        flash(f'No subscription found for email {email}', 'danger')
        return redirect(url_for("home"))

    return render_template("subscription.html", subscription=subs)


@app.route("/all_user_subscription")
def get_all_subscription():
    """Display all user subscriptions."""
    subs = Subscribe.query.all()
    print(subs)
    return render_template("all_subscription.html", all_subscription=subs)


@app.route("/update_subs/<email>")
def update_subscription(email: str):
    """Toggle the subscription status for a given email."""
    subscription = Subscribe.query.filter_by(email=email).first()
    if subscription:
        subscription.is_active = not subscription.is_active  # Toggle is_active status
        if subscription.is_active:
            flash(f'User {email} subscription is Activated', 'success')
        else:
            flash(f'User {email} subscription is Deactivated', 'danger')

        db.session.commit()

    return redirect(url_for("get_subscription_status", email=email))


@app.route("/unsubscribe/<email>")
def unsubscribe(email: str):
    """Unsubscribe a user by email."""
    subscription = Subscribe.query.filter_by(email=email).first()
    if subscription:
        db.session.delete(subscription)
        db.session.commit()
        flash(f'User with email {email} unsubscribed', 'warning')
    else:
        flash(f'No subscription found for email {email}', 'danger')

    return redirect(url_for("home"))


if __name__ == '__main__':
    from models import Subscribe
    create_db()
    app.run(debug=True)
