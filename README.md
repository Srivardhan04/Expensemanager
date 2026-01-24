💰 Expense Manager – Full Stack Django Project!!

A full-stack web application built using Django, HTML, CSS, and JavaScript that helps users track income and expenses, visualize spending patterns, and export financial reports.
🚀 Features
🔐 Authentication
User registration & login
Secure session handling
User-specific data
📊 Dashboard
Total Income, Expense, Balance
Today / Week / Month spending
Filter by date, category, amount
Search & sort transactions
📝 Expense Management
Add, Edit, Delete transactions
Categories & notes support
📈 Analytics
Monthly expense bar chart
Category breakdown pie chart
Interactive charts using Chart.js
📤 Reports & Export
Export to:
PDF
Excel (.xlsx)
CSV
Weekly / Monthly / Yearly reports
🎨 UI / UX
Glassmorphism design
Dark / Light theme toggle
Responsive layout
Smooth animations
☁ Deployment Ready
Render compatible
🧠 Tech Stack
Layer	Technology
Backend	Django 5
Frontend	HTML, CSS, JS
Charts	Chart.js
Database	SQLite (local), PostgreSQL (prod)
Exports	ReportLab, OpenPyXL
Hosting	Render
Static Files	WhiteNoise

expense_manager/
│
├── expense_manager/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── expenses/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   ├── static/
│
├── staticfiles/
├── db.sqlite3
├── manage.py
├── requirements.txt

⚙ Setup Locally
1. Clone Repo
git clone https://github.com/yourusername/expense-manager.git
cd expense-manager

2. Create Virtual Env
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Migrate Database
python manage.py migrate

5. Run Server
python manage.py runserver

Open:
http://127.0.0.1:8000/
🗄 Where Data is Stored
Local: db.sqlite3
Production: PostgreSQL (Render)
Each user has separate data
Uses Django ORM
🌍 Deployment (Render)
Gunicorn for server
Whitenoise for static files
PostgreSQL database
Environment variables for security
📦 requirements.txt
Django
gunicorn
whitenoise
dj-database-url
psycopg2-binary
reportlab
openpyxl
🧪 Sample Screens
Login & Register
Dashboard
Analytics
Export buttons
Edit/Add forms
🔒 Security
Password hashing (Django)
CSRF protection
Login required pages
Environment secrets
👨‍💻 Author
Name: Lakshmi Srivardha Tallapaneni
Project: Expense Manager
Role: Full Stack Developer
Year: 2026
⭐ Future Improvements
Mobile app version
Email reports
Budget limits
AI spending insights
📜 License
This project is for educational and personal use.
Feel free to modify and extend.
Just create a file:
README.md
Paste this content, then:
git add README.md
git commit -m "Added project README"
git push


Whitenoise static handling

PostgreSQL ready
