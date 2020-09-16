from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    # print(request.scheme)
    # print(request.method)
    # print(request.GET)
    # print(request.POST)
    # print(request.path) # http://127.0.0.1/index?name=xiaoming则返回/index
    # print(request.get_host())   # # http://127.0.0.1/index?name=xiaoming则返回127.0.0.1
    # print(request.get_port())   # http://127.0.0.1/index?name=xiaoming则返回80
    # print(request.get_full_path)    # http://127.0.0.1/index?name=xiaoming则返回/index?name=xiaoming
    return HttpResponse("this is index page")


def test_get(request):
    # name = request.GET['name']
    name = request.GET.get('name')
    age = request.GET.get('age')
    return HttpResponse("name="+name+"<br />"+"age="+age)


def test_post(request):
    print(request.method)

    # 当name对应多个值时，get('name')会获取最新的值
    # name = request.POST.get('name')

    # 当一个key对应多个值时，可以使用getlist(key)方法获取到所有值的列表
    # namelist = request.POST.getlist('name')

    # 当一个key对应多个值时，items或取最新值
    # items = request.POST.items()
    # for data in items:
    #     print(data)

    list = request.POST.lists()
    for data in list:
        print(data)     # ('name', ['xiaoming', 'xiaoli']) ('age', ['20'])

    age = request.POST.get('age')
    return HttpResponse("name="+str(data)+" age="+age)


def ads(request):
    return render(request, 'index.html')


def hostlist(request):
    return render(request, 'hostlist.html')


def testUrl(request, year, month, day):
    return HttpResponse("日期:" + year + "-" + month + "-" + day)


def login(request):
    return render(request, "login.html")


def login_check(request):
    if request.GET.get('username') != '':
        username = request.POST.get('username')
    if request.GET.get('password') != '':
        password = request.POST.get('password')
    print(username,password)
    if username == 'root' and password == '123':
        result = 'Login success'
    else:
        result = 'username or password is wrong'
    return HttpResponse(result)





























