from django.shortcuts import render

# Create your views here.
from .models import StudentWallet, WalletTransaction

def save_money(request, student_id, amount):
    student_wallet = StudentWallet.objects.get(student_id=student_id)
    student_wallet.balance += amount
    student_wallet.save()
    WalletTransaction.objects.create(wallet=student_wallet, amount=amount, transaction_type='credit')
    return render(request, 'success.html', {'message': 'Money saved successfully.'})

def pay_school_fees(request, student_id, amount):
    student_wallet = StudentWallet.objects.get(student_id=student_id)
    if student_wallet.balance >= amount:
        student_wallet.balance -= amount
        student_wallet.save()
        WalletTransaction.objects.create(wallet=student_wallet, amount=amount, transaction_type='debit')
        return render(request, 'success.html', {'message': 'School fees paid successfully.'})
    else:
        return render(request, 'error.html', {'message': 'Insufficient funds in the wallet.'})


def pay_acceptance_fee(request, student_id, amount):
    student_wallet = StudentWallet.objects.create(student_id=student_id, balance=0.00)
    student_wallet.balance += amount
    student_wallet.save()
    WalletTransaction.objects.create(wallet=student_wallet, amount=amount, transaction_type='credit')
    return render(request, 'success.html', {'message': 'Acceptance fee paid successfully. Wallet created.'})


# Student Self Service Portal
def view_results(request, student_id):
    student = Student.objects.get(id=student_id)
    if student.has_fees_cleared and ResultApproval.objects.filter(student=student, is_approved=True).exists():
        # Logic to display results
        return render(request, 'results.html', {'results': student.results})
    else:
        return render(request, 'error.html', {'message': 'Fees not cleared or results not approved.'})

def borrow_book(request, student_id, book_id):
    student = Student.objects.get(id=student_id)
    book = LibraryBook.objects.get(id=book_id)
    if book.is_borrowed:
        return render(request, 'error.html', {'message': 'Book is already borrowed.'})
    book.is_borrowed = True
    book.save()
    return render(request, 'success.html', {'message': 'Book borrowed successfully.'})

def return_book(request, student_id, book_id):
    student = Student.objects.get(id=student_id)
    book = LibraryBook.objects.get(id=book_id)
    if book.is_borrowed:
        book.is_borrowed = False
        book.save()
        return render(request, 'success.html', {'message': 'Book returned successfully.'})
    else:
        return render(request, 'error.html', {'message': 'Book is not borrowed.'})

def manage_clearance(request, student_id):
    student = Student.objects.get(id=student_id)
    student_involvements = StudentInvolvement.objects.filter(student=student)
    for involvement in student_involvements:
        involvement.is_cleared = True
        involvement.save()
    return render(request, 'success.html', {'message': 'Clearance granted for all involvements.'})
