# 💰 Expense Manager

A comprehensive web-based expense tracking and management application built with Django. Track your income, expenses, and visualize your spending patterns with intuitive charts and reports.

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Django](https://img.shields.io/badge/django-5.2.9-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 📊 Dashboard
- **Real-time Overview**: View your current balance, total income, and total expenses at a glance
- **Quick Stats**: Track today's spending, weekly expenses, and monthly totals
- **Interactive Charts**: Visualize your financial data with beautiful Chart.js graphs
- **Transaction List**: Browse all your transactions with search and filter capabilities

### 💸 Transaction Management
- **Income & Expense Tracking**: Record both income and expense transactions
- **Categories**: Organize transactions into customizable categories
- **Date Management**: Track when each transaction occurred
- **Edit & Delete**: Full CRUD operations for managing your transactions

### 📈 Reports & Analytics
- **Monthly Trends**: Compare income vs. expenses across different months
- **Category Breakdown**: See spending distribution across categories with pie charts
- **Time-based Analysis**: Filter by date ranges to analyze specific periods
- **Search Functionality**: Quickly find transactions by title or category

### 👤 User Management
- **Secure Authentication**: User registration and login system
- **Profile Management**: Update your profile information
- **Password Security**: Change password functionality with validation
- **Multi-user Support**: Each user has their own isolated data

### 🔒 Security Features
- CSRF protection enabled
- Secure session cookies
- Password hashing with Django's built-in authentication
- SQL injection prevention through Django ORM
- XSS protection with template escaping

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srivardhan04/Expensemanager.git
   cd Expensemanager
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file or set the following environment variables:
   DJANGO_SECRET_KEY=your-secret-key-here
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Register a new account or login with your credentials

## 📁 Project Structure

```
expense_manager/
├── expense_manager/          # Main project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── expenses/                # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # App URL patterns
│   ├── static/             # Static files (CSS, JS)
│   └── templates/          # HTML templates
├── staticfiles/            # Collected static files
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
├── build.sh               # Build script for deployment
└── README.md              # Project documentation
```

## 🗄️ Database Models

### Transaction Model
- **user**: Foreign key to User model (tracks ownership)
- **title**: Transaction description
- **amount**: Transaction amount (Decimal)
- **category**: Transaction category (e.g., Food, Transport, Salary)
- **type**: "income" or "expense"
- **date**: Transaction date
- **description**: Optional detailed description

## 🎨 Technologies Used

### Backend
- **Django 5.2.9**: Web framework
- **Python 3.11**: Programming language
- **SQLite/PostgreSQL**: Database
- **Gunicorn**: WSGI HTTP Server

### Frontend
- **HTML5 & CSS3**: Structure and styling
- **JavaScript**: Interactive functionality
- **Chart.js**: Data visualization
- **Bootstrap**: Responsive design

### Deployment
- **WhiteNoise**: Static file serving
- **Render**: Cloud hosting platform

## 🌐 Deployment

This application is configured for deployment on Render.com.

### Deploy to Render

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Render**
   - Create a new Web Service on [Render](https://render.com)
   - Connect your GitHub repository
   - Render will automatically detect the configuration from `render.yaml`

3. **Set environment variables**
   - Add `DJANGO_SECRET_KEY` in the Render dashboard

4. **Deploy**
   - Render will automatically build and deploy your application
   - Access your application at the provided URL

## 📊 Usage

### Adding a Transaction
1. Navigate to Dashboard
2. Click "Add Transaction" button
3. Fill in the details:
   - Title
   - Amount
   - Category
   - Type (Income/Expense)
   - Date
4. Click "Save"

### Viewing Reports
1. Go to the Reports page
2. Select date range or category filters
3. View charts and analytics
4. Export data if needed

### Managing Profile
1. Click on Profile in the navigation
2. Update your information
3. Change password if needed
4. Save changes

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DJANGO_SECRET_KEY` | Secret key for Django | Yes | (dev key in debug mode) |
| `DEBUG` | Debug mode | No | False |
| `DATABASE_URL` | Database connection string | No | SQLite |
| `ALLOWED_HOSTS` | Allowed domain names | No | localhost, 127.0.0.1, .onrender.com |

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Srivardhan**
- GitHub: [@Srivardhan04](https://github.com/Srivardhan04)
- Repository: [Expensemanager](https://github.com/Srivardhan04/Expensemanager.git)

## 🙏 Acknowledgments

- Django Documentation
- Chart.js for beautiful visualizations
- Bootstrap for responsive design
- The open-source community

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the Django documentation

## 🔮 Future Enhancements

- [ ] Budget planning and alerts
- [ ] Recurring transactions
- [ ] Multi-currency support
- [ ] Export to PDF/Excel
- [ ] Mobile application
- [ ] Email notifications
- [ ] Advanced analytics and predictions
- [ ] Receipt image upload
- [ ] Shared accounts for families
- [ ] Bank account integration

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
