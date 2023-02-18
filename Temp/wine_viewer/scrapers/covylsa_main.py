#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

""" Script who get the prices of a wine shop and format in a list of tuples """

URL = "https://www.covylsa.com/"

def get_soup(url):
	""" Function who make soup """
	response = requests.get(url).text
	soup = BeautifulSoup(response, 'lxml')
	return soup

def get_pages_urls(soup):
	""" Get product categories main urls """
	products_main_urls = []
	barra = soup.find('div', {'id': 'NavBarElementID2496403'})
	menu_urls = barra.find_all('li')
	for tag in menu_urls:
		try:
			if tag['class'][1]:
				url = tag.find('a', href=True)
				response = requests.get("https://www.covylsa.com/epages/ea2537.sf/es_ES/" + str(url['href'])).text
				second_soup = BeautifulSoup(response, 'lxml')
				second_level_urls = second_soup.find('div', {'class': 'CategoryList'})
				seconds = second_level_urls.find_all('a', href=True)
				for second in seconds:
					products_main_urls.append("https://www.covylsa.com/epages/ea2537.sf/es_ES/" + str(second['href']))
		except:
			url = tag.find('a', href=True)
			products_main_urls.append("https://www.covylsa.com/epages/ea2537.sf/es_ES/" + str(url['href']))
	return products_main_urls

def get_product_info(soup):
	""" Get product name and price """
	registro = []
	product = soup.find_all('td')
	for pro in product:
		try:
			name = pro.find('h3').text.strip()
			price = pro.find('span', {'class': 'price-value'}).span.text.strip()
			try:
				identificador = pro.a['href'].split('/')[-1]
			except:
				identificador = 'N/A'
			lugar = 'Covylsa'
			try:
				if pro.find('div', {'class': 'Description'}):
					stock = pro.find('div', {'class': 'Description'}).text.strip()
				else:
					stock = 'N/A'
			except:
				stock = 'N/A'
			registro.append((identificador, name, price, stock, lugar))
		except:
			pass
	return registro

def main():
	""" Main control function to get the list of tuples """
	products = []
	main_soup = get_soup(URL)
	main_urls = get_pages_urls(main_soup)
	for url in main_urls:
		products_info = get_soup(url)
		product = get_product_info(products_info)
		products.append(product)
	products_list = [t for lst in products for t in lst]
	return products_list


if __name__=='__main__':
	main()
