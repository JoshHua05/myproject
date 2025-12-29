from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('deleteRegistration/<delReg_id>',views.deleteRegistration, name='deleteRegistration'),
    path('updateRegistration/<updateReg_id>',views.updateRegistration, name='updateRegistration'),
    path('registration/',views.registration, name='registration'),
    path('about/',views.about, name='about'),
    path('cycle/',views.cycle, name='cycle'),
    path('createCycle/',views.createCycle, name='createCycle'),
    path('deleteCycle/<cycle_id>',views.deleteCycle, name='deleteCycle'),
    path('mtf/',views.mtf, name='mtf'),
    path('createMtf/',views.createMtf, name='createMtf'),
    path('deleteMtf/<mtf_id>',views.deleteMtf, name='deleteMtf'),
    path('updateMtf/<mtf_id>',views.updateMtf, name='updateMtf'),
    path('pc/',views.pc, name='pc'),
    path('createPc/',views.createPc, name='createPc'),
    path('deletePc/<pc_id>',views.deletePc, name='deletePc'),
    path('updatePc/<pc_id>',views.updatePc, name='updatePc'),
    path('purpose/',views.purpose, name='purpose'),
    path('login/',views.login_user, name='login_user'),
    path('logout/',views.logout_user, name='logout_user'),
    path('register/',views.register_user, name='register_user'),
]
