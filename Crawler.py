import requests
from bs4 import BeautifulSoup
import mechanicalsoup
from lxml import html
from twilio.rest import Client


login = {
	"g_cn_cod": ###,
	"g_cn_mot_pas": ###,
	"CSRFToken": ###,
}

"""
session_requests = requests.session()

login_url = "https://dossier.parcoursup.fr/Candidat/authentification"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='CSRFToken']/@value")))[0]

result = session_requests.post(
	login_url,
	data = login,
	headers = dict(referer=login_url)
)

url = 'https://dossier.parcoursup.fr/Candidat/admissions?ACTION=0'
result = session_requests.get(
	url,
	headers = dict(referer = url)
)

result.ok # Will tell us if the last request was ok
result.status_code
"""

browser = mechanicalsoup.StatefulBrowser()

browser.open("https://dossier.parcoursup.fr/Candidat/authentification?")
#print(browser.get_url())

browser.select_form('form[name="accesdossier"]')

browser["g_cn_cod"] = "###"
browser["g_cn_mot_pas"] = "###"

browser.submit_selected()

page = browser.get_current_page()

placement = list(browser.get_current_page().find_all('div', id='rang_cddt'))[:100]


name = list(browser.get_current_page().find_all('tr', class_='voeu'))[1:100]

#for whatsapp sms V
account_sid = '###'
auth_token = '###'
client = Client(account_sid, auth_token)

finaltext = ""

for child, child2 in zip(name, placement):
	uname = child.findAll('td')
	uname = uname[2].text.strip()

	position = child2.find('span', class_='strong').text
	text = uname + ":  \n" + position + "\n\n"
	#print('\n' + uname)
	#print(position)
	print(text)
	finaltext += text


message = client.messages.create(
		body= "Saheen's position today in Parcoursup: \n\n" + finaltext,
		from_='whatsapp:+###',
		to='whatsapp:+###'
	)

message = client.messages.create(
		body= "Saheen's position today in Parcoursup: \n\n" + finaltext,
		from_='whatsapp:+###',
		to='whatsapp:+###'
	)

message = client.messages.create(
		body= "Saheen's position today in Parcoursup: \n\n" + finaltext,
		from_='whatsapp:+###',
		to='whatsapp:+####'
	)

print(message.sid)
