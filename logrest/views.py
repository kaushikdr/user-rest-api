from django.shortcuts import render
from logrest.forms import SignUpForm,LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf

from rest_framework import generics
from logrest.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters

import pdb

# Create your views here.

def signup(request):
	if request.POST:
		form = SignUpForm(request.POST)
		
		if form.is_valid():
			form.save()
			context = {'form':form, 'success':True}
			return render(request, 'logrest/signup.html', context)
	form = SignUpForm()
	context = {'form':form, 'success':False}
	return render(request, 'logrest/signup.html', context)


def logout(request):
	#pdb.set_trace()
	auth.logout(request)
	request.session = {}
	return HttpResponseRedirect('/user/login')
'''
def login(request):
	if request.POST:
		#pdb.set_trace()
		form = LoginForm(request.POST)
		user = auth.authenticate(username=form.data['username'], password=form.data['password'])
		if user:
			auth.login(request, user)
			context = {'form':'success'}
			context.update(csrf(request))
			return render(request,'logrest/login.html',context)
	form = LoginForm()
	context = {'form':form}
	return render(request, 'logrest/login.html',context)
'''


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)

class LoginView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
'''
class SignUpView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter,)
'''