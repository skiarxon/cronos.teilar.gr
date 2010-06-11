# -*- coding: utf-8 -*-

from cronos.announcements.models import *
from cronos.declaration.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def declaration(request):
	msg = ''
	summary = ''
	declaration_lessons = []
	try:
		declaration_full = request.user.get_profile().declaration.split(',')
		i = 3
		summary = declaration_full[:i]
		while i <= len(declaration_full) - len(summary):
			declaration_lessons.append(declaration_full[i:i+6])
			i += 6
	except:
		msg = 'Η δήλωσή σας είναι κενή'
		pass

	return  render_to_response('declaration.html', {
			'summary': summary,
			'declaration_lessons': declaration_lessons,
			'msg': msg,
		}, context_instance = RequestContext(request))
