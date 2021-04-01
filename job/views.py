from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from.models import*
from django.contrib.auth import authenticate,login,logout
from datetime import date
# Create your views here.
def Index (request):
    return render(request,'index.html')

def admin_login(request):
    error = ''
    if request.method == 'POST':
        un = request.POST['uname']
        up = request.POST['pwd']
        user = authenticate(username=un, password=up)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error='yes'
    d = {'error':error}
    return render(request,'admin_login.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return render('/admin_login/')
    return render(request,'admin_home.html')



def user_login(request):
    error = ''
    if request.method=='POST':
        un = request.POST['uname']
        up = request.POST['pwd']
        user = authenticate(username=un,password=up)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == 'student':
                    login(request,user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'user_login.html',d)


def recruiter_login(request):
    error = ''
    if request.method == 'POST':
        un = request.POST['uname']
        up = request.POST['pwd']
        user = authenticate(username=un, password=up)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == 'recruiter'and user1.status!='pending':
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}

    return render(request,'recruiter_login.html',d)


def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        img = request.FILES['image']
        pw = request.POST['Pwd']
        em = request.POST['uemail']
        con = request.POST['cnumber']
        gen = request.POST['gender']
        cn = request.POST['company']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pw)
            Recruiter.objects.create(user=user, mobile=con, gender=gen,company=cn, image=img, type="recruiter",status='pending')
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'recruiter_signup.html', d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter_login/')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        gen = request.POST['gender']
        con = request.POST['cnumber']

        recruiter.user.first_name=fn
        recruiter.user.last_name=ln
        recruiter.gender = gen
        recruiter.mobile = con
        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            recruiter.image=i
            recruiter.save()
        except:
            pass
    d = {'error': error,'recruiter':recruiter}
    return render(request,'recruiter_home.html',d)


def user_signup(request):
    error=""
    if request.method=='POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        img = request.FILES['image']
        pw = request.POST['Pwd']
        em = request.POST['uemail']
        con = request.POST['cnumber']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name = fn,last_name=ln,username=em,password=pw)
            StudentUser.objects.create(user=user,mobile=con,gender=gen,image=img,type="student")
            error="no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'user_signup.html',d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('/user_login/')
    user=request.user
    student = StudentUser.objects.get(user=user)
    error=""
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        gen = request.POST['gender']
        con = request.POST['cnumber']

        student.user.first_name = fn
        student.user.last_name = ln
        student.gender = gen
        student.mobile = con
        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            student.image = i
            student.save()
        except:
            pass
    d = {'error': error, 'student': student}
    return render(request,'user_home.html',d)


def user_logout(request):
    logout(request)
    return redirect('index')


def view_users(request):
    if  not request.user.is_authenticated:
        return redirect('/admin_login/')
    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request,'view_users.html',d)


def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('/admin_login/')
    student = User.objects.get(id=pid)
    student.delete()
    return render(request,'view_users.html')

def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('/admin_login/')
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('/all_recruiter/')


def pending_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('/admin_login/')
    data = Recruiter.objects.filter(status='pending')
    d =  {'data':data}
    return render(request,'pending_recruiter.html',d)


def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('/admin_login/')
    error = ""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        recruiter.status=s
        try:
            recruiter.save()
            error="no"
        except:
            error = "no"
    d =  {'recruiter':recruiter,"error":error}
    return render(request,'change_status.html',d)

def accept_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('/admin_login/')
    data = Recruiter.objects.filter(status='Accept')
    d = {'data':data}
    return render(request,'accept_recruiter.html',d)

def reject_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('/admin_login/')
    data = Recruiter.objects.filter(status='Reject')
    d = {'data':data}
    return render(request,'reject_recruiter.html',d)

def all_recruiter(request):
    if not request.user.is_staff:
        return redirect('/admin_login/')
    data = Recruiter.objects.all()
    d = {'data':data}
    return render(request,'all_recruiter.html',d)

def change_admin_pass(request):
    if not request.user.is_authenticated:
        return redirect('/admin_login/')
    error = ""
    if request.method=='POST':
        c = request.POST['cpass']
        n = request.POST['npass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'change_admmin_pass.html',d)

def user_change_pass(request):
    if not request.user.is_authenticated:
        return redirect('/user_login/')
    error = ""
    if request.method=='POST':
        c = request.POST['cpass']
        n = request.POST['cnpass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error="not"
        except:
            error = "yes"
    d = {"error":error}
    return render(request,'user_change_pass.html',d)


def recruiter_change_pass(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter_login.html/')
    error = ""
    if request.method =='POST':
        c = request.POST['cpass']
        n = request.POST['cnpass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error = "yes"
    d = {"error":error}
    return render(request,'recruiter_change_pass.html',d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter_login/')
    error = ""
    if request.method == 'POST':
        t = request.POST['jtitle']
        e = request.POST['jexperience']
        i = request.FILES['jimage']
        s = request.POST['jsalary']
        sk = request.POST['jskill']
        d = request.POST['jdis']
        sd = request.POST['jsdate']
        ed = request.POST['jedate']
        l = request.POST['jlocation']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        print(recruiter)
        print(user)
        print(t)
        try:
            Job.objects.create(recruiter=recruiter, satart_date=sd, end_date=ed, title=t, salary=s, skills=sk,
                               discription=d, experience=e, location=l, post_date=date.today(), image=i)
            error = "no"
        except:
            error = "yes"
        print(error)
    d = {'error': error}
    return render(request, 'add_job.html', d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('/recruiter_login/')
    user = request.user
    print(user)
    recruiter = Recruiter.objects.get(user=user)
    print(recruiter)
    data = Job.objects.filter(recruiter=recruiter)
    print(data)
    d = {'data':data}

    return render(request,'job_list.html',d)


def edit_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('/recruiter_login/')
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['jtitle']
        e = request.POST['jexperience']
        s = request.POST['jsalary']
        sk = request.POST['jskill']
        d = request.POST['jdis']
        l = request.POST['jlocation']

        job.title=jt
        job.experience = e
        job.salary = s
        job.skills = sk
        job.discription = d
        job.location = l

        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        print(error)
    d = {'error': error,'job':job}
    return render(request, 'edit_jobdetail.html', d)

def user_joblist(request):
    if not request.user.is_authenticated:
        return redirect('/user_login.html/')
    data = Job.objects.all()


    d = {'data':data}
    return render(request,'user_joblist.html',d)


def delete_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('/recruiter_login/')
    data = Job.objects.get(id=pid)
    print(data)
    data.delete()
    return redirect('/job_list/')

