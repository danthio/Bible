
import tkinter as tk
from tkinter import ttk 
import json
from PIL import Image,ImageTk
import time
import math
import sqlite3 as db


"""
with open('data/asv.json', 'r') as file:
	data = file.read()


bible=json.loads(data)


for b in bible["resultset"]["row"]:


	if b["field"][1]==1:# and b["field"][2]==1:
		print(b["field"])
"""

# Function to wrap text
def wrap_text(canvas, text, x, y, width,col,con,font=("FreeMono", 13)):
    # Create a list to store lines of wrapped text
    lines = []
    words = text.split()
    current_line = words[0]


    
    for word in words[1:]:
        # Try to add the word to the current line
        test_line = current_line + " " + word
        # Create temporary text to test width
        temp_text = canvas.create_text(x, y, text=test_line, font=font, anchor="nw",fill=col)
        
        # Check if the new line is too wide for the canvas
        text_width = canvas.bbox(temp_text)[2] - canvas.bbox(temp_text)[0]
        
        if text_width <= width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
        
        # Delete the temporary text item after the test
        canvas.delete(temp_text)
    
    # Add the last line
    lines.append(current_line)
    
    # Create the wrapped text on the canvas
    for i, line in enumerate(lines):

    	if con==0:
        	canvas.create_text(x, y + i * 20, text=line, font=font, anchor="nw",fill=col)

    return y+i*20



def b3(e):
	global highlights,view
	global book,chapter,verse,_book
	global can2
	global state


	if state==4:
		for i in view:

			if i[-1][0]<=e.x<=i[-1][2]:
				if i[-1][1]<=e.y+can2.canvasy(0)<=i[-1][3]:





					dbbible=db.connect('data/highlights.db')
					cur=dbbible.cursor()


					try:
						ar=[]
						for _ in highlights:
							ar.append(_[:3])

						v=ar.index(i[:3])




						cur.execute("SELECT * FROM highlight")
						rows=cur.fetchall()

						for row in rows:

							if row[1]==i[0] and row[2]==i[1] and row[3]==i[2]:
								s=int(row[0])



						cur.execute("DELETE FROM highlight WHERE id_="+str(s)+"")
						dbbible.commit()


					except:




						cur.execute("SELECT MAX(id_) FROM highlight")
						rows=cur.fetchall()

						v=0
						for row in rows:
							v=row[0]
						if v==None:
							v=1
						else:
							v+=1




						cur.execute("INSERT INTO highlight VALUES("+str(v)+","+str(i[0])+","+str(i[1])+","+str(i[2])+",'"+str(_book)+"')")

						dbbible.commit()



					main(book,chapter,verse)
def b1(e):


	global wd,ht,o_or_n
	global combo1,combo2,combo3
	global bible_books
	global var1,var2,var3
	global frame

	global book,chapter,verse,can2,yscroll,_book
	global can,can2

	global ar_var2,ar_var3


	if state==1:


		y=(ht-40-20-40-20-40-20-40)/2


		#asv


		cx,cy=wd/2-140,y+20

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:

			_book="asv"

			load_bible(0)
			sel_testament()
			return



		cx,cy=wd/2+140,y+20

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:

			_book="asv"

			load_bible(0)
			sel_testament()
			return



		if wd/2-140<=e.x<=wd/2+140:
			if y<=e.y<=y+40:
				_book="asv"
				load_bible(0)
				sel_testament()
				return





		#kjv


		cx,cy=wd/2-140,y+20+70

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:
			_book="kjv"

			load_bible(1)
			sel_testament()
			return



		cx,cy=wd/2+140,y+20+70

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:
			_book="kjv"

			load_bible(1)
			sel_testament()
			return



		if wd/2-140<=e.x<=wd/2+140:
			if y+70<=e.y<=y+40+70:
				_book="kjv"
				load_bible(1)
				sel_testament()
				return



		#continue

		def cnt():
			global _book,book,chapter,verse
			global can2


			ar=[]

			with open('data/save.txt', 'r') as file:



				for line in file:

					ar.append(line.strip())




			book=int(ar[0])
			chapter=int(ar[1])

			if ar[2]=="":
				verse=ar[2]
			else:
				verse=int(ar[2])




			fraction=int(ar[3])#/(can2.bbox("all")[3])

			can2.yview_moveto(0)

			_book=ar[4]

			if _book=="asv":
				load_bible(0)
			elif _book=="kjv":
				load_bible(1)


		cx,cy=wd/2-140,y+20+140

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:

			with open('data/save.txt', 'r') as file:
				if file.read()=="":
					return

			cnt()
			
			main(book,chapter,verse)




			return



		cx,cy=wd/2+140,y+20+140

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:

			with open('data/save.txt', 'r') as file:
				if file.read()=="":
					return

			cnt()
			main(book,chapter,verse)

			return



		if wd/2-140<=e.x<=wd/2+140:
			if y+140<=e.y<=y+40+140:



				with open('data/save.txt', 'r') as file:
					if file.read()=="":
						return

				cnt()
				main(book,chapter,verse)

				return



		#highlights



		cx,cy=wd/2-140,y+20+70+140

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:
			can2["scrollregion"]=(0,0, wd-20-7,ht-90)
			view_highlights()
			
			return



		cx,cy=wd/2+140,y+20+70+140

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:
			can2["scrollregion"]=(0,0, wd-20-7,ht-90)
			view_highlights()
			
			return



		if wd/2-140<=e.x<=wd/2+140:
			if y+70+140<=e.y<=y+40+70+140:
				can2["scrollregion"]=(0,0, wd-20-7,ht-90)
				view_highlights()
				
				return






	elif state==2:
		

		cx,cy=wd-5-30+15,5+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			choose_bible()

			return


		y=(ht-40-20-40)/2


		#old testament


		cx,cy=wd/2-100,y+20

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:


			o_or_n=0

			can.focus_set()


			ar_var2=[]
			ar_var3=[]

			select_chapter_and_verse(0)
			return



		cx,cy=wd/2+100,y+20

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:

			o_or_n=0
			can.focus_set()


			ar_var2=[]
			ar_var3=[]
			select_chapter_and_verse(0)
			return



		if wd/2-100<=e.x<=wd/2+100:
			if y<=e.y<=y+40:
				o_or_n=0
				can.focus_set()

				ar_var2=[]
				ar_var3=[]

				select_chapter_and_verse(0)
				return





		#new testament


		cx,cy=wd/2-100,y+20+70

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:

			o_or_n=1

			can.focus_set()

			select_chapter_and_verse(1)
			return



		cx,cy=wd/2+100,y+20+70

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:
			o_or_n=1

			can.focus_set()

			select_chapter_and_verse(1)
			return



		if wd/2-100<=e.x<=wd/2+100:
			if y+70<=e.y<=y+40+70:
				o_or_n=1
				can.focus_set()
				select_chapter_and_verse(1)
				return

	elif state==3:


		cx,cy=wd-5-30+15,5+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			combo1.set("")
			combo2.set("")
			combo3.set("")


			combo1.place_forget()
			combo2.place_forget()
			combo3.place_forget()

			sel_testament()

			return









		y=ht-60


		cx,cy=wd/2-100,y+20

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:

			if var1.get()=="":
				return
			else:
				book=bible_books.index(var1.get())+1



			if var2.get()=="":

				chapter=1
			else:
				chapter=int(var2.get())


			verse=var3.get()







			main(book,chapter,verse)
			return



		cx,cy=wd/2+100,y+20

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=20:



			if var1.get()=="":
				return
			else:
				book=bible_books.index(var1.get())+1



			if var2.get()=="":

				chapter=1
			else:
				chapter=int(var2.get())

			verse=var3.get()




	

			main(book,chapter,verse)

			return



		if wd/2-100<=e.x<=wd/2+100:
			if y<=e.y<=y+40:

				if var1.get()=="":
					return
				else:
					book=bible_books.index(var1.get())+1



				if var2.get()=="":

					chapter=1
				else:
					chapter=int(var2.get())


				verse=var3.get()





				main(book,chapter,verse)
				return











	elif state==4:




		cx,cy=wd-5-30+15,5+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			can2["scrollregion"]=(0,0, wd-20-7,ht-90)
			frame.place_forget()
			o_or_n=1
			can.focus_set()
			
			combo1.set("")
			combo2.set("")
			combo3.set("")		
			combo1.place_forget()
			combo2.place_forget()			
			combo3.place_forget()

			ar_var2=[]
			ar_var3=[]

			sel_testament()

			return



		x=wd/3

		cx,cy=x,ht-45/2

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			
			if chapter-1==0 and book-1!=0:

				book-=1
				chapter=1
				verse=""
				can2["scrollregion"]=(0,0, wd-20-7,ht-90)
				main(book,chapter,verse)

			elif chapter-1>=1:

				chapter-=1
				verse=""
				can2["scrollregion"]=(0,0, wd-20-7,ht-90)
				main(book,chapter,verse)




		x=wd/3

		cx,cy=wd-x,ht-45/2

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			
			n=len(determine_chapters(bible_books[book-1]))

			if chapter+1>n and book+1!=67:

				book+=1
				chapter=1
				verse=""

				can2["scrollregion"]=(0,0, wd-20-7,ht-90)


				main(book,chapter,verse)

			elif chapter+1<=n:


				chapter+=1
				verse=""

				can2["scrollregion"]=(0,0, wd-20-7,ht-90)

				main(book,chapter,verse)




	elif state==5:



		cx,cy=wd-5-30+15,5+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			choose_bible()
			frame.place_forget()



def view_highlights():
	global state,frame,can2,can
	global back,bible_books

	state=5


	can.delete("all")
	can2.delete("all")



	highlights=[]


	can.create_image(wd-5-30,5,image=back,anchor="nw")

	can.create_text(wd/2,45/2,text="Highlights",font=("FreeMono",15))







	dbbible=db.connect('data/highlights.db')
	cur=dbbible.cursor()


	cur.execute("SELECT * FROM highlight")
	rows=cur.fetchall()

	for row in rows:

		highlights.append([int(row[1]),int(row[2]),int(row[3]),str(row[4])])



	ar=[]



	for i in highlights:

		if i[-1]=="asv":
			load_bible(0)
		elif i[-1]=="kjv":
			load_bible(1)


		for b in bible["resultset"]["row"]:



				if b["field"][1]==i[0] and b["field"][2]==i[1] and b["field"][3]==i[2]:



					title=str(bible_books[i[0]-1])+" "+str(i[1])+":"+str(i[2])
					body=b["field"][-1]
					ar.append([title,body])


	y=10


	for _ in range(len(ar)):


		yy=wrap_text(can2, ar[_][0], 10, y, wd-20-7-20,"blue",0)
		y=yy+20
		yy=wrap_text(can2, ar[_][1], 10, y, wd-20-7-20,"#000000",0)


		


		y=yy+40







	can2["scrollregion"]=(0,0, wd-7,y)


	frame.place(in_=root,x=0,y=45)




def update():
	global can2,yscroll
	global book,chapter,verse,_book
	global state


	if state==4:



		yscroll=can2.canvasy(0)


		file = open("data/save.txt", "w")
		L = []

		L.append(str(book)+"\n")
		L.append(str(chapter)+"\n")
		L.append(str(verse)+"\n")
		L.append(str(int(yscroll))+"\n")
		L.append(str(_book)+"\n")


		file.writelines(L)
		file.close()


	root.after(100,update)


def main(book_,chapter_,verse_):
	global state,can,can2,frame,back
	global wd,ht

	global var3,bible_books

	global next_,previous

	global highlights
	global view,highlights
	global yscroll
	global _book

	state=4

	


	can.delete("all")
	can2.delete("all")

	highlights=[]







	dbbible=db.connect('data/highlights.db')
	cur=dbbible.cursor()


	cur.execute("SELECT * FROM highlight")
	rows=cur.fetchall()

	for row in rows:

		highlights.append([row[1],row[2],row[3],row[4]])













	can.create_image(wd-5-30,5,image=back,anchor="nw")


	x=wd/3

	can.create_image(x-15,ht-45/2-15,image=previous,anchor="nw")

	can.create_image(wd-x-15,ht-45/2-15,image=next_ ,anchor="nw")


	



	title=str(bible_books[book_-1])+"  "+str(chapter_)

	can.create_text(wd/2,45/2,text=title,font=("FreeMono",17))

	ar=[]

	v=1

	view=[]


	for b in bible["resultset"]["row"]:

		if verse_=="":

			


			if b["field"][1]==book_ and b["field"][2]==chapter_:

				txt=str(v)+" "+b["field"][-1]

				ar.append(txt)

				view.append([book_,chapter_,v])

				v+=1
		else:
			verse_=int(verse_)

			if b["field"][1]==book_ and b["field"][2]==chapter_ and b["field"][3]==verse_:

				txt=str(verse_)+" "+b["field"][-1]
				ar.append(txt)
				view.append([book_,chapter_,verse_])
				break







	y=10


	for _ in range(len(ar)):

		col="#000000"



		yv=wrap_text(can2, ar[_], 10, y, wd-7-20,col,1)

		view[_].append([5,y-10, wd-5,yv+30])

		
		for i in highlights:
			if view[_][:3]==i[:3]:
				col="blue"



				
				#can2.create_rectangle(5,y-10, wd-5,yv+30,fill="#000000")

		yy=wrap_text(can2, ar[_], 10, y, wd-7-20,col,0)

		


		y=yy+40






	can2["scrollregion"]=(0,0, wd-7,y)


	frame.place(in_=root,x=0,y=45)






def determine_chapters(book):

	global ar_var2,bible_books


	ar_var2=[]

	n=0

	for b in bible["resultset"]["row"]:

		if b["field"][1]==bible_books.index(book)+1:
			n=b["field"][2]




	c=1

	for v in range(n):
		ar_var2.append(c)

		c+=1

	return ar_var2

def determine_verses(book,chapter):

	global ar_var3,bible_books


	ar_var3=[]

	n=0

	for b in bible["resultset"]["row"]:

		if b["field"][1]==bible_books.index(book)+1 and b["field"][2]==int(chapter):
			n+=1

	c=1

	for v in range(n):
		ar_var3.append(c)

		c+=1

	return ar_var3

def sel_combo1(e):

	global var1,ar_var2,o_or_n
	global combo2,combo3

	book=var1.get()

	ar_var2=determine_chapters(book)


	combo2.set('')
	combo3.set('')


	select_chapter_and_verse(o_or_n)


def sel_combo2(e):

	global var1,var2,ar_var2,o_or_n
	global combo2,combo3

	book=var1.get()
	chapter=var2.get()

	ar_var3=determine_verses(book,chapter)



	combo3.set('')


	select_chapter_and_verse(o_or_n)





def select_chapter_and_verse(c):
	global state,can,wd,ht,bible_books,bible,ar_var2,ar_var3




	state=3

	if c==0:
		chapters=bible_books[:39]

	else:
		chapters=bible_books[39:]




	can.delete("all")


	can.create_image(wd-20-30,10,image=back,anchor="nw")

	y=((ht-60)-167)/2


	can.create_arc(140-30,y-10-20, 140-30+30,y-10-20+30,start=90,extent=90,style="arc",outline="#000000")
	can.create_arc(140-30,y+167-20-30, 140-30+30,y+167-20,start=180,extent=90,style="arc",outline="#000000")


	can.create_arc(wd-140+30+15-30,y-10-20, wd-140+30+15,y-10-20+30,start=0,extent=90,style="arc",outline="#000000")
	can.create_arc(wd-140+30+15-30,y+167-20-30, wd-140+30+15,y+167-20,start=270,extent=90,style="arc",outline="#000000")

	can.create_line(140-30+15,y-10-20, wd-140+30+15-15,y-10-20,fill="#000000")
	can.create_line(140-30+15-1,y+167-20, wd-140+30+15-15,y+167-20,fill="#000000")

	can.create_line(140-30,y-10-20+15, 140-30,y+167-20-15,fill="#000000")
	can.create_line(wd-140+30+15,y-10-20+15, wd-140+30+15,y+167-20-15,fill="#000000")

	can.create_text(140,y,text="Book",font=("FreeMono",13),fill="#000000",anchor="w")




	combo1['values'] = chapters
	combo1['state'] = 'readonly'
	combo1.place(in_=root,x=140,y=y+20)


	can.create_text(140,y+70,text="Chapter",font=("FreeMono",13),fill="#000000",anchor="w")


	combo2['values'] = ar_var2
	combo2['state'] = 'readonly'
	combo2.place(in_=root,x=140,y=y+20+70)



	can.create_text(140+243,y+70,text="Verse",font=("FreeMono",13),fill="#000000",anchor="w")

	combo3['values'] = ar_var3
	combo3['state'] = 'readonly'

	combo3.place(in_=root,x=140+243,y=y+20+70)


	y=ht-20-40


	can.create_arc(wd/2-100-20,y, wd/2-100+20,y+40,outline="#000000",style="arc",start=90,extent=180)
	can.create_arc(wd/2+100-20,y, wd/2+100+20,y+40,outline="#000000",style="arc",start=270,extent=180)

	can.create_line(wd/2-100,y, wd/2+100,y,fill="#000000")
	can.create_line(wd/2-100-1,y+40, wd/2+100,y+40)



	can.create_text(wd/2,y+20,text="Read",font=("FreeMono",13))





def sel_testament():
	global can,wd,ht,state,back

	state=2

	can.delete("all") 

	y=(ht-40-20-40)/2

	can.delete("all")

	can.create_image(wd-5-30,5,image=back,anchor="nw")






	can.create_arc(wd/2-100-20,y, wd/2-100+20,y+40,outline="#000000",style="arc",start=90,extent=180)
	can.create_arc(wd/2+100-20,y, wd/2+100+20,y+40,outline="#000000",style="arc",start=270,extent=180)

	can.create_line(wd/2-100,y, wd/2+100,y,fill="#000000")
	can.create_line(wd/2-100-1,y+40, wd/2+100,y+40)



	can.create_text(wd/2,y+20,text="Old Testament",font=("FreeMono",13))



	can.create_arc(wd/2-100-20,y+70, wd/2-100+20,y+40+70,outline="#000000",style="arc",start=90,extent=180)
	can.create_arc(wd/2+100-20,y+70, wd/2+100+20,y+40+70,outline="#000000",style="arc",start=270,extent=180)

	can.create_line(wd/2-100,y+70, wd/2+100,y+70,fill="#000000")
	can.create_line(wd/2-100-1,y+40+70, wd/2+100,y+40+70)

	can.create_text(wd/2,y+20+70,text="New Testament",font=("FreeMono",13))






def load_bible(c):
	global bible


	if c==0:


		with open('data/asv.json', 'r') as file:
			data = file.read()


		bible=json.loads(data)


	elif c==1:


		with open('data/kjv.json', 'r') as file:
			data = file.read()


		bible=json.loads(data)



	return bible



def choose_bible():
	global can,state,wd,ht

	state=1


	y=(ht-40-20-40-20-40-20-40)/2

	can.delete("all")



	can.create_arc(wd/2-140-20,y, wd/2-140+20,y+40,outline="#000000",style="arc",start=90,extent=180)
	can.create_arc(wd/2+140-20,y, wd/2+140+20,y+40,outline="#000000",style="arc",start=270,extent=180)

	can.create_line(wd/2-140,y, wd/2+140,y,fill="#000000")
	can.create_line(wd/2-140-1,y+40, wd/2+140,y+40)



	can.create_text(wd/2,y+20,text="American Standard Version (ASV)",font=("FreeMono",13))



	can.create_arc(wd/2-140-20,y+70, wd/2-140+20,y+40+70,outline="#000000",style="arc",start=90,extent=180)
	can.create_arc(wd/2+140-20,y+70, wd/2+140+20,y+40+70,outline="#000000",style="arc",start=270,extent=180)

	can.create_line(wd/2-140,y+70, wd/2+140,y+70,fill="#000000")
	can.create_line(wd/2-140-1,y+40+70, wd/2+140,y+40+70)

	can.create_text(wd/2,y+20+70,text="King James Version (KJV)",font=("FreeMono",13))



	can.create_arc(wd/2-140-20,y+140, wd/2-140+20,y+40+140,outline="#000000",style="arc",start=90,extent=180)
	can.create_arc(wd/2+140-20,y+140, wd/2+140+20,y+40+140,outline="#000000",style="arc",start=270,extent=180)

	can.create_line(wd/2-140,y+140, wd/2+140,y+140,fill="#000000")
	can.create_line(wd/2-140-1,y+40+140, wd/2+140,y+40+140)

	can.create_text(wd/2,y+20+140,text="Continue",font=("FreeMono",13))


	can.create_arc(wd/2-140-20,y+140+70, wd/2-140+20,y+40+140+70,outline="#000000",style="arc",start=90,extent=180)
	can.create_arc(wd/2+140-20,y+140+70, wd/2+140+20,y+40+140+70,outline="#000000",style="arc",start=270,extent=180)

	can.create_line(wd/2-140,y+140+70, wd/2+140,y+140+70,fill="#000000")
	can.create_line(wd/2-140-1,y+40+140+70, wd/2+140,y+40+140++70)

	can.create_text(wd/2,y+20+140+70,text="Highlights",font=("FreeMono",13))

	

def intro():
	global can,bg


	can.delete("all")

	can.create_image(0,0,image=bg,anchor="nw")

def intro_():
	global v1,state


	if state==0:

		if time.time()>v1+1.5:

			choose_bible()

	root.after(1000,intro_)


def load_images():

	global bg,back,next_,previous

	bg=ImageTk.PhotoImage(file="data/cross.jpg")

	back=ImageTk.PhotoImage(file="data/back.png")

	next_=ImageTk.PhotoImage(file="data/right.png")

	previous=ImageTk.PhotoImage(file="data/left.png")








bible={}



bible_books = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", 
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", 
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", 
    "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", 
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations", 
    "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", 
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", 
    "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", 
    "Mark", "Luke", "John", "Acts", "Romans", 
    "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", 
    "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", 
    "Titus", "Philemon", "Hebrews", "James", "1 Peter", 
    "2 Peter", "1 John", "2 John", "3 John", "Jude", 
    "Revelation"
]















bg=0
back=0

state=0



o_or_n=0

book,chapter,verse="","",""




highlights=[]
view=[]
yscroll=0

_book=""







next_,previous=0,0

root=tk.Tk()
root.title("Bible")
root.resizable(0,0)
root.iconbitmap("data/cross.ico")


wd,ht=720,641


w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry(str(wd)+"x"+str(ht)+"+"+str(int((w-wd)/2))+"+0")


can=tk.Canvas(width=720,height=641,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",b1)





style=ttk.Style()
style.element_create("My.Vertical.TScrollbar.trough", "from", "clam")
style.element_create("My.Vertical.TScrollbar.thumb", "from", "clam")
style.element_create("My.Vertical.TScrollbar.grip", "from", "clam")

style.layout("My.Vertical.TScrollbar",
   [('My.Vertical.TScrollbar.trough',
     {'children': [('My.Vertical.TScrollbar.thumb',
                    {'unit': '1',
                     'children':
                        [('My.Vertical.TScrollbar.grip', {'sticky': ''})],
                     'sticky': 'nswe'})
                  ],
      'sticky': 'ns'})])


style.configure("My.Vertical.TScrollbar", gripcount=0, background="#000000",
                troughcolor='#ffffff', borderwidth=0, bordercolor='#ffffff',
                lightcolor='#ffffff',relief="flat", darkcolor='#ffffff',
                arrowsize=7)

var1 = tk.StringVar() 

combo1 = ttk.Combobox(textvariable=var1,font=("FreeMono",15),width=40)
combo1.bind('<<ComboboxSelected>>',sel_combo1)


var2 = tk.StringVar() 
ar_var2=[]
combo2 = ttk.Combobox(textvariable=var2,font=("FreeMono",15),width=18)
combo2.bind('<<ComboboxSelected>>',sel_combo2)

var3 = tk.StringVar() 
ar_var3=[]
combo3 = ttk.Combobox(textvariable=var3,font=("FreeMono",15),width=18)


def _on_mousewheel(e):
	global can2

	can2.yview_scroll(int(-1*(e.delta/120)), "units")
	#print(int(-1*(e.delta/120)))



frame=tk.Frame(bg="#ffffff",width=wd,height=ht-90)

can2=tk.Canvas(frame,bg="#ffffff",width=wd-7,height=ht-90,relief="flat",highlightthickness=0,border=0,
	scrollregion=(0,0,wd-20-7,ht-90))
can2.pack(side=tk.LEFT)
can2.bind_all("<MouseWheel>",_on_mousewheel)
can2.bind("<Button-3>",b3)


sb=ttk.Scrollbar(frame,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")

sb.config(command=can2.yview)

can2.config(yscrollcommand=sb.set)
sb.pack(side=tk.LEFT,fill=tk.Y)



try:
	dbbible=db.connect('data/highlights.db')
	cur=dbbible.cursor()	
	cur.execute("""CREATE TABLE highlight(
		id_ INT,
		book INT,
		chapter INT,
		verse INT,
		book_ VARCHAR(255)
		);""")

	dbbible.close()
except:
	pass












load_images()
intro()


v1=time.time()

intro_()

update()
root.mainloop()
