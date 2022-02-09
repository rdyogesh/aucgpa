from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    if(request.method == 'GET'):
        return render(request,'index.html')
    else:
        dept = request.POST.get("dept")
        sem = request.POST.get("sem")
        data = models.subjects.objects.filter(dept=dept,sem=sem)
        cnt=1
        resp={}
        for i in data:
            resp[str(cnt)] = {'subcode':i.subcode,'subject_name':i.subject_name,'credit':i.credits}
            print(resp[str(cnt)])
            cnt+=1
        return render(request,'gpacalculator.html',{'resp':resp,'cnt':cnt})

def calculategpa(req):
        cnt=int(req.POST.get("cnt"))
        credit=0
        sum=0
        for i in range(1,cnt):
            grade = int(req.POST.get("grade"+str(i)))
            print(grade)
            if(grade>=5):
                c = int(req.POST.get("credit"+str(i)))
                sum+=(c*grade)
                credit+=c
        gpa=sum/credit
        print(sum,credit,gpa)
        return render(req,'result.html',{'mark':gpa,'msg':" - your  GPA."})