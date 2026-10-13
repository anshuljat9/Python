# This is a dynamic route in Flask that takes a username as a parameter from the URL and returns a personalized greeting. The <username> part of the route is a variable that will be replaced with the actual username provided in the URL.
"""
@app.route("/user/<username>")
def user(username):
    return f"Hello, {username}!" 
"""

# This is another dynamic route that takes both a name and an age as parameters from the URL. The <name> and <int:age> parts of the route are variables that will be replaced with the actual name and age provided in the URL. The int: prefix indicates that the age parameter should be treated as an integer.
"""
@app.route("/student/<name>/<int:age>")
def student(name, age):
    return f"Hello, {name}! You are {age} years old."
"""

# Interview Question :
# 1. What is a dynamic route in Flask and how does it work?
# A dynamic route in Flask is a URL pattern that includes variable parts, allowing the route to accept parameters from the URL. These parameters can be used within the associated view function to generate dynamic content based on user input. When a client requests a URL that matches a dynamic route, Flask extracts the variable parts from the URL and passes them as arguments to the view function. This enables developers to create personalized responses and handle user-specific data in their web applications.


# 2. multiple Dynamic route kise handle kar sakte hai ?
# Flask me multiple dynamic routes handle karne ke liye hum alag alag @app.route() decorators ka use karte hain, jisme har route ke liye alag function define kiya jata hai. Har function ko unique name diya jata hai taki Flask ko pata chale ki kaunsa function kis route ke liye responsible hai. Agar same name ke function ko do alag alag dynamic routes me use karne ki koshish ki jaye to error aayega.

