from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/product')
def product_page():
    return render_template("product.html")


@app.route ('/sweatshirt')
def buy_sweatshirt():
    return render_template('sweatshirt.html')

@app.route('/table')
def buy_table():
    return render_template('table.html')

@app.route('/bags')
def buy_bags():
    return render_template('bags.html')

@app.route('/totebag')
def buy_totebag():
    return render_template('totebag.html')


@app.route('/cart')
def cart_page():
    return render_template('cart.html')


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
