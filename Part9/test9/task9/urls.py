from django.urls import path
from . import views


urlpatterns=[
    path('',views.login),
    path('identifying/',views.identifying),
    path('submit/',views.submit),
    path('receive/',views.receive),
    path('success/',views.success),
    path('showimage/',views.show_picture),
    path('showlist/',views.show_imagelist),
    path('labelimage/',views.Labelimage),
    path('savelabel/',views.savelabel),
    path('deletelabel/',views.deletelabel),
    path('reviselabel/',views.reviselabel),
    path('distribute/',views.distribute),
    path('savedistribute/',views.savedistribute),
    path('manageusers/',views.manageusers),
    path('savemanageusers/',views.savemanageusers),
    path('warn/',views.warn),
    path('register/',views.register),
    path('retrievepassword/',views.retrievepassword),
    path('test/',views.test),
]