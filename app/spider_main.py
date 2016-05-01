
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' My first spider '

__author__ = 'Leslie Wong'


import html_downloader, html_outputer, html_parser, url_manager

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
		# Spider调度程序
	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print('craw %d : %s ' % (count, new_url))
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
		
				if count > 100:
					break
				count += 1
			except:
				print('craw failed!')
		self.outputer.output_html()
		
if __name__ == '__main__':
	root_url = 'http://baike.baidu.com/view/21087.htm'
	obj_saider = SpiderMain()
	obj_saider.craw(root_url)