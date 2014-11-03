import sys
from PyQt4 import QtGui, QtCore
from bs4 import BeautifulSoup as soup 
from urllib2 import Request,urlopen,HTTPError
import time
from xgoogle.search import GoogleSearch , SearchError
import httplib
import webbrowser


class GUI(QtGui.QWidget):
	def __init__(self):
		super(GUI,self).__init__()
		self.initGUI()

	def google(self,text):
		
		try:
			print "Trying to search for "+text
		
			g1 = GoogleSearch(text)
		
		
			g1.results_per_page = 25
		
			results = g1.get_results()
			
			if len(results)==0:
				print "No search result!!"
			else:
				print "Results FOund!!"
				print type(results)
				print len(results)
				for res in results[:2]:
					time.sleep(1)
					url = res.url.encode("utf8")
					response = self.search(url)
					if response == "Kgpian":
						self.close()
						break
		except SearchError, e:
			print "Failed Once"
		except HTTPError:
			print "Oops"

	
	
	def initGUI(self):
		
		self.btn = QtGui.QPushButton('Input Name',self)
		self.btn.move(20,20)
		self.btn.clicked.connect(self.showDialog)

		self.setWindowTitle('Search')
		self.setGeometry(300,300,250,150)
		self.show()

	def showDialog(self):

		text,ok = QtGui.QInputDialog.getText(self,'Input','Enter The search term')
		if ok:
			self.text = str(text)
			self.google(self.text)


	def search(self,url):
		request = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
		data =  urlopen(request).read()
		if "Kharagpur" in data:
			print "Kgpian"
			# print "Url opened in your browser"
			# webbrowser.open_new_tab(url)
			
			return "Kgpian"

	


def main():
	app = QtGui.QApplication(sys.argv)
	obj = GUI()
	sys.exit(app.exec_())





if __name__ == '__main__':
	#httplib.HTTPConnection.debuglevel = 1
	main()






