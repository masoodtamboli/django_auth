from django.shortcuts import render, HttpResponse, redirect
import pyrebase

# Firebase Config to access firebase services
firebaseConfig = {
  "apiKey": "AIzaSyB7FIGlPJoQ12SdkKNOS5hBZ4lrWExWcZU",
  "authDomain": "djangoapp-2a443.firebaseapp.com",
  "projectId": "djangoapp-2a443",
  "storageBucket": "djangoapp-2a443.appspot.com",
  "messagingSenderId": "324656338359",
  "appId": "1:324656338359:web:dccf836731140e71c38432",
  "measurementId": "G-6EN8VWKM7W",
  "databaseURL": "https://djangoapp-2a443-default-rtdb.firebaseio.com"
}

# Initializing Firebase config and accessing services
firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

# Create your views here.

# When '' blank is accessed show it index.html page
def index(request):
    return render(request, 'index.html')

# when submit button clicked handle signin
def handleSignIn(request):
    if request.method == 'POST':
        #get the post Params
        email = request.POST.get('emailId', False)
        password = request.POST.get('password', False)

        try:
            user = authe.sign_in_with_email_and_password(email, password)
        except:
            msg = "Invalid Credentials!"
            return redirect(request, 'index.html',{"message":msg})
        
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        return render(request, 'Home.html', {"eml": email})
    else:
        return HttpResponse('404 - Not Found')

def logout(request):
    try:
        del request.session['uid']
    except Exception as e:
        print(e)
    return render(request,"index.html")