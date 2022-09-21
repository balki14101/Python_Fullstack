

from flask import Flask,jsonify,render_template

app = Flask(__name__)

todo = [{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",    
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",    
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",    
  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",    
  },
  {
    "userId": 1,
    "id": 5,
    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",    
  },
  {
    "userId": 1,
    "id": 6,
    "title": "qui ullam ratione quibusdam voluptatem quia omnis",    
  },
  {
    "userId": 1,
    "id": 7,
    "title": "illo expedita consequatur quia in",    
  },
  {
    "userId": 1,
    "id": 8,
    "title": "quo adipisci enim quam ut ab",    
  },
  {
    "userId": 1,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",    
  },
  {
    "userId": 1,
    "id": 10,
    "title": "illo est ratione doloremque quia maiores aut",    
  },
  {
    "userId": 1,
    "id": 11,
    "title": "vero rerum temporibus dolor",    
  },
  {
    "userId": 2,
    "id": 26,
    "title": "aliquam aut quasi",
  },
  {
    "userId": 2,
    "id": 27,
    "title": "veritatis pariatur delectus",
  },
  {
    "userId": 2,
    "id": 28,
    "title": "nesciunt totam sit blanditiis sit",
  }]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/todos",methods = ['POST', 'GET'])
def get():
    return  jsonify({"TODOS":todo})  

@app.route("/todos/<int:id>")
def getId(id):
    return  jsonify({"TODOS":todo[id]})   

@app.route('/user/<username>')
def show_user(username):
    # Greet the user
    return f'Hello {username} !'
   

##login page function##
@app.route("/login")
def login():
       return render_template('demoHtml.html')

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