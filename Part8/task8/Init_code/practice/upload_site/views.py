from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.forms.models import model_to_dict

# Create your views here.




def login(request):
    return render(request,'login.html',locals())

def identifying(request):
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    c = User.objects.filter(user = user,pwd = pwd).count()
    if c==0:
        return HttpResponse('登陆失败')
    else:
        authoritys = User.objects.filter(user=user, pwd=pwd)
        authority = model_to_dict(authoritys[0])['authority']  #fitler查询结果是记录列表，用索引0取第一条记录
        return render(request,'imagelist.html',locals())

def submit(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    imagelist = imagefile.objects.values()
    return render(request,'submit_image.html',locals())

def success(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    return render(request,'success.html',locals())

#接收图片的接口
def receive(request):
    user = request.POST.get('user')
    authority = request.POST.get('authority')
    pwd = request.POST.get('pwd')
    rec_image_list = request.FILES.getlist('upload_file')
    for rec_image in rec_image_list:
        with open(f'upload_site/static/image/{rec_image.name}','wb') as f:
            f.write(rec_image.read())
            image_file = imagefile(imagename = rec_image,labelnote="否")
            image_file.save()
    return render(request,'success.html',locals())



def show_picture(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    imageName = request.GET.get('imageName')
    x1 = request.GET.get('x1')
    y1 = request.GET.get('y1')
    x2 = request.GET.get('x2')
    y2 = request.GET.get('y2')
    Label = request.GET.get('Label')
    if authority=='manager' or authority=='checker':
        c = Imagelabel.objects.filter(imagename=imageName).count()
        if c == 0:
            labellist = Imagelabel.objects.filter(imagename='无标注')
        else:
            labellist = Imagelabel.objects.filter(imagename=imageName)

    if  authority=='marker':
        c = Imagelabel.objects.filter(imagename=imageName,user=user).count()
        if c == 0:
            labellist = Imagelabel.objects.filter(imagename='无标注')
        else:
            labellist = Imagelabel.objects.filter(imagename=imageName,user=user)

    return render(request,'show.html',locals())

def show_imagelist(request):
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    c = User.objects.filter(user=user, pwd=pwd).count()
    if c == 0:
        return HttpResponse('登陆失败')
    else:
        authoritys = User.objects.filter(user=user)
        authority = model_to_dict(authoritys[0])['authority']  # fitler查询结果是记录列表，用索引0取第一条记录
        if authority == 'manager':
            imagelist = imagefile.objects.values()
        if authority == 'checker':
            imagelist = imagefile.objects.values()
        if  authority == 'marker':
            imagelist = Userimgae.objects.filter(user=user)
        return render(request, 'imagelist.html', locals())


def distribute(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    users = User.objects.values()
    imagelist = imagefile.objects.values()
    return render(request, 'distribute.html', locals())

def Labelimage(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    imageName = request.GET.get('imageName')
    return render(request, 'Labelimage.html',locals())

def savelabel(request):
    user = request.POST.get('user')
    authority = request.POST.get('authority')
    pwd = request.POST.get('pwd')
    label_id = request.POST.get('label_id')
    imagename = request.POST.get('imagename')
    labelnote = request.POST.get('labelnote')
    x1 = request.POST.get('x1')
    y1 = request.POST.get('y1')
    x2 = request.POST.get('x2')
    y2 = request.POST.get('y2')
    label = request.POST.get('label')

    c = Imagelabel.objects.filter(id=label_id).count()
    if c==0:
        Imagelabel(imagename=imagename, x1=x1, y1=y1, x2=x2, y2=y2, label=label,user=user).save()
        imagefile.objects.filter(imagename=imagename).update(labelnote=labelnote)
        Userimgae.objects.filter(imagename=imagename,user=user).update(labelnote=labelnote)
    else:
        Imagelabel.objects.filter(id=label_id).update(imagename=imagename,x1=x1, y1=y1, x2=x2, y2=y2, label=label,user=user)
    return render(request,'success.html',locals())

def deletelabel(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    label_id = request.GET.get('label_id')
    Imagelabel.objects.filter(id = label_id).delete()
    return render(request,'success.html',locals())

def reviselabel(request):
    user = request.POST.get('user')
    authority = request.POST.get('authority')
    pwd = request.POST.get('pwd')
    label_id = request.GET.get('label_id')
    imagename = request.GET.get('imageName')
    x1 = request.GET.get('x1')
    y1 = request.GET.get('y1')
    x2 = request.GET.get('x2')
    y2 = request.GET.get('y2')
    label = request.GET.get('Label')
    return render(request, 'reviselabel.html', locals())

def savedistribute(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    message = request.GET.values() #接收所有输入
    a = 0
    for i in message:
        if a<3:
            pass
        elif a==3:
            user1 = i
        else:
            imagename = i
            Userimgae(user=user1,imagename=imagename,labelnote='否').save()
        a+=1
    return render(request,'success.html',locals())

def manageusers(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    users = User.objects.values()
    return render(request, 'manageusers.html', locals())

def savemanageusers(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    newuser = request.GET.get('newuser')
    newauthority = request.GET.get('newauthority')
    newpwd = request.GET.get('newpwd')
    n = User.objects.filter(user=newuser).count()
    if n==0:
        User(user=newuser, pwd=newpwd, authority=newauthority).save()
        return render(request, 'success.html', locals())
    else:
        User.objects.filter(user=newuser).update(pwd=newpwd, authority=newauthority)
        return render(request, 'success.html', locals())

def warn(request):
    user = request.GET.get('user')
    authority = request.GET.get('authority')
    pwd = request.GET.get('pwd')
    warn = request.GET.get('warn')
    label_id = request.GET.get('label_id')
    if warn=='警告':
        Imagelabel.objects.filter(id=label_id).update(warn="警告")
    else:
        Imagelabel.objects.filter(id=label_id).update(warn="无警告")
    return render(request, 'success.html', locals())