#!/usr/bin/python


import urllib, urllib2, time, os, sys
from datetime import *

def get_fetch_list(h_s, h_e, t):
	l = []
	if t == '1': r = 5
	elif t == '2': r = 30
	for h in range(h_s, h_e):
		for m in range(0, 60, r):
			l.append('%02d%02d'%(h, m))
	return l


def fetch_save_img(name, date, t):
	save_path = save_dir + date
	remote_path = url[t]%(date+name)
	print date, name, '...'
	print remote_path
	if not os.path.exists(save_path):
		os.mkdir(save_path)
	if urllib.urlopen(remote_path).info().getheader('Content-Type') in ('image/gif', 'image/jpeg'):
		urllib.urlretrieve(remote_path, save_path+'/'+name+postfix[int(t)-1])
		print 'Success'
	else:
		print 'Fail'


save_dir = './images/'

url = {'1':'http://i.weather.com.cn/i/product/pic/l/sevp_aoc_rdcp_sldas_ebref_az9451_l88_pi_%s00000.gif', '2':'http://i.weather.com.cn/i/product/pic/l/sevp_nsmc_wxcl_asc_e99_achn_lno_py_%s00000.jpg'}

a_day = timedelta(days=2)
now = datetime.now()
now -= a_day
date = now.strftime('%Y%m%d')
ts = ('1', '2')
postfix = ('.gif', '.jpg')
h_s, h_e = 0, 24

if len(sys.argv) == 2:
	ts = (sys.argv[1])
	print ts
if len(sys.argv) >= 3:
	date = sys.argv[1]
	ts = (sys.argv[2])
	print ts
if len(sys.argv) == 4:
	h_s, h_e = int(sys.argv[3]), int(sys.argv[4])

for t in ts:
	save_dir = save_dir + t + '/'
	ss = get_fetch_list(h_s, h_e, t)
	print ss
	for name in ss:
		fetch_save_img(name, date, t)





