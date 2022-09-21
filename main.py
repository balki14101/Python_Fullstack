

from flask import Flask,jsonify,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Hello World"

@app.route('/user/<username>')
def show_user(username):
    # Greet the user
    return f'Hello {username} !'
   

##login page function##
@app.route("/login")
def login():
       return render_template('login.html')       

##signUp page function##
@app.route('/signUp')
def signUp():
   return render_template('signUp.html')   

##home page function##
@app.route('/home')
def home():
   return render_template('home.html')          
    
if __name__ == "__main__":
    app.run(debug=True)