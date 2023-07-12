from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_def):
    def wrapper(req , *args, **kwargs):
            if req.user.is_authenticated :
                return redirect("profil")
            else:
                return view_def(req,*args,**kwargs)

    return wrapper


def allowed_users(allowed_roles = []): # can give me an access to all statement in function 
    print(allowed_roles)
    def decorator(view_def):
        def wrapper(req,*args,**kwargs):

            if req.user.groups.exists():
                group = req.user.groups.all()[0].name
            if group in allowed_roles:
                return view_def(req,*args,**kwargs)
            else:
                return HttpResponse("this user is not allowed to access in this page")
        return wrapper
    return decorator


