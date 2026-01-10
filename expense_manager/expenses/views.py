from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction
from datetime import date, timedelta
from django.http import HttpResponse

# ================= REGISTER =================
def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        if not username or not password:
            return render(request, "register.html", {"error": "All fields required"})
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "User exists"})
        User.objects.create_user(username=username, password=password)
        return redirect('/login/')
    return render(request, "register.html")

# ================= LOGIN =================
def login_user(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/?msg=welcome')
        return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

# ================= LOGOUT =================
def logout_user(request):
    logout(request)
    return redirect('/login/')

# ================= DASHBOARD =================
@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # Filters
    if request.GET.get("search"):
        transactions = transactions.filter(title__icontains=request.GET["search"])
    if request.GET.get("category"):
        transactions = transactions.filter(category=request.GET["category"])
    if request.GET.get("start"):
        transactions = transactions.filter(date__gte=request.GET["start"])
    if request.GET.get("end"):
        transactions = transactions.filter(date__lte=request.GET["end"])

    # Summary
    total_income = transactions.filter(type="income").aggregate(t=Sum("amount"))["t"] or 0
    total_expense = transactions.filter(type="expense").aggregate(t=Sum("amount"))["t"] or 0
    balance = total_income - total_expense

    today = date.today()
    today_spent = transactions.filter(date=today, type="expense").aggregate(t=Sum("amount"))["t"] or 0
    week_spent = transactions.filter(date__gte=today-timedelta(days=7), type="expense").aggregate(t=Sum("amount"))["t"] or 0
    month_spent = transactions.filter(date__month=today.month, type="expense").aggregate(t=Sum("amount"))["t"] or 0

    # Monthly Data
    months = list(range(1,13))
    expense_totals = []
    income_totals = []

    for m in months:
        expense_totals.append(
            transactions.filter(date__month=m, type="expense").aggregate(t=Sum("amount"))["t"] or 0
        )
        income_totals.append(
            transactions.filter(date__month=m, type="income").aggregate(t=Sum("amount"))["t"] or 0
        )

    # Categories
    categories = {}
    for t in transactions:
        categories[t.category] = categories.get(t.category, 0) + t.amount

    categories_list = Transaction.objects.filter(user=request.user)\
        .values_list("category", flat=True).distinct()

    return render(request, "dashboard.html", {
        "expenses": transactions,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "today_spent": today_spent,
        "week_spent": week_spent,
        "month_spent": month_spent,
        "months": months,
        "month_totals": expense_totals,
        "income_totals": income_totals,
        "categories": {
            "keys": list(categories.keys()),
            "values": list(categories.values())
        },
        "categories_list": categories_list,
    })

# ================= ADD =================
@login_required
def add_expense(request):
    if request.method == "POST":
        Transaction.objects.create(
            user=request.user,
            title=request.POST["title"],
            category=request.POST["category"],
            type=request.POST["type"],
            amount=request.POST["amount"],
            date=request.POST["date"],
            note=request.POST.get("note","")
        )
        return redirect('/?msg=added')
    return render(request, "add_expense.html")

# ================= EDIT =================
@login_required
def edit_expense(request, id):
    exp = get_object_or_404(Transaction, id=id, user=request.user)
    if request.method == "POST":
        for f in ["title","category","type","amount","date","note"]:
            setattr(exp, f, request.POST.get(f))
        exp.save()
        return redirect('/?msg=updated')
    return render(request, "edit_expense.html", {"expense": exp})

# ================= DELETE =================
@login_required
def delete_expense(request, id):
    get_object_or_404(Transaction, id=id, user=request.user).delete()
    return redirect('/?msg=deleted')

# ================= PDF EXPORT =================
@login_required
def download_pdf_report(request):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="expense_report.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    y = 800
    p.drawString(50, y, f"Expense Report - {request.user.username}")
    y -= 30

    for t in transactions:
        p.drawString(50, y, f"{t.date} | {t.title} | {t.category} | {t.type} | ₹{t.amount}")
        y -= 15
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response

# ================= EXCEL EXPORT =================
@login_required
def download_excel_report(request):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    ws.append(["Date","Title","Category","Type","Amount","Note"])

    for t in Transaction.objects.filter(user=request.user):
        ws.append([t.date, t.title, t.category, t.type, t.amount, t.note])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="expense_report.xlsx"'
    wb.save(response)
    return response

# ================= CSV EXPORT =================
@login_required
def download_csv_report(request):
    import csv
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="expense_report.csv"'
    writer = csv.writer(response)
    writer.writerow(["Date","Title","Category","Type","Amount","Note"])
    for t in Transaction.objects.filter(user=request.user):
        writer.writerow([t.date, t.title, t.category, t.type, t.amount, t.note])
    return response

# ================= REPORTS PAGE =================
@login_required
def reports_page(request):
    return render(request, "reports.html")

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# ================= PROFILE =================
@login_required
def profile_page(request):
    return render(request, "profile.html")

# ================= CHANGE PASSWORD =================
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("/profile/?msg=changed")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})

# ================= BACKUP PAGE =================
@login_required
def backup_page(request):
    return render(request, "backup.html")

# ================= DOWNLOAD BACKUP =================
@login_required
def download_backup(request):
    import csv
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="backup.csv"'
    writer = csv.writer(response)
    writer.writerow(["title","category","type","amount","date","note"])
    for t in Transaction.objects.filter(user=request.user):
        writer.writerow([t.title, t.category, t.type, t.amount, t.date, t.note])
    return response

# ================= RESTORE BACKUP =================
@login_required
def restore_backup(request):
    if request.method == "POST" and request.FILES.get("file"):
        import csv, io
        file = request.FILES["file"]
        decoded = file.read().decode("utf-8")
        reader = csv.reader(io.StringIO(decoded))
        next(reader)  # skip header
        for row in reader:
            Transaction.objects.create(
                user=request.user,
                title=row[0],
                category=row[1],
                type=row[2],
                amount=row[3],
                date=row[4],
                note=row[5] if len(row) > 5 else ""
            )
        return redirect("/backup/?msg=restored")
    return redirect("/backup/")