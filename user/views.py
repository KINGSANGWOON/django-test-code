from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
# from user.models import Users
from user.models import Users
# Create your views here.

def index(request): # django에게 미들웨어에가 명시적으로 request를 넘겨준다
    user = Users.objects.filter(username="admin").first() #orm공부해서 적기
    email = user.email if user else "Anonymous User!!"  # object를 가지고 와서 만약 있으면 그 user의 값을 아니면 Anonymous User!! 값을 넣어준다
    print(email)
    print(request.user.is_authenticated)
    # if request.user.is_authenticated is False:
    #     email = "Anonymous User!"
    #     print(email)
    return render(request, "base.html", {"welcome_msg":f"Hello {email}!" , "hello":"world"}) # 말그대로 return값이다 base.html에 welcome_msg부분을 Hello {이메일}을 넣어서
    # 요청이 들어 왔을 때, html 파일을 가지고 redering하기 전에, {"welcome_msg":f"Hello {email}!" , "hello":"world"} 이 값을 넣어주고 렌더링을 해준다.  

def redirect_test(request):
    print("Go Redirect")
    return redirect("index_1")
    #user가 로그인을 하지않고 로그인을 해야 사용할 수 있는 페이지에 접근했을 때 redirect해준다

@csrf_exempt
def get_user(request,user_id):
    print(user_id)
    if request.method == "GET":
        abc = request.GET.get("abc")  #request 의 GET 부분에서 GET 전송 부분이에서 abc라는 key 값을 가진 value 값을 가지고 온다 get은 함수이다 
        xyz = request.GET.get("xyz")  #예) localhost:8000/get_user/1?abc=123&xzy=098  #파싱해줌
        user = Users.objects.filter(pk=user_id).first()  
        return render(request,"base.html",{"user":user,"params":[abc,xyz]}) #user의 객체를 받으면 그 객체가 자동으로 username을 리턴한다 만약 username이라고 하고 싶으면 username이라고 치면된다
    elif request.method == "POST":
        username = request.GET.get("username")
        if username:
            user = Users.objects.filter(pk=user_id).update(username=username)  # username의 값을 변경해 준다 짜피 같은 이름
            #쿼리 스트링을 username = 본인이 바꾸고 싶은 이름을 적어주면 이름이 바뀐다
        return JsonResponse(status= 201,data= dict(msg="You just reached with Post Method!") ,safe=False) #jsonresponse는 사용하긴 했지만 개인적인 공부가 필요함
        #if 문이 끝난다음에 