from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    # "http://localhost:8000",
    # "http://192.168.155.62:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_methods=["*"],
    # allow_headers=["*"],
)
app.include_router(user)






# @app.get("/")
# def index():
#     return {"message": "Welcome To FastAPI World"}

# from flask import Flask,jsonify,render_template,url_for

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#    return "Hello World"

# @app.route('/user/<username>')
# def show_user(username):
#     # Greet the user
#     return f'Hello {username} !'
   

# ##login page function##
# @app.route("/login")
# def login():
#        return render_template('login.html')       

# ##signUp page function##
# @app.route('/signUp')
# def signUp():
#    return render_template('signUp.html')   

# ##home page function##
# @app.route('/home')
# def home():
#    return render_template('demoHtml.html')          


    
# if __name__ == "__main__":
#     app.run(debug=True)