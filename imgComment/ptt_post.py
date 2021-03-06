# -*- coding: utf-8 -*-

import platform
import telnetlib
import time
import os

"""
usage:

my_poster_object = ptt_post()
return_url = my_poster_object.to_post(title,content, image_url)

"""

class ptt_post:

	def __init__(self):
		self.telnet = telnetlib.Telnet()
		self.host = 'ptt.cc'
		self.user = 'PlayImage'
		self.passwd = 'qlkza'
		self.command_dic = {}
		self.telnet.open(self.host)
		self.command_dic['left'] = self.key_left
		self.command_dic['right'] = self.key_right
		self.command_dic['down'] = self.key_down
		self.command_dic['up'] = self.key_up
		self.command_dic['up3'] = self.key_up_3
		self.command_dic['up2'] = self.key_up_2
		self.command_dic['up2s'] = self.key_up2_s

		self.delay = 0.0

		self.command_dic['ctrl_p'] = self.key_control_p
		self.command_dic['ctrl_x'] = self.key_control_x

		self.command_dic['_0_'] = self.key_0
		self.command_dic['_s_'] = self.key_s
		self.command_dic['_Q_'] = self.key_Q
		self.command_dic['last4'] = self.key_last_4


	def key_up(self):
	    self.telnet.write(('\033[A').encode("big5"))

	def key_up_3(self):

	    self.telnet.write(('\033[A').encode("big5"))
	    self.telnet.write(('\033[A').encode("big5"))
	    self.telnet.write(('\033[A').encode("big5"))

	def key_up_2(self):
		self.telnet.write(('\033[A').encode("big5"))
		self.telnet.write(('\033[A').encode("big5"))

	def key_up2_s(self):
		self.key_up_2()
		self.key_s()

	def key_last_4(self):
		# 'up','11111','up3','_Q_'
		self.key_right()
		self.telnet.write('11111\r'.encode("big5"))
		self.key_up_3()
		self.key_Q()


	def key_down(self):
	    self.telnet.write(('\033[B').encode("big5"))

	def key_right(self):
	    self.telnet.write(('\033[C').encode("big5"))

	def key_left(self):

	    self.telnet.write(('\033[D').encode("big5"))

	def key_s(self):
		self.telnet.write(('s').encode("big5"))

	def key_0(self):
		self.telnet.write(('0').encode("big5"))


	def key_Q(self):
		self.telnet.write(('Q').encode("big5"))

	def key_control_p(self):
	    self.telnet.write((chr(ord('p') - ord('a') + 1)).encode("big5"))

	def key_control_x(self):
	    self.telnet.write((chr(ord('x') - ord('a') + 1)).encode("big5"))


	def disconnect(self):
	    self.key_left()
	    self.key_left()
	    self.key_left()
	    self.key_left()
	    self.key_left()


	    self.telnet.write(('G\r').encode("big5"))
	    login_status = self.telnet.read_until('[N]'.encode("big5"), 3)

	    # print login_status

	    self.telnet.write(('y\r\r').encode("big5"))

	    self.telnet.close()

	def to_post(self,title_s,text_s,url_s):
		command_index = 0

		# title_text = u'[互動] '+title_s.decode('utf8')
		title_text = u'[互動] '+title_s

		# title = title_text.encode('big5')
		title = title_text
		# content_text = text_s.decode('utf8')
		content_text = text_s
		# content = content_text.encode('big5')
		content = content_text
		# url = url_s.decode('utf8').encode('big5')
		# url = url_s.encode('big5')
		url = url_s

		command_lst = [self.user,self.passwd,' ','up2s','test','up2','ctrl_p',' ',title,content,url,'ctrl_x','s','last4']


		run_mode = True
		# mode = raw_input(">>> Input: ")
		# run_mode = False
		# if mode == "run":
			# run_mode = True

		command = ""

		url = "no found"

		while True:
			time.sleep(self.delay)
			data = self.telnet.read_until(b'fejif', 3)
			# data = telnet.read_eager()
			# data = telnet.read_some()
			# os.system('clear')

			# print("--------------")
			# print(data.encode("big5"))
			# print("--------------")
			# if command == "_Q_":
			if command_index==len(command_lst):
				temp_data = data.decode("big5")
				index_start = temp_data.find("https:")
				index_end = temp_data.find(".html")+5
				# print index_start, "  ", index_end
				sub_str = temp_data[index_start:index_end]
				# print len(sub_str),sub_str

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
					print(type(command))
					temp = command+'\r'
					print("----temp:"+temp.encode("big5"))

					temp = temp.encode("big5")
					# print(b"----temp:"+temp)
					self.telnet.write(temp)

# poster = ptt_post()
# print(poster.to_post("編號1.5","this is test content. 測試資料","http://i.imgur.com/1GcDKFv.jpg"))
