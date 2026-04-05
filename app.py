from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1> Free Fire Beginner Course</h1>

    <h2>Lesson 1</h2>
    <p>Movement and controls</p>

    <h2>Lesson 2</h2>
    <p>Best sensitivity for headshots</p>

    <h2>Lesson 3</h2>
    <p>Landing strategy</p>

    <h2>Lesson 4</h2>
    <p>Best beginner weapons</p>
    """

if __name__ == "__main__":
    app.run()
