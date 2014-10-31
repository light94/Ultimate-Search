import sys
from PyQt4 import QtGui, QtCore
from bs4 import BeautifulSoup as soup 
import urllib2
import httplib
from xgoogle.search import GoogleSearch , SearchError



class GUI(QtGui.QInputDialog):

	def __init__(self):
		super(GUI,self).__init__()
		#self.GUI()
	
	def initGUI(self):
		text,response = self.getText(self,'Input','Enter alumni name here')
		if response:
			print text
			self.text = text	

def search(url):
	request = urllib2.Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
	opener = urllib2.build_opener()
	data = opener.open(request).read()
	if "Kharagpur" in data:
		print "Kgpian"


def google(text):
	
	try:
		print "Trying to search for "
		g1 = GoogleSearch(text)
		g1.results_per_page = 10
		results = g1.get_results()
		for result in results[:2]:
			response = search(result.url.encode("utf8"))
	except SearchError,e:
		print "Failed Once"
	except urllib2.HTTPError:
		print "Oops"


def main():
	app = QtGui.QApplication(sys.argv)
	obj = GUI()
	
	
	QtCore.QTimer.singleShot(0, obj.initGUI)
	

	if not app.exec_():
		text = obj.text
		text = str(text)
		google(text)





if __name__ == '__main__':
	main()






