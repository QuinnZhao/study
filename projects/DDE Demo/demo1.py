import win32ui
import dde
import threading

class Conversation(threading.Thread):
	def __init__(self, server, first, second, tag):
		threading.Thread.__init__(self)
		self.tag = tag #string
		self.first = first #string
		self.second = second #string
		self.server = server #dde server object
		self.conversation = dde.CreateConversation(server)
		#The focus of the problem. Here it works.
		self.conversation.ConnectTo(self.first, self.second)
	
	def run(self):
		print("")

def main():
	machine ="Irrelevant_MachineName"
	tag ="Irrelevant_Tagname"
	server = dde.CreateServer()
	server.Create("Irrelevant_ServerName")
	t = Conversation(server,"Irrelevant_Name", machine, tag)
	t.start()

main() 