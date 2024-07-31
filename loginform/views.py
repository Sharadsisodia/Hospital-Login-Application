from django.http import HttpResponse
from django.shortcuts import render
from formlogin.models import patient,doctor

def logIn(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request,"signupForm.html")

def loginpage(request):
    # doctor = get_object_or_404(doctor, username=username)
    # patient = get_object_or_404(patient, username=username)
    if request.method=='POST':
        patientData=patient.objects.all()
        doctorData=doctor.objects.all()
        r_role=request.POST.get('role')
        client_username=request.POST.get('username')
        client_Password=request.POST.get('password')
        if(r_role=='patient'):
            for da in patientData:
                if(da.p_Username==client_username and da.p_Password==client_Password):
                    context = {
                        'logged_in': "Patient",
                        'first_name': da.p_Firstname,
                        'last_name': da.p_Lastname,
                        'profile_picture': da.p_Picture.url,
                        'username': da.p_Username,
                        'email': da.p_EmailId,
                        'address_line1': da.p_AddressLi,
                        'city': da.p_City,
                        'state': da.p_State,
                        'pincode': da.p_Pincode
                        }
                    return render(request, 'loginPage.html', context)
        else:
            for da in doctorData:
                if(da.d_Username==client_username and da.d_Password==client_Password):
                    context = {
                        'logged_in': "Doctor",
                        'first_name': da.d_Firstname,
                        'last_name': da.d_Lastname,
                        'profile_picture': da.d_Picture.url,
                        'username': da.d_Username,
                        'email': da.d_EmailId,
                        'address_line1': da.d_AddressLi,
                        'city': da.d_City,
                        'state': da.d_State,
                        'pincode': da.d_Pincode
                        }
                    return render(request, 'loginPage.html', context)
        print("Incorrect username or password")
        context={
            'incorrectPass':'Incorrect username or password'
        }
        return render(request, 'index.html',context)


def signupComp(request):
    if request.method=='POST':
        patientData=patient.objects.all()
        doctorData=doctor.objects.all()

        f_name=request.POST.get('firstName')
        l_name=request.POST.get('lastName')
        picture=request.FILES.get('profilePicture')
        userName=request.POST.get('username')
        eMail=request.POST.get('email')
        password=request.POST.get('password')
        addr1=request.POST.get('addressLine1')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        role=request.POST.get('role')


        if role=='patient':
            for da in patientData:
                if(da.p_Username!=userName):
                    entryData=patient(p_Firstname=f_name, p_Lastname=l_name, p_Picture=picture, p_Username=userName, p_EmailId=eMail, p_Password=password, p_AddressLi=addr1, p_City=city, p_State=state, p_Pincode=pincode)
                    entryData.save()
                    return render(request,"signupComp.html")
            context={
                'usernameExist':'Username already exist, Try using with different username'
            }
            return render(request, 'signupForm.html',context)
        else:
            for da in doctorData:
                if(da.d_Username!=userName):
                    entryData=doctor(d_Firstname=f_name, d_Lastname=l_name, d_Picture=picture, d_Username=userName, d_EmailId=eMail, d_Password=password, d_AddressLi=addr1, d_City=city, d_State=state, d_Pincode=pincode)
                    entryData.save()
                    return render(request,"signupComp.html")
            context={
                'usernameExist':'Username already exist, Try using with different username'
            }
            return render(request, 'signupForm.html',context)
