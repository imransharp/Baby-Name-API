from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# --- Dataset of names ---
names = {
    "boy": [
        {
            "name": "Ibrahim",
            "occurrences": 69,
            "references": ["2:124", "4:54", "6:74"],
            "bio": "Prophet Ibrahim (Abraham), father of prophets, mentioned 69 times in Quran."
        },
        {
            "name": "Yusuf",
            "occurrences": 27,
            "references": ["12:4", "12:7", "12:23"],
            "bio": "Prophet Yusuf (Joseph), known for patience and beauty, story in Surah Yusuf."
        },
        {
            "name": "Musa",
            "occurrences": 136,
            "references": ["2:51", "7:103", "20:9"],
            "bio": "Prophet Musa (Moses), mentioned most in Quran, leader of Bani Israel."
        }
    ],
    "girl": [
        {
            "name": "Maryam",
            "occurrences": 24,
            "references": ["3:42", "19:16", "21:91"],
            "bio": "Maryam (Mary), mother of Prophet Isa (Jesus), only woman mentioned by name in Quran."
        },
        {
            "name": "Aisha",
            "occurrences": 0,
            "references": [],
            "bio": "Aisha (RA), wife of Prophet Muhammad (PBUH), scholar of Hadith."
        },
        {
            "name": "Khadija",
            "occurrences": 0,
            "references": [],
            "bio": "Khadija (RA), first wife of Prophet Muhammad (PBUH), first believer in Islam."
        }
    ]
}

@app.route("/")
def home():
    return "Flask is running! 🚀"

@app.route("/api/get_name")
def getname():
    gender = request.args.get("gender")
    if gender is None:
        return jsonify({"error": "Missing parameter: gender=boy or gender=girl"})
    gender = gender.lower()
    if gender in names:
        return jsonify(random.choice(names[gender]))
    return jsonify({"error": "Invalid gender, please use boy or girl"})

# --- GUI Page ---
@app.route("/web")
def web():
    gender = request.args.get("gender")
    selected_name = None

    if gender and gender.lower() in names:
        selected_name = random.choice(names[gender.lower()])

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Baby Name Generator</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container py-5">
            <h1 class="text-center mb-4">🌙 Quranic Baby Name Generator</h1>

            <form method="get" action="/web" class="text-center mb-4">
                <label for="gender" class="form-label">Select Gender:</label>
                <select name="gender" class="form-select w-25 d-inline-block">
                    <option value="boy">Boy</option>
                    <option value="girl">Girl</option>
                </select>
                <button type="submit" class="btn btn-success ms-2">Find Name</button>
            </form>

            {% if selected_name %}
            <div class="card shadow-lg p-4">
                <h2 class="text-primary">{{ selected_name.name }}</h2>
                <p><strong>Occurrences in Quran:</strong> {{ selected_name.occurrences }}</p>
                <p><strong>References:</strong> {{ selected_name.references | join(", ") }}</p>
                <p><strong>Bio:</strong> {{ selected_name.bio }}</p>
            </div>
            {% endif %}
        </div>
    </body>
    </html>
    """, selected_name=selected_name)


if __name__ == "__main__":
    app.run(debug=True)
