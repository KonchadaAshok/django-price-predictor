Real-Time Price Prediction (Django + ML)

This project is a **Real-Time Price Prediction Web App** built using **Django** and integrated with a trained **Machine Learning model**.  
It allows users to input feature values and get instant price predictions — displayed in a visually appealing and dynamic interface.

---

Features

- Interactive and glassmorphic UI 
- Real-time ML model predictions 
- Popup notifications for success/error alerts  
- Responsive design for all devices  
- Secure Django backend with CSRF protection  

---
Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Django (Python) |
| Machine Learning | Scikit-learn / joblib model |
| Database | SQLite (default) |
| Version Control | Git & GitHub |

---

 Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create and activate a virtual environment
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install required dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, create one using:

pip freeze > requirements.txt

4️⃣ Run database migrations
python manage.py makemigrations
python manage.py migrate

4. Run the Django development server
python manage.py runserver


Then open your browser and visit:
👉 http://127.0.0.1:8000/

🧠 Machine Learning Model Integration

If you’ve trained an ML model separately (e.g., model.pkl), make sure it’s located in your Django app directory, for example:

price_predictor/
│
├── ml_model/
│   └── model.pkl


Then, in your Django views.py, load it like this:

import joblib
model = joblib.load('ml_model/model.pkl')

Static Files (Logo, CSS, JS)

Place all static assets in the /static/ directory, for example:

static/
├── images/
│   └── w2a.jpeg
├── css/
│   └── style.css


Then, in your template:

{% load static %}
<img src="{% static 'images/w2a.jpeg' %}" alt="Logo">

🧾 Common Django Commands
Command	Description
python manage.py runserver	Start the server
python manage.py startapp <appname>	Create a new app
python manage.py createsuperuser	Create admin user
python manage.py collectstatic	Collect static files for deployment
🧩 Folder Structure
price_predictor_project/
│
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── price_predictor/          # Django app
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
└── ml_model/
    └── model.pkl
 Troubleshooting

Static files not loading?
Make sure you added this in settings.py:

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


Logo not showing?
Check that the file path matches exactly with what you reference in your template.

Model not found?
Verify model.pkl exists and is in the correct directory.

 Author

Konchada Ashok
💼 Machine Learning & Django Developer
📧 [konchadaashokkumar436@gmail.com, ashokkumarkonchada@gmail.com]
🌐 https://github.com/KonchadaAshok

📜 License

This project is open-source and available under the MIT License.


---
