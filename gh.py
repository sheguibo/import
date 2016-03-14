amazondatamonitorsystemstart
def gh():
	gh_Thread().start()
	
class gh_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    

    def run(self):
        while True:
        	time.sleep(2)
        	print 12344567
amazondatamonitorsystemend