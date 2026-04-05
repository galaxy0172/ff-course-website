from flask import Flask

app = Flask(__name__)

def layout(title, content):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>

<style>

body {{
margin:0;
font-family:Arial;
background:linear-gradient(120deg,#0f172a,#020617);
color:white;
}}

nav {{
background:#020617;
padding:15px;
display:flex;
justify-content:space-between;
align-items:center;
}}

nav h1 {{
color:#f43f5e;
margin:0;
}}

nav a {{
color:white;
text-decoration:none;
margin-left:20px;
}}

.hero {{
text-align:center;
padding:60px 20px;
}}

.hero h2 {{
font-size:40px;
}}

.container {{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:20px;
padding:30px;
}}

.card {{
background:#1e293b;
padding:20px;
border-radius:10px;
box-shadow:0 6px 15px rgba(0,0,0,0.4);
transition:0.3s;
}}

.card:hover {{
transform:scale(1.05);
background:#334155;
}}

.card h3 {{
color:#22c55e;
}}

button {{
background:#f43f5e;
border:none;
padding:10px 20px;
color:white;
border-radius:6px;
}}

footer {{
text-align:center;
padding:20px;
background:#020617;
color:gray;
}}

</style>
</head>

<body>

<nav>
<h1>🔥 FF Academy</h1>

<div>
<a href="/">Home</a>
<a href="/lessons">Lessons</a>
<a href="/tips">Tips</a>
<a href="/videos">Videos</a>
<a href="/earn">Earn</a>
<a href="/contact">Contact</a>
</div>

</nav>

{content}

<footer>
© 2026 Free Fire Academy
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    content = """
<div class="hero">
<h2>Become a Free Fire Pro</h2>
<p>Learn headshots, sensitivity and survival strategies.</p>
</div>

<div class="container">

<div class="card">
<h3>Beginner Lessons</h3>
<p>Learn the basics of Free Fire gameplay.</p>
</div>

<div class="card">
<h3>Headshot Training</h3>
<p>Master drag shots and aiming techniques.</p>
</div>

<div class="card">
<h3>Rank Push Guide</h3>
<p>Strategies to reach Heroic faster.</p>
</div>

</div>
"""
    return layout("Home", content)

@app.route("/lessons")
def lessons():
    content = """
<div class="hero"><h2>Lessons</h2></div>

<div class="container">

<div class="card">
<h3>Lesson 1</h3>
<p>Movement and controls basics.</p>
</div>

<div class="card">
<h3>Lesson 2</h3>
<p>Best sensitivity settings.</p>
</div>

<div class="card">
<h3>Lesson 3</h3>
<p>Landing locations and survival tips.</p>
</div>

<div class="card">
<h3>Lesson 4</h3>
<p>Best beginner weapons.</p>
</div>

</div>
"""
    return layout("Lessons", content)

@app.route("/tips")
def tips():
    content = """
<div class="hero"><h2>Pro Tips</h2></div>

<div class="container">

<div class="card">
<h3>Headshot Tips</h3>
<p>Use high sensitivity and drag shots.</p>
</div>

<div class="card">
<h3>Survival Tips</h3>
<p>Stay near cover and rotate early.</p>
</div>

<div class="card">
<h3>Weapon Tips</h3>
<p>Use MP40 and M1887 for close fights.</p>
</div>

</div>
"""
    return layout("Tips", content)

@app.route("/videos")
def videos():
    content = """
<div class="hero"><h2>Training Videos</h2></div>

<div class="container">

<div class="card">
<h3>Headshot Training</h3>

<iframe width="100%" height="200"
src="https://www.youtube.com/embed/dQw4w9WgXcQ"
frameborder="0"
allowfullscreen></iframe>

</div>

</div>
"""
    return layout("Videos", content)

@app.route("/earn")
def earn():
    content = """
<div class="hero"><h2>Earn With This Website</h2></div>

<div class="container">

<div class="card">
<h3>Advertisement</h3>
<p>Place ads here to earn money.</p>
</div>

<div class="card">
<h3>Affiliate Marketing</h3>
<p>Recommend gaming phones or accessories.</p>
</div>

<div class="card">
<h3>YouTube Promotion</h3>
<p>Promote your gaming channel.</p>
</div>

</div>
"""
    return layout("Earn", content)

@app.route("/contact")
def contact():
    content = """
<div class="hero"><h2>Contact & Community</h2></div>

<div class="container">

<div class="card">
<h3>Instagram</h3>
<p>Follow my gaming page:</p>
<p><b>@oster_rx</b></p>
<button>Follow</button>
</div>

</div>
"""
    return layout("Contact", content)

if __name__ == "__main__":
    app.run()

