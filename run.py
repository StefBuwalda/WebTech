from flask import Flask

# Create Flask instance
app = Flask("__name__")


# Default app route
@app.route("/")
def index():
    # Return HTML content
    return "<h1>This is the default page</h1>"


# Prevent execution when imported by other script
if __name__ == "__main__":
    # Start the flask server in debug mode for development purposes
    app.run(port=80, debug=True)
