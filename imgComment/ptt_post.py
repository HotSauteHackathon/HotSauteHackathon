# -*- coding: utf-8 -*-

import platform
import telnetlib
import time
import os


class ptt_post:

	


	def __init__(self):
		self.telnet = telnetlib.Telnet()
		self.host = 'ptt.cc'
		self.user = 'frankofranko'
		self.passwd = 'qlkza'
		self.command_dic = {}
		self.telnet.open(self.host)
		self.command_dic['left'] = self.key_left
		self.command_dic['right'] = self.key_right
		self.command_dic['down'] = self.key_down
		self.command_dic['up'] = self.key_up
		self.command_dic['up3'] = self.key_up_3

		self.command_dic['ctrl_p'] = self.key_control_p
		self.command_dic['ctrl_x'] = self.key_control_x

		self.command_dic['_0_'] = self.key_0
		self.command_dic['_s_'] = self.key_s
		self.command_dic['_Q_'] = self.key_Q


	def key_up(self):
	    self.telnet.write('\033[A')

	def key_up_3(self):
	    self.telnet.write('\033[A')
	    self.telnet.write('\033[A')
	    self.telnet.write('\033[A')
	 
	def key_down(self):
	    self.telnet.write('\033[B')

	def key_right(self):
	    self.telnet.write('\033[C')

	def key_left(self):
	    self.telnet.write('\033[D')    

	def key_s(self):
		self.telnet.write('s') 

	def key_0(self):
		self.telnet.write('0') 

	def key_Q(self):
		self.telnet.write('Q')

	def key_control_p(self):
	    self.telnet.write(chr(ord('p') - ord('a') + 1))

	def key_control_x(self):
	    self.telnet.write(chr(ord('x') - ord('a') + 1))


	def disconnect(self):
	    self.key_left()
	    self.key_left()
	    self.key_left()
	    self.key_left()
	    self.key_left()
	 
	    self.telnet.write('G\r')
	    login_status = self.telnet.read_until('[N]', 3)
	 
	    print login_status
	 
	    self.telnet.write('y\r\r')
	    self.telnet.close()

	def to_post(self,title_s,text_s,url_s):
		command_index = 0
		title_text = u'[互動] '+title_s.decode('utf8')
		title = title_text.encode('big5')
		content_text = text_s.decode('utf8')
		content = content_text.encode('big5')
		url = url_s.decode('utf8').encode('big5')
		command_lst = ['PlayImage','qlkza',' ','up','up','_s_','test','up','up','ctrl_p',' ',title,content,url,'ctrl_x','s','up','11111','up3','_Q_']


		run_mode = True
		# mode = raw_input(">>> Input: ")
		# run_mode = False
		# if mode == "run":
			# run_mode = True

		command = ""

		url = "no found"

		while True:
			time.sleep(0.35)
			data = self.telnet.read_until('fejif', 3)
			# data = telnet.read_eager()
			# data = telnet.read_some()
			os.system('clear')
			print "--------------"
			print data
			print "--------------"
			if command == "_Q_":
				index_start = data.find("https:")
				index_end = data.find(".html")+5
				print index_start, "  ", index_end
				sub_str = data[index_start:index_end]
				print len(sub_str),sub_str
				url = sub_str
				self.disconnect()
				return url
			if command_index < len(command_lst) and run_mode==True:
				command = command_lst[command_index]
				command_index += 1
			else:
				command = raw_input(">>> Input: ")
			if len(command)>0:
				if command in self.command_dic.keys():
					self.command_dic[command]()
				else:
					self.telnet.write(command+'\r')

# poster = ptt_post()
# print poster.to_post("編號1","this is test content. 測試資料","http://i.imgur.com/1GcDKFv.jpg")