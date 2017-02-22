import sqlite3


def question1(c):
	c.execute('pragma table_info(fortunes)')
	for i in c:
		print (i)

def question2(c):
	c.execute('select count(*) from fortunes')
	for i in c:
		return(i[0])se
	
def question3(c):
	c.execute('select count(*) from fortunes where filename="startrek"')
	for i in c:
		return(i[0])
		
def question4(c):
	c.execute('select count(size) from fortunes where filename="limerick"')
	for i in c:
		return(i[0])

def question5(c):
	c.execute('select aphorism from fortunes where aphorism like "%Flintstone%"')
	for i in c:
		return(i[0])
		
def question6(c):
	c.execute('select aphorism from fortunes where aphorism like "%Star trek%"')
	for i in c:
		return(i[0])

		
def main():

	db = sqlite3.connect('freebsd_fortunes_clean.sl3')
	c = db.cursor()
	
	print('\n1 - What is the schema of the database?')
	question1(c)
	print('\n2 - How many rows are there in the database?')
	print(question2(c))
	print('\n3 - How many rows are from the filename startrek?')
	print(question3(c))
	print('\n4 - What is the average length of the aphorisms that have a filename of "limerick"?')
	print(question4(c))
	print('\n5 - What is the id and the text of the aphorism that contains the string "Flintstone"')
	print(question5(c))
	print('\n6 - Select a Star Trek quote or limerick of your choice and print it out.')
	print(question6(c))

if __name__ == '__main__':
	main()
	

