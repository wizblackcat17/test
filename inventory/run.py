from flask import Flask, render_template, request, redirect
import mysql.connector

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)


# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="inventory"
)

# Create cursor
cursor = db.cursor()

# Create tables if they don't exist
tables = [
    """
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS items (
        item_id INT AUTO_INCREMENT PRIMARY KEY,
        item_name VARCHAR(255),
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS prices (
        price_id INT AUTO_INCREMENT PRIMARY KEY,
        item_id INT,
        price DECIMAL(10, 2),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (item_id) REFERENCES items(item_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS barcodes (
        barcode_id INT AUTO_INCREMENT PRIMARY KEY,
        barcode_number VARCHAR(255),
        item_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (item_id) REFERENCES items(item_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS reports (
        report_id INT AUTO_INCREMENT PRIMARY KEY,
        report_name VARCHAR(255),
        user_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    """
]

for table in tables:
    cursor.execute(table)

# Home route
@app.route('/')
def home():
    # Fetch all items from the items table
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return render_template('index.html', items=items)

# Add item route
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        # Insert new item into the items table
        cursor.execute("""
            INSERT INTO items (item_name, description)
            VALUES (%s, %s)
        """, (name, description))
        db.commit()

        return  render_template('index.html')

    return render_template('add.html')



# Add barcode route
@app.route('/add_barcode', methods=['GET', 'POST'])
def add_barcode():
    if request.method == 'POST':
        item_id = request.form['item_id']
        barcode_number = request.form['barcode_number']

        # Insert barcode information into barcode table
        cursor.execute("""
            INSERT INTO barcode (item_id, barcode_number)
            VALUES (%s, %s)
        """, (item_id, barcode_number))
        db.commit()

        return  redirect('/view_barcode')

    return render_template('add_barcode.html')

# Add price route
@app.route('/view_barcode', methods=['GET'])
def view_barcode():
    cursor.execute("SELECT * FROM barcodes")
    barcodes_data = cursor.fetchall()
    print("barcodes_data", barcodes_data)
    return render_template('view_prices.html', barcodes_data=barcodes_data)
# Add customer route
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Insert customer information into customers table
        cursor.execute("""
            INSERT INTO customers (customer_name, email)
            VALUES (%s, %s)
        """, (name, email))
        db.commit()

        return  redirect('/view_customers')

    return render_template('add_customer.html')


# Add price route
@app.route('/view_customers', methods=['GET'])
def view_customers():
    cursor.execute("SELECT * FROM customers")
    customer_data = cursor.fetchall()
    print("customer_data", customer_data)
    return render_template('view_customers.html', customer_data=customer_data)

# Add price route
@app.route('/add_price', methods=['GET', 'POST'])
def add_price():
    if request.method == 'POST':
        item_id = request.form['item_id']
        price = request.form['price']

        # Insert price information into prices table
        cursor.execute("""
            INSERT INTO prices (item_id, price)
            VALUES (%s, %s)
        """, (item_id, price))
        db.commit()

        return  redirect('/view_prices')
    cursor.execute("SELECT * FROM prices")
    price_data = cursor.fetchall()
    print("price_data", price_data)
    return render_template('add_prices.html', price_data)


# Add price route
@app.route('/view_prices', methods=['GET'])
def view_prices():
    cursor.execute("SELECT * FROM prices")
    price_data = cursor.fetchall()
    print("price_data", price_data)
    return render_template('view_prices.html', price_data=price_data)

@app.route('/add_report', methods=['GET', 'POST'])
def add_report():
    if request.method == 'POST':
        # Retrieve the data from the form
        report_name = request.form.get('report_name')
        report_id = request.form.get('report_id')
        user_id = request.form.get('user_id')

        # TODO: Perform validation and error handling

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # SQL query to insert the report data into the database
        sql = "INSERT INTO reports (report_name, report_id, user_id) VALUES (%s, %s, %s)"
        values = (report_name, report_id, user_id)

        # Execute the SQL query
        cursor.execute(sql, values)

        # Commit the changes to the database
        db.commit()

        # Close the cursor
        cursor.close()

        # Redirect back to the form or to a success page
        return redirect('/add_report')
    return render_template('add_reports.html')


@app.route('/view_reports', methods=['GET'])
def view_reports():
    cursor.execute("SELECT * FROM reports")
    price_data = cursor.fetchall()
    print("price_data", price_data)
    return render_template('view_reports.html', price_data=price_data)

if __name__ == '__main__':
    app.run(debug=True)
