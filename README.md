# 🌙 Quranic Baby Name Generator

A simple **Flask web app** that generates baby names from the Quran and Islamic history.  
Users can select **Boy** or **Girl**, and the app returns a **random name** with references, occurrences in the Quran, and a short biography.

---

## 🚀 Features
- Choose **boy** or **girl** name
- Returns a random name each time
- Shows references, occurrences, and biography
- Web front-end built with **Bootstrap**
- REST API endpoint: `/api/get_name`

---

## 🛠 Tech Stack
- Python (Flask)
- HTML + Bootstrap (front-end)
- Gunicorn (for production server)

---

## 📌 Installation (Local)
```bash
# clone the repo
git clone https://github.com/YOUR-USERNAME/baby-name-app.git
cd baby-name-app

# create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# install dependencies
pip install -r requirements.txt

# run app
python app.py
