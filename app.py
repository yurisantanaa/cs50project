
import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///inventory.db")

@app.after_request
def after_request(response):
  response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
  response.headers["Expires"] = 0
  response.headers["Pragma"] = "no-cache"
  return response

#MAIN PAGE
@app.route("/")
@login_required
def index():
  produtos = []
  listaProductsOnDB = db.execute('SELECT * FROM products')
  # listaProductsOnDB = db.execute('SELECT productId FROM products')
  for produto in listaProductsOnDB:
    produtos.append(produto)
  print(produtos)
  return render_template("index.html",produtos = produtos)

#LOGIN RELATED
@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  else:
    session.clear()
    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
      return render_template("login.html",message="Please enter an email")
    if not password:
      return render_template("login.html",message="Please enter a password")
    
    search_rows = db.execute("SELECT * from users WHERE email = ?",email)

    if len(search_rows) != 1 or not check_password_hash(search_rows[0]['hash'],password):
      return render_template('login.html',message="Incorrect email or password")
    
    session['user_id'] = search_rows[0]['id']
    return redirect("/")
  
@app.route("/register",methods=["GET","POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")
  else:
    session.clear()
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("confirmation")
    email = request.form.get("email")

    if not username:
      return render_template("register.html",message="Please enter a username")
    if not password:
      return render_template("register.html",message="Please enter a password")
    if not password_confirmation:
      return render_template("register.html",message="Please confirm your password")
    if not email:
      return render_template("register.html",message="Please enter an email")
    if password != password_confirmation:
      return render_template("register.html",message="Passwords do not match")
    
    password_hash = generate_password_hash(password)

    if db.execute("SELECT * FROM users WHERE username = ?",username):
      return render_template("register.html",message="Username already in use")
    
    if db.execute("SELECT * FROM users WHERE email = ?",email):
      return render_template("register.html",message="Email already in use")

    db.execute("INSERT INTO users(username,email,hash) VALUES(?,?,?)",username,email,password_hash)

    return redirect("/") 

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")


#INVENTORY RELATED

@app.route("/add",methods=["GET","POST"])
@login_required
def addProduct():

  if request.method == "GET":
    return render_template('addItem.html')
  
  else:

    if db.execute('SELECT * FROM products WHERE name = ?',request.form.get('productName').upper()):
      return render_template('addItem.html',message='produto ja existe')
    
    productName = request.form.get('productName').upper()

    productCategoryOnDB = db.execute('SELECT * FROM categories WHERE categoryName = ?',request.form.get('productCategory').upper())
    if productCategoryOnDB:
      productCategory = productCategoryOnDB[0]['categoryid']
    else:
      db.execute('INSERT INTO categories(categoryName) VALUES(?)',request.form.get('productCategory').upper())
      productCategoryOnDB = db.execute('SELECT * FROM categories WHERE categoryName = ?',request.form.get('productCategory').upper())
      productCategory = productCategoryOnDB[0]['categoryid']
    
    stock = 0

    if request.form.get('productImage'):
      productImage = request.form.get('productImage')
    else:
      productImage = None
    
    if request.form.get('productDescription'):
      productDescription = request.form.get('productDescription')
    else:
      productDescription = None
    
    if not productName:
      return render_template('addItem.html',message='product name invalid or already exists')

    if not productCategory:
      return render_template('addItem.html',message='invalid product category')
    
    if not productImage:
      return render_template('addItem.html',message='invalid image')

    
    db.execute('INSERT INTO products(name,category,stock,image,description) VALUES(?,?,?,?,?)',productName,productCategory,stock,productImage,productDescription)
    

    return redirect('/')
  

@app.route("/sell",methods = ['GET','POST'])
def sell():
  if request.method == 'GET':
    return render_template('sell.html')
  else:
    productName = request.form.get('productName')
    productQuantity = request.form.get('productQuantity')

    productinDB = db.execute("SELECT * FROM products WHERE name = ?",productName)

    if not productinDB:
      return render_template("sell.html",message = 'product not availible')
    
    if productQuantity > productinDB['initial']:
      return render_template("sell.html",message = 'not enough units')
    

@app.route('/produto/<int:id>')
def produto(id):
    print()
    print(id)
    print()
    produto = db.execute('SELECT * FROM products WHERE productId = ?',id)
    print(produto)
    if produto:
        return render_template('product.html', produto=produto)
    else:
        return render_template("index.html",message = '404')