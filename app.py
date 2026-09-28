from flask import Flask, request, redirect, url_for, render_template_string, send_from_directory
import sqlite3, os
app=Flask(__name__)
BASE='/var/www/awsapp'; DB=BASE+'/users.db'; UP=BASE+'/uploads'
os.makedirs(UP,exist_ok=True)
def db(): return sqlite3.connect(DB)
def init():
 c=db(); c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, first_name TEXT, last_name TEXT, email TEXT, address TEXT, upload_name TEXT, word_count INTEGER DEFAULT 0)"); c.commit(); c.close()
init()
STYLE="""<style>body{font:16px Arial;max-width:760px;margin:38px auto;background:#f7f9fc;color:#172033}form,.card{background:#fff;padding:26px;border-radius:12px;box-shadow:0 2px 12px #ccd}input{width:100%;padding:9px;margin:5px 0 14px;box-sizing:border-box}button,a.btn{background:#075985;color:#fff;padding:10px 15px;border:0;border-radius:7px;text-decoration:none;display:inline-block}nav{margin-bottom:22px}small{color:#526}</style>"""
@ app.route('/')
def home(): return STYLE+"<nav><a class=btn href='/login'>Re-login</a></nav><h1>AWS User Registration</h1><form method=post action='/register' enctype=multipart/form-data><label>Username</label><input name=username required><label>Password</label><input type=password name=password required><label>First name</label><input name=first_name required><label>Last name</label><input name=last_name required><label>Email</label><input type=email name=email required><label>Address</label><input name=address required><label>Upload Limerick text file</label><input type=file name=file accept='.txt' required><button>Register and view profile</button></form>"
@ app.route('/register',methods=['POST'])
def register():
 f=request.files['file']; name=os.path.basename(f.filename); path=os.path.join(UP,name); f.save(path)
 try: words=len(open(path,errors='ignore').read().split())
 except: words=0
 try:
  c=db();c.execute('INSERT INTO users(username,password,first_name,last_name,email,address,upload_name,word_count) VALUES(?,?,?,?,?,?,?,?)',(request.form['username'],request.form['password'],request.form['first_name'],request.form['last_name'],request.form['email'],request.form['address'],name,words));c.commit();c.close()
 except Exception as e:return STYLE+'<p>Username already exists. Choose another.</p><a class=btn href="/">Back</a>',400
 return redirect(url_for('profile',username=request.form['username']))
@ app.route('/profile/<username>')
def profile(username):
 c=db();u=c.execute('SELECT username,first_name,last_name,email,address,upload_name,word_count FROM users WHERE username=?',(username,)).fetchone();c.close()
 if not u:return redirect('/')
 return STYLE+f"<nav><a class=btn href='/'>New registration</a> <a class=btn href='/login'>Re-login</a></nav><div class=card><h1>Welcome, {u[1]} {u[2]}</h1><p><b>Username:</b> {u[0]}</p><p><b>Email:</b> {u[3]}</p><p><b>Address:</b> {u[4]}</p><p><b>Uploaded file:</b> {u[5]}</p><p><b>Word count:</b> {u[6]}</p><a class=btn href='/download/{u[5]}'>Download uploaded file</a></div>"
@ app.route('/login',methods=['GET','POST'])
def login():
 if request.method=='POST':
  c=db();u=c.execute('SELECT username FROM users WHERE username=? AND password=?',(request.form['username'],request.form['password'])).fetchone();c.close()
  return redirect(url_for('profile',username=u[0])) if u else (STYLE+'<p>Invalid login.</p><a class=btn href="/login">Try again</a>',401)
 return STYLE+"<h1>Re-login</h1><form method=post><label>Username</label><input name=username required><label>Password</label><input name=password type=password required><button>Sign in</button></form>"
@ app.route('/download/<name>')
def download(name): return send_from_directory(UP,name,as_attachment=True)
