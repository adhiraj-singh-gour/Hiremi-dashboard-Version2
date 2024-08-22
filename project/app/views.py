from django.shortcuts import render,redirect
from django.contrib.auth import  login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import random
from django.core.mail import send_mail

# =======================================================================================================
# =======================================================================================================
def index(request):
    return render(request, 'index.html')

def otp_page(request):
    return render(request, 'otp-page.html')

@login_required
def superuser_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('superuser_login')


def superuser_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(email,password)

        if user is not None and user.is_superuser:
            # Generate a random OTP
            otp = random.randint(100000, 999999)
            
            # Save the OTP in the session
            request.session['otp'] = otp
            request.session['superuser_email'] = email

            # Send OTP to the superuser's email
            send_mail(
                'Your OTP for Login',
                f'Your OTP is {otp}',
                'adhirajsingh31032003@gmail.com',  # Replace with your "from" email
                [email],
                fail_silently=False,
            )
            print(otp)

            # Redirect to OTP verification page
            return redirect('otp_page')  # Replace with the name of your OTP page URL
        else:
            messages.error(request, 'Invalid email or password for superuser.')
            print(messages)
    
    return render(request, 'index.html')


def otp_verify(request):
    if request.method == 'POST':
        otp_digits = [
            request.POST.get('digit1'),
            request.POST.get('digit2'),
            request.POST.get('digit3'),
            request.POST.get('digit4'),
            request.POST.get('digit5'),
            request.POST.get('digit6')
        ]
        print(otp_digits)
        entered_otp = ''.join(otp_digits)
        session_otp = str(request.session.get('otp'))

        if entered_otp == session_otp:
            email = request.session.get('superuser_email')
            user = authenticate(request, username=email, password="admin")

            if user is not None:
                login(request, user)
                # Clean up session data
                del request.session['otp']
                del request.session['superuser_email']

                # Redirect to the dashboard instead of rendering directly
                return redirect('dashboard')  # Update with your actual dashboard URL or name
            else:
                messages.error(request, 'Unable to authenticate. Please try again.')
        else:
            # OTP is incorrect
            messages.error(request, 'Invalid OTP. Please try again.')

    # If OTP is incorrect or request method is GET
    return render(request, 'otp-page.html')


def resend_otp(request):
    if 'superuser_email' in request.session:
        email = request.session['superuser_email']  
        otp = random.randint(100000, 999999) 
        print(email)
        request.session['otp'] = otp
        send_mail(
            'Your Resent OTP for Login',
            f'Your OTP is {otp}',
            'adhirajsingh31032003@gmail.com',
            [email],
            fail_silently=False,
        )
        print(f"Resent OTP: {otp}")
        messages.success(request, 'A new OTP has been sent to your email.')
        return redirect('otp_page') 
    messages.error(request, 'Unable to resend OTP. Please try logging in again.')
    return redirect('superuser_login')  

# ============================================================================================================
# ============================================================================================================


#                                           Dashboard Section Started
# ============================================================================================================
# ============================================================================================================


def dashboard(request):
    return render(request,"dashboard.html")

def mentorship(request):
    return render(request,"mentorship.html")

def internship(request):
    return render(request,"internship.html")

def fresher_Job(request):
    return render(request,"fresher-job.html")

def corporate_training(request):
    return render(request,"corporate-training.html")
