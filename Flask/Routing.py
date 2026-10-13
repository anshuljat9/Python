#What is Routing in Flask ?
# Flask App Routing is the process of connecting URL paths with Python functions in a Flask application. When a client requests a URL, Flask matches it with a registered route and calls the associated view function. The main routing mechanism is the route() decorator.
# Router har url ke liye alag alag route hote hain .

# home URL ke piche /about lagane se  -> about() function is se about page open hua hai 
# home URL ke piche /contact lagane se  -> contact() function is se contact page open hua hai 

# Common Mistake :
# same name ke function ko do alag alag route me use karne se error aayega .
# @app har route ke liye alag alag function ka name hona chahiye .


# Interview Question :

# 1. What is Routing in Flask and how does it work?
# Routing in Flask is the process of mapping URL paths to specific Python functions (view functions) in a Flask application. When a client makes a request to a particular URL, Flask checks its registered routes to find a match. If a match is found, Flask invokes the corresponding view function, which generates and returns the appropriate response (such as HTML content or JSON data) to the client. The main routing mechanism in Flask is the use of the @app.route() decorator, which associates a URL path with a specific function.

# 2. @app.route() decorator ka kya kaam hai?
# @app.route() decorator ka kaam hai ki ye URL path ko specific function ke saath map karta hai. Jab client us URL ko request karta hai, Flask us function ko call karta hai jo us route ke saath associated hai. Isse dynamic web pages aur APIs create karna possible hota hai.

# 3. Multiple route kaise handle karte hain Flask me?
# Flask me multiple routes handle karne ke liye hum alag alag @app.route() decorators ka use karte hain, jisme har route ke liye alag function define kiya jata hai. Har function ko unique name diya jata hai taki Flask ko pata chale ki kaunsa function kis route ke liye responsible hai. Agar same name ke function ko do alag alag routes me use karne ki koshish ki jaye to error aayega.