from pexpect import pxssh

class BOT:
	#initializing the class 
	def __init__(self,host,user,password):
		self.host=host
		self.user=user
		self.password=password
		self.session=self.ssh()

	#ssh into client
	def ssh(self):
		try:
			bot=pxssh.pxssh()
			bot.login(self.host,self.user,self.password)
			return bot
		except Exception as e:
			print('Connection failed')
			print(e)

	# send command to client 		
	def send_command(self,cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before #this returnes the
									# the output of the bash command

# send a command to all the bots
def command_bots(command):
	for bot in botnet:
		attack=bot.send_command(command)
		print('Output from :'+bot.host)
		print(attack)

botnet=[]

def add_bot(host,user,password):
	new_bot=BOT(host,user,password)
	botnet.append(new_bot)

add_bot('127.0.0.1','roy','Haru123')
command_bots('cd Desktop;ls')

