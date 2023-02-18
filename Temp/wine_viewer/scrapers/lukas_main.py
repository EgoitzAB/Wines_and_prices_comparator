#!/usr/bin/python3

import requests
import re

from bs4 import BeautifulSoup

""" I need to disable the ssl certificate, in browser works but not with requests, urlib,
request-html or xextract. I try downloading certifi, and other methods. Impossible, finally
I leave because I am not going to send data and the domain is reliable """

URL = "https://lukasgourmet.com/product-sitemap.xml"
product_pattern = re.compile(r'product.+')

def get_soup(url):
	""" Function who make soup """
	requests.urllib3.disable_warnings()
	session = requests.Session()
	response = session.get(url, verify=False).text
	soup = BeautifulSoup(response, features='xml')
	return soup

def extract_selectors(soup, selector):
    """ Avoid NoneType object don't have attribute failure """
    try:
        return soup.find(selector)
    except:
        return 'N/A'

def get_products_urls(soup):
	""" Function to get the wines urls """
	wines_links = []
	vinoteca = re.compile(r"vinoteca")
	links = soup.find_all('loc')
	for link in links:
		if re.search(vinoteca, link.text):
			wines_links.append(link.text)
	return wines_links

def get_products_info(soup):
	""" Function to get the product info """
	try:
		nombre = extract_selectors(soup, ('h1', {'class': 'product_title entry-title'})).text
		precio = extract_selectors(soup, ('bdi')).text
		if soup.find('p', {'class': re.compile('^stock.+')}):
			stock = soup.find('p', {'class': re.compile('^stock.+')}).text
		else:
			stock = 'N/A'
		lugar = 'Lukas'
		identificador = soup.find('div', {'class': 'main'}).div.next_element.attrs['id']
		return (identificador, nombre, precio, stock, lugar)
	except:
		pass

def main():
	""" Main function to get the products info """
	productos = []
	soup = get_soup(URL)
	wines_links = get_products_urls(soup)
	for wine in wines_links:
		soup = get_soup(wine)
		product = get_products_info(soup)
		productos.append(product)
	return productos

if __name__=='__main__':
	main()