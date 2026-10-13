from flask import Flask  # type: ignore

app = Flask(__name__)
@app.route("/") #
def home():
    return "Hello Anshul"

@app.route("/users")
def users():
    return "This is users page"

@app.route("/user/<username>") # This is dynamic route 
def user(username):
    return f"Hello, {username}!"

@app.route("/student/<name>/<int:age>") # This is also synamic route with the multiple parameter 
def student(name, age):
    return f"Hello, {name}! You are {age} years old."

@app.route("/about")
def about():
    return "This is about page"


if __name__ == "__main__":
    app.run(debug=True)

# debug=true is liye hai ki baar baar server ko restart na karna pade jab bhi code me changes ho. 

# Interview Questions:
# 1. What is Flask and why is it used?
# Flask is a lightweight web framework used to build web applications and APIs. It is used for its simplicity, flexibility, and minimal design, allowing developers to create dynamic web pages and RESTful APIs with ease.

# 2. why need virtual environment in flask?
# A virtual environment is needed in Flask to create an isolated environment for the project, ensuring that dependencies and packages do not conflict with other projects or the system's Python installation. It allows developers to manage project-specific dependencies and maintain a clean development environment.

# 3. __name__ == "__main__" ka kya matlab hai?
# __name__ ek special variable hai jo current module ka name store karta hai. Jab hum directly script ko run karte hain, to __name__ ki value "__main__" hoti hai. Iska matlab hai ki ye code block sirf tab execute hoga jab script ko directly run kiya jaye, na ki import kiya jaye.