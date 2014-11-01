import sys
from bs4 import BeautifulSoup as soup 
from urllib2 import Request,urlopen,HTTPError
import time
from xgoogle.search import GoogleSearch , SearchError
import httplib
import webbrowser
import ezodf
	
			
def search(url):
	request = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
	data =  urlopen(request).read()
	if "Kharagpur" in data:
		print "Kgpian"
		# print "Url opened in your browser"
		# webbrowser.open_new_tab(url)
		
		return "Found"

def encode(data):
	return data.encode('ascii','ignore')

def google(text):
	response = ""
	time.sleep(0.5)
	count = 0
	
	try:
		print "Trying to search for "+text
	
		g1 = GoogleSearch(text)
	
	
		g1.results_per_page = 25
	
		results = g1.get_results()
		
		for res in results[:2]:
			time.sleep(0.5)
			response = search(res.url.encode("utf8"))
			return response
	except SearchError, e:
		print "Failed Once"
	except HTTPError:
		print "Oops"
#The search terms shall have atleast one of *, #,!,<,>,? which mean firstname,lastname,company,post,yearofpassing,department in that order

def openfile(fname):
	spreadsheet = ezodf.opendoc(fname)
	sheet = spreadsheet.sheets[0]
	rows = sheet.nrows()
	columns = sheet.ncols()
	for row in range(1	,5):
		with open('search.txt','r') as f:
			for line in f:
			
				newline = ""
				splitline = line.split(" ")
				if sheet[row,0].value !=None or sheet[row,1].value !=None or sheet[row,3].value !=None:
		

					
					
					for word in splitline:

						if '*' in word:
							newline = newline+" " +encode(sheet[row,0].value)
						elif '#' in word:
							newline = newline+" " +encode(sheet[row,1].value)
						elif '!' in word:
							newline = newline+" " +encode(sheet[row,3].value)
						elif '<' in word:
							newline = newline+" " +encode(sheet[row,4].value)
						else:
							newline = newline+" "+word
					response = google(newline)
					if response == "Found":
						break
					

def main():
	a = raw_input('Enter the complete path of the file\n')
	openfile(a)
	






if __name__ == '__main__':
	#httplib.HTTPConnection.debuglevel = 1
	main()






