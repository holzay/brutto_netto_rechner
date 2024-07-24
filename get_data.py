import requests
import re

def get_data(start_salary,end_salary,interval):
	# http://www.bmf-steuerrechner.de/interface/2024Version1.xhtml?code=2024ESSt&LZZ=1&RE4=2500000&STKL=1

	URL='http://www.bmf-steuerrechner.de/interface/2024Version1.xhtml'

	lohnsteuer={}

	PATTERN = r'<ausgabe\ name="LSTLZZ"\ value="(\d+)"\ type="STANDARD"\/>'

	last_value = 0
	start_salary=start_salary*100
	end_salary=end_salary*100

	for i in range(start_salary,end_salary,interval):
		payload = {
			'code' : '2024ESSt',
			'LZZ' : '1',
			'RE4' : i,
			'STKL' : '1'
		}
		r = requests.get(URL,params=payload)
		if i % 10 == 0:
			print(i) 
		if r.status_code == 200:
			m = re.search(PATTERN,r.text)
			if m:
				if int(m.group(1)) > last_value:
					lohnsteuer[i] = m.group(1)
		else:
			print(r.status_code)

	print(f'writing {len(lohnsteuer)} items into file...')
		
	with open('lohnsteuer.txt','w') as f:
		for key in lohnsteuer:
			f.write(f'{key},{lohnsteuer[key]}\n')

if __name__=='__main__':
	get_data(0,100000)