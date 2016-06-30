from django.http import HttpResponse
import hashlib

def userInfo(request):
    User.objects.filter(user_id=request.GET.get('user_id'))
    return 


def saveUserInfo(request):
    # extract info
    post = request.POST
    if post.__contains__('user_name'):
        name = post.get('user_name')
    try:
        user = User.objects.get_or_create(user_name=name)
    except ObjectDoesNotExist:
        return 403

    pwd = hashlib.md5(post.get('password').hexdigest()
    user, created = User(user_name=name, password=pwd, profile=post.get('profile'), c_time = datetime.datetime.now(), m_time = datetime.datetime.now())
    
    # save
    user.save()
    return 200;
