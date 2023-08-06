#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ By Lukman And The•SQUAD team Project
# Update V1.6
_auth01_ = 'Lukman-xd'

# Author : Lukmanul Hakim.
# Facebook (Lukman X Udin)   : Facebook.com/Dapunta.Khurayra.X
# Instagram (☬ 𝐀𝐧𝐨𝐧𝐲𝐦 𝟒𝟎𝟒 ☬)    : Instagram.com/ratya.anonym.id
# Whatsapp (Dapunta Bot_Key)      : +6282245780524

# Recode SC Orang Itu Gak Keren Bro
# Lu Gaakan Bisa Berkembang Kalau Skillu Cuma Recode
# Gaada Yg Susah Selama Lu Mau Belajar & Berusaha
# Jangan Sampai Lu Jual File Source Code Ini !

### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

### Perumpamaan Module & Syntax
req_ses = requests.Session()
req_get = requests.get
req_post = requests.post
js_lo = json.loads
lukman_p = print
lukman_i = input
lukman_o = open
lukman_e = exit

### Warna
Z = "\x1b[0;90m" # Hitam
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
BM = '\x1b[1;101m' # Belajang Merah

### Host & Penampungan
host = "https://mbasic.facebook.com"
id = []
cp = 0
ok = 0
uid = []
id2 = []
loop = 0
akun = []
method = []
tokenku = []
taplikasi = []
lisensiku = []
lisensikuni = []
m_fb = "https://m.facebook.com/"
web_fb = "https://www.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36"

### Waktu & Tanggal
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tanggal = ("%s-%s-%s"%(tgl,bln,thn))

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

### Clear Login Session
def bersih():
    try:os.remove('Data/token.txt')
    except:pass
    try:os.remove('Data/cookies.txt')
    except:pass

### Display Text
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

### Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
    
class open_role:
	def __init__(self):
		global tiktok,pupuk,puput
		try:
			tiktok = open("Data/token.txt","r").read()
		except:pass
		try:
			pupuk = open("Data/cookies.txt","r").read()
			puput = {'cookie':pupuk}
		except:pass

### Logo
def banner():
	clear()
	logo_line_1 = ("%s    ____           __          __                "%(O))
	logo_line_2 = ("%s   / __/___ ______/ /_  ____  / /__ ╔══════════════════════╗"%(O))
	logo_line_3 = ("%s  / /_/ __ `/ ___/ __ \/ __ \/ //_/ ║%s  Code By Lukman Xd   %s║"%(O,P,O))
	logo_line_4 = ("%s / __/ /_/ / /__/ /_/ / /_/ / ,<    ║%s  • The•SQUAD team •  %s║"%(O,P,O))
	logo_line_5 = ("%s/_/  \__,_/\___/_.___/\____/_/|_|_  ╚══════════════════════╝  "%(O))
	logo_line_6 = ("%s      ____  ________  ____ ___  (_)_  ______ ___ "%(O))
	logo_line_7 = ("%s     / __ \/ ___/ _ \/ __ `__ \/ / / / / __ `__ \ "%(O))
	logo_line_8 = ("%s    / /_/ / /  /  __/ / / / / / / /_/ / / / / / / "%(O))
	logo_line_9 = ("%s   / .___/_/   \___/_/ /_/ /_/_/\__,_/_/ /_/ /_/ "%(O))
	logo_line_10 = ("%s  /_/                                            "%(O))
	lukman_p(logo_line_1)
	lukman_p(logo_line_2)
	lukman_p(logo_line_3)
	lukman_p(logo_line_4)
	lukman_p(logo_line_5+'\n')
	#lukman_p(logo_line_6)
	#lukman_p(logo_line_7)
	#lukman_p(logo_line_8)
	#lukman_p(logo_line_9)
	#lukman_p(logo_line_10)
	
def menu_log():
	bersih()
	banner()
	lukman_p('%s╔═══════[ %sPilih Metode Login %s]'%(O,P,O))
	lukman_p('%s╠═[%s01%s] %sLogin Menggunakan Cookies'%(O,P,O,P))
	lukman_p('%s╠═[%s02%s] %sTutorial Penggunaan Script'%(O,P,O,P))
	lukman_p('%s╠═[%s03%s] %sInfo Author & Team Project'%(O,P,O,P))
	lukman_p('%s╠═[%s04%s] %sLihat Hasil Crack'%(O,P,O,P))
	lukman_p('%s╠═[%s05%s] %sCheck Opsi Crack'%(O,P,O,P))
	lukman_p('%s║'%(O))
	lukman_p('%s╠═══════[ %sFitur Clone Fb %s]'%(O,P,O))
	lukman_p('%s╠═[%s06%s] %sClone Nomor Fb'%(O,P,O,P))
	lukman_p('%s╠═[%s07%s] %sClone Email Fb'%(O,P,O,P))
	lukman_p('%s╠═[%s08%s] %sClone Nama Fb'%(O,P,O,P))
	lukman_p('%s╠═[%s09%s] %sClone Komen Fb'%(O,P,O,P))
	lukman_p('%s╠═[%s00%s] %sKeluar'%(O,P,O,P))
	lukman_p('%s║'%(O))
	pmu = lukman_i('%s╠═[%s•%s] %sPilih : '%(O,P,O,P))
	lukman_p('%s║'%(O))
	if pmu in ['']:jalan('%s╚═[%s!%s] %sIsi Yang Benar'%(O,P,O,P));menu_log()
	elif pmu in ['1','01','001','a']:
		lukman_p("%s╠═[%s!%s] %sMasukan Cookies Kamu Saran : %scookiedough"%(O,P,O,P,BM))
		cookie = lukman_i('%s╚═[%s•%s] %sCookies : '%(O,P,O,P))
		try:
			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
			find_token = re.search("(EAAG\w+)", data.text)
			open('Data/token.txt','w').write(find_token.group(1))
			open('Data/cookies.txt','w').write(cookie)
			open_role()
			yz  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tiktok),cookies=puput)
			zxc = json.loads(yz.text)
			nama= zxc["name"]
			jalan('%s╚═[%s•%s] %sSelamat datang %s%s%s in tools facbok'%(O,P,O,P,BM,nama,P));menu()
		except requests.exceptions.ConnectionError:jalan('%s╚═[%s!%s] %sKoneksi Bermasalah'%(O,P,O,P));time.sleep(2);lukman_e()
		except (KeyError,IOError,AttributeError):jalan('%s╚═[%s!%s] %sCookies Invalid'%(O,P,O,P));bersih();menu_log()
	elif pmu in ['2','02','002','b']:tutor_deck()
	elif pmu in ['3','03','003','c']:gw_author()
	elif pmu in ['4','04','004','d']:results()
	elif pmu in ['5','05','005','e']:cek_results()
	elif pmu in ['6','06','006','f']:clone_nomor()
	elif pmu in ['7','07','007','g']:clone_email()
	elif pmu in ['8','08','008','h']:clone_nama()
	elif pmu in ['9','09','009','i']:clone_komen()
	elif pmu in ['0','00','000','j']:jalan('%s╠══[%s!%s] %sTerima Kasih Telah Menggunakan SC Ini'%(O,P,O,P));jalan('%s╚══[%s!%s] %sSemoga Harimu Menyenangkan :)\n'%(O,P,O,P));time.sleep(3);bersih();clear();lukman_e()
	else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()
		
	
def menu():
	exit()
	
menu_log()
