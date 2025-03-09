from flask import Flask, render_template, redirect, request, session, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "very_secret_key"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success")
def payment_success():
    return render_template("success.html")


@app.route("/checkout")
def checkout():
    return render_template("payment.html")


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_id = int(request.form.get("product_id"))

    products = {
        1: {"name": "Dwarf Axeman", "price": 399.99},
        2: {"name": "Elf Ranger", "price": 349.99},
        3: {"name": "Three Magicians", "price": 699.99},
        4: {"name": "Three Adventurers", "price": 649.99},
        5: {"name": "Human Commander", "price": 549.99},
        6: {"name": "Human Cavalry", "price": 449.99},
    }

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]
    if product_id in products:
        cart.append(products[product_id])

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    return render_template("cart.html", cart=cart_items)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))


if __name__ == "__main__":
    app.run(debug=True)