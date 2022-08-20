from app import app
from flask import render_template
from app.forms import AddressForm
from app.models import Person

@app.route('/')
def index():
    registry = {
        'name': 'Coolio',
        'phone': '555-968-4563',
        'address': '718 Fantastic Voyage Ave'
    }
    return render_template('index.html', registry=registry)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = AddressForm()
    if form.validate_on_submit():
        print('Form has been validated!')
        username = form.username.data
        phone = form.phone.data
        address = form.address.data
        registry = Person(username=username, phone=phone, address=address)
        print(f"{registry.username} has been created.")
    return render_template('register.html', form=form)