import random, requests, time, threading, string
from colorama import init, Fore, Back, Style

from googlesearch import search

import concurrent.futures

init(convert=True)

class Scraper():
	def logo():
		print(f"""{Fore.RESET}                                                
 _____             _____                         
|  _  |___ ___ ___|   __|___ ___ ___ ___ ___ ___ 
|     |   | . |   |__   |  _|  _| .'| . | -_|  _|
|__|__|_|_|___|_|_|_____|___|_| |__,|  _|___|_|  
				    |_|          

	{Fore.LIGHTCYAN_EX}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
	┃ {Fore.RESET}1) Generate & Check{Fore.LIGHTCYAN_EX}           ┃
	┃ {Fore.RESET}2) Check from file{Fore.LIGHTCYAN_EX}            ┃
	┃ {Fore.RESET}3) Leech & Check{Fore.LIGHTCYAN_EX}              ┃
	┃ {Fore.RESET}4) Leech, Generate & Check {Fore.LIGHTCYAN_EX}   ┃
	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")

	def idGenerator(size, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
		return "".join(random.choices(chars, k=size))

	def generateIDs(amount):
		print(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] Generating {amount} codes, please wait!\n")
		with open(f"output/{time.strftime('%H-%M-%S', time.localtime())}-ids.txt", "w", encoding='utf-8') as file:
			start = time.time()
			for i in range(int(amount)):
				id = Scraper.idGenerator(10)
				file.write(f'{id}\n')
			print(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] Generated {amount} codes in {time.time() - start} seconds!\n")
	
	def checkURL():
		handle = open(f"output/{time.strftime('%H-%M-%S', time.localtime())}-valid.txt", 'w')
		while True:
			id = Scraper.idGenerator(10)
			url = f"https://api.anonfiles.com/v2/file/{id}/info"
			r = requests.get(url).json()
			if(r['status'] == True):
				fullLink = r['data']['file']['url']['full']
				fileName = r['data']['file']['metadata']['name']

				print(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTCYAN_EX}{fullLink}{Fore.RESET} | {Fore.LIGHTCYAN_EX}{fileName}{Fore.RESET}")
				
				handle.write(f'{fullLink} | {fileName}\n')
			else:
				print(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTRED_EX}https://anonfiles.com/" + id)
	def checkByFile(file):
			file1 = open(f'{file}', 'r')
			Lines = file1.readlines()
			handle = open(f"output/{time.strftime('%H-%M-%S', time.localtime())}-valid.txt", 'w')
			for line in Lines:
				url = f"https://api.anonfiles.com/v2/file/{line}/info"
				r = requests.get(url).json()
				if(r['status'] == True):
					fullLink = r['data']['file']['url']['full']
					fileName = r['data']['file']['metadata']['name']

					print(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTCYAN_EX}{fullLink}{Fore.RESET} | {Fore.LIGHTCYAN_EX}{fileName}{Fore.RESET}")
					
					handle.write(f"{fullLink}" + " | " + f"{fileName}" + '/n')
				else:
					print(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTRED_EX}https://anonfiles.com/" + id)
	def leechAndCheck():
		handle = open(f"output/{time.strftime('%H-%M-%S', time.localtime())}-valid.txt", 'w')
		for url in search('site:anonfile.com'):
			if 'https://anonfile.com/' in url:
				id = url.replace('https://anonfile.com/', '')

				url = f"https://api.anonfiles.com/v2/file/{id}/info"
				r = requests.get(url).json()
				if(r['status'] == True):
					fullLink = r['data']['file']['url']['full']
					fileName = r['data']['file']['metadata']['name']

					print(f"111{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTCYAN_EX}{fullLink}{Fore.RESET} | {Fore.LIGHTCYAN_EX}{fileName}{Fore.RESET}")
					
					handle.write(f"{fullLink}" + " | " + f"{fileName}" + '/n')
				else:
					print(f"111{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.LIGHTRED_EX}https://anonfiles.com/" + id)

if __name__ == "__main__":
	Scraper.logo()
	choice = input(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.RESET}mode ~ ")
	if (choice == "1"):
		try:
			i = input(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.RESET}threads ~ ")
			t = []

			for i in range(int(i) + 1):
				thread = threading.Thread(target=Scraper.checkURL(), daemon=True)
				t.append(thread)
				thread.start()

			for thread in t:
				thread.join()
		except (KeyboardInterrupt, ValueError):
			exit("")
	if (choice == "2"):
		filename = input(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.RESET}file path ~ ")
		try:
			i = input(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.RESET}threads ~ ")
			t = []

			for i in range(int(i) + 1):
				thread = threading.Thread(target=Scraper.checkByFile(f"{filename}"), daemon=True)
				t.append(thread)
				thread.start()

			for thread in t:
				thread.join()
		except (KeyboardInterrupt, ValueError):
			exit("")
	if (choice == "3"):
		try:
			i = input(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.RESET}threads ~ ")
			t = []

			for _ in range(int(i) + 1):
				thread = threading.Thread(target=Scraper.leechAndCheck, args=('f',), daemon=True)
				t.append(thread)
				thread.start()

			for thread in t:
				thread.join()
		except (KeyboardInterrupt, ValueError):
			exit("")
	if (choice == "4"):
		try:
			i = input(f"{Fore.RESET}[{Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{Fore.RESET}] {Fore.RESET}threads ~ ")

			with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
				# Submit function1 num_runs times
				for _ in range(int(i) + 1):
					executor.submit(Scraper.leechAndCheck())
				
				# Submit function2 num_runs times
				for _ in range(int(i) + 1):
					executor.submit(Scraper.checkURL())

		except (KeyboardInterrupt, ValueError):
			exit("")