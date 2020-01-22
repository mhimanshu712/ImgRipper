from bs4 import BeautifulSoup as bs
import requests as rq
import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()

#Make download dic
try:
	os.mkdir('downloads')
except:
	pass

def download():
	imgarr = []
	doc = rq.get(e.get())
	doc = doc.content
	
	soup = bs(doc,'lxml')
	images = soup.find_all('img')
	
	for image in images:
		if image.has_attr('src'):
			imgarr.append(image['src'])

	messagebox.askyesno('Download?',f"{len(imgarr)} images found!\nDownload All?")
	print(imgarr[0])
	ind = imgarr[0].rindex('/')+1
	print(imgarr[0][ind:])
	print('oooo')

	for img in imgarr:
		fileindex = img.rindex('/')+1
		filename = img[fileindex:]
		if '?' in filename:
			fileindex = filename.rindex('?')
			filename = filename[:fileindex]
		print(filename)
		url = img
		if not '://' in img:
			url = e.get() + img
		print('url>>> ',url)
		res = rq.get(url)
		if res.status_code == 200:
			with open('./download/'+filename,'wb') as f:
				f.write(res.content)

	messagebox.showinfo('Done','Done Downloading')

	
                
	
	
	
	

tk.Label(root,text='Img Ripper',bg='black',fg='white',font=('Helvetica',20)).pack(pady=30)
e = tk.Entry(root,width=30,bd=5)
e.pack(pady=10,padx=50)
b = tk.Button(root,text='Download!',command=download)
b.pack(pady=30)



root.mainloop()
