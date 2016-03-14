amazondatamonitorsystemstart
def gh():
	gh_Thread().start()
	
class gh_Thread(threading.Thread):
    def __init__(self,app):
        threading.Thread.__init__(self)
        self.app=app

    def run(self):
        while True:
        	time.sleep(2)
        	print 12344567
amazondatamonitorsystemend