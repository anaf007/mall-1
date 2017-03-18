#coding=utf-8

from flask import render_template
def url(url,message,location):
	return render_template('success.html',url=url,\
		message=message,location=location)