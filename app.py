from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Free Fire Beginner Course</title>

<style>
body{
    margin:0;
    font-family:Arial;
    background:linear-gradient(120deg,#0f172a,#020617);
    color:white;
}

nav{
    background:#020617;
    padding:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

nav h1{
    color:#f43f5e;
}

nav a{
    color:white;
    text-decoration:none;
    margin-left:20px;
}

.hero{
    text-align:center;
    padding:60px 20px;
}

.hero h2{
    font-size:40px;
}

.hero button{
    padding:12px 25px;
    border:none;
    background:#f43f5e;
    color:white;
    font-size:16px;
    border-radius:6px;
}

.container{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
    padding:30px;
}

.card{
    background:#1e293b;
    padding:25px;
    border-radius:10px;
    transition:0.3s;
}

.card:hover{
    transform:scale(1.05);
    background:#334155;
}

.card h3{
    color:#22c55e;
}

footer{
    background:#020617;
    text-align:center;
    padding:20px;
    margin-top:30px;
}
</style>

</head>

<body>

<nav>
<h1>🔥 FF Course</h1>
<div>
<a href="#">Home</a>
<a href="#">Lessons</a>
<a href="#">Tips</a>
<a href="#">Contact</a>
</div>
</nav>

<div class="hero">
<h2>Become a Free Fire Pro</h2>
<p>Learn headshots, sensitivity and survival strategy.</p>
<button>Start Learning</button>
</div>

<div class="container">

<div class="card">
<h3>Lesson 1</h3>
<p>Movement and controls for beginners.</p>
</div>

<div class="card">
<h3>Lesson 2</h3>
<p>Best sensitivity for headshots.</p>
</div>

<div class="card">
<h3>Lesson 3</h3>
<p>Best landing strategy.</p>
</div>

<div class="card">
<h3>Lesson 4</h3>
<p>Best beginner weapons.</p>
</div>

</div>

<footer>
<p>© 2026 Free Fire Beginner Course</p>
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
