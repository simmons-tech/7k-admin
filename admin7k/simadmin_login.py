from django.conf import settings

def simadmin_staff_required(f):
    def new_f():
        print
        f()
    return new_f
