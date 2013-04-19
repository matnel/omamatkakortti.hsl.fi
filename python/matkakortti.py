import mechanize
import re
import json

def get_data(username, password):

	b = mechanize.Browser()
	b.open('https://omamatkakortti.hsl.fi/Login.aspx')

	## authenticale

	b.select_form( 'aspnetForm' )

	auth = list(b.forms())[0]

	auth['Etuile$MainContent$LoginControl$LoginForm$UserName'] = username
	auth['Etuile$MainContent$LoginControl$LoginForm$Password'] = password

	r = b.submit()

	data = r.read()

	data = re.search('ETUILE.dotnet.parseJSON\(\'(.*)\'\);', data)

	data = data.group(1)

	return json.loads( data )

if __name__ == '__main__':
	get_data('username', 'password')