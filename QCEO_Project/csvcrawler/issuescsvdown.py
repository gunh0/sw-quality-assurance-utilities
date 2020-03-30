import requests
from bs4 import BeautifulSoup as bs
import csv
import datetime

LOGIN_INFO = { 
	'username': 'kimmin',
	'password': '1qa3ed2ws'
}

day = datetime.datetime.now().strftime('%m%d')

with requests.Session() as s:
	first_page = s.get('http://project.lsware.co.kr/redmine/login')
	html = first_page.text
	soup = bs(html, 'html.parser')
	csrf = soup.find('input', {'name': 'authenticity_token'})
	print(csrf['value'])
	LOGIN_INFO = {**LOGIN_INFO, **{'authenticity_token': csrf['value']}}
	print(LOGIN_INFO)
	login_req = s.post('http://project.lsware.co.kr/redmine/login', data=LOGIN_INFO)

	#secums
	secums_page = s.get('http://project.lsware.co.kr/redmine/projects/secums/')
	
	download = s.get('http://project.lsware.co.kr/redmine/projects/secums/issues.csv')

	csvcontent = download.content.decode('euc-kr')

	with open('/home/qceo/issues/secums/issues' + day + '.csv', 'w') as f:
		writer = csv.writer(f)
		reader = csv.reader(csvcontent.splitlines(), delimiter=',')
		reader = list(reader)
		for row in reader:
			writer.writerow(row)	

	#omniguard unix
	omniguardunix_page = s.get('http://project.lsware.co.kr/redmine/projects/unity/')
	
	download = s.get('http://project.lsware.co.kr/redmine/projects/unity/issues.csv')

	csvcontent = download.content.decode('euc-kr')

	with open('/home/qceo/issues/omniguardunix/issues' + day + '.csv', 'w') as f:
		writer = csv.writer(f)
		reader = csv.reader(csvcontent.splitlines(), delimiter=',')
		reader = list(reader)
		for row in reader:
			writer.writerow(row)

	#omniguard windows
	omniguardwindows_page = s.get('http://project.lsware.co.kr/redmine/projects/uac-for-windowws-se/')

	download = s.get('http://project.lsware.co.kr/redmine/projects/uac-for-windowws-se/issues.csv')

	csvcontent = download.content.decode('euc-kr')

	with open('/home/qceo/issues/omniguardwindows/issues' + day + '.csv', 'w') as f:
		writer = csv.writer(f)
		reader = csv.reader(csvcontent.splitlines(), delimiter=',')
		reader = list(reader)
		for row in reader:
			writer.writerow(row)	

	#fossguard
	fossguard_page = s.get('http://project.lsware.co.kr/redmine/projects/fossguard/')					
				
	download = s.get('http://project.lsware.co.kr/redmine/projects/fossguard/issues.csv')

	csvcontent = download.content.decode('cp949')

	with open('/home/qceo/issues/fossguard/issues' + day + '.csv', 'w') as f:
		writer = csv.writer(f)
		reader = csv.reader(csvcontent.splitlines(), delimiter=',')
		reader = list(reader)
		for row in reader:
			writer.writerow(row)	

	#athena
	athena_page = s.get('http://project.lsware.co.kr/redmine/projects/athena-dev/')
	
	download = s.get('http://project.lsware.co.kr/redmine/projects/athena-dev/issues.csv')

	csvcontent = download.content.decode('euc-kr')

	with open('/home/qceo/issues/athena/issues' + day + '.csv', 'w') as f:
		writer = csv.writer(f)
		reader = csv.reader(csvcontent.splitlines(), delimiter=',')
		reader = list(reader)
		for row in reader:
			writer.writerow(row)	