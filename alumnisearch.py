import sys
from PyQt4 import QtGui, QtCore
from bs4 import BeautifulSoup as soup 
from urllib2 import Request,urlopen,HTTPError
import time
from xgoogle.search import GoogleSearch , SearchError
import httplib



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
	print "Here"
	request = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
	data =  urlopen(request).read()
	if "Kharagpur" in data:
		print "Kgpian"
		return "Kgpian"

def google(text):
	time.sleep(1)
	try:
		print "Trying to search for "+text
	
		g1 = GoogleSearch(text)
	
	
		g1.results_per_page = 25
	
		results = g1.get_results()
		print len(results)
		for res in results[:2]:
			time.sleep(1)
			response = search(res.url.encode("utf8"))
	except SearchError, e:
		print "Failed Once"
	except HTTPError:
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
	httplib.HTTPConnection.debuglevel = 1
	main()






