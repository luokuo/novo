from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
#限制接口调用的次数，可以根据ip限制，根据时间限制等等
from ratelimit.decorators import ratelimit

from user.forms import LoginForm


class UserLogin(View):
	def get(self, request):
		# 判断用户是否记住用户名
		username = request.COOKIES.get('username')
		checked = 'checked'
		if username is None:
			username = ''
			checked = ''

		return render(request, "login.html", {'username': username, 'checked': checked})

	@ratelimit(key='ip', rate = '5 / m')
	@ratelimit(key='post：username', rate = '5 / m')
	@ratelimit(key='post：password', rate = '5 / m')
	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('pwd')
		remember = request.POST.get('remember', None) #没有记住用户名则设为None
		#参数校验
		if not all([username, password]):
			return render(request, 'login.html', {'errmsg': '参数不完整'})
		#登陆校验
		user = authenticate(username=username, password=password)
		if user is not None:
			# 记住用户的登录状态
			login(request, user)
			#获取用户登陆之前访问的url地址，默认跳转到首页
			next_url = request.GET.get('next', reverse('index'))
			response = redirect(next_url)
			if remember == 'on':
				response.set_cookie('username', username, max_age=7 * 24 * 3600)
			else:
				response.delete_cookie('username')
			return response
		else:
			return render(request, 'login.html', {'errmsg': '用户名或密码错误'})



class LogoutView(View):
	def get(self, request):
		# 清除用户登录状态,内置的logout函数会自动清除当前session
		logout(request)
		return redirect(reverse('user:login'))
