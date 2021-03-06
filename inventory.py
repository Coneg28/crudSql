from tkinter import *
 
 
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=COMPLAB503_PC2;'
                      'Database=db_clothing_line;'
                      'Trusted_Connection=yes;')
 
class Product:
    def __init__(self, name, price, size, description):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__size = size
 
    def getName(self):
        return self.__name
 
    def getPrice(self):
        return self.__price
 
    def getDescription(self):
        return self.__description
 
    def getSize(self):
        return self.__size
 
 
 
def addProduct():
    product = Product(e1.get(), e2.get(), e3.get(), e4.get())
    cursor = conn.cursor()
    cursor.execute("INSERT into products (name, price ,size, description, timestamp) values ('"+ product.getName() +"',"+ product.getPrice() +",'"+ product.getSize() + "','"+ product.getDescription() +"' ,CURRENT_TIMESTAMP)")
    cursor.commit()
    viewProducts()
 
def deleteProduct(product):
    cursor = conn.cursor()
    cursor.execute('DELETE products where name = '+ product )
    viewProducts()
 
def updateProduct(product):
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e1.insert(0, product[1])
    e2.insert(0, product[2])
    e3.insert(0, product[3])
    e4.insert(0, product[4])
   
    btn1['state'] = NORMAL
    btn2['state'] = DISABLED
    btn1.configure(command=lambda: updateIt(e1.get(), e2.get(), e3.get(), e4.get(), product[0]))
 
def updateIt(name, price, size, description, id):
    cursor = conn.cursor()
    cursor.execute("UPDATE products set name = '"+name+"', price = "+price+", size = '"+size+"', description = '"+description+"',timestamp = CURRENT_TIMESTAMP where id =" +str(id))
    cursor.commit()
    btn1['state'] = DISABLED
    btn2['state'] = NORMAL
    viewProducts()
    Label(root, text="").grid(row=1, column=3, sticky=W, padx=10, pady=5)
    Label(root, text="").grid(row=2, column=3, sticky=W, padx=10, pady=5)
    Label(root, text="").grid(row=3, column=3, sticky=W, padx=10, pady=5)
    Label(root, text="").grid(row=4, column=3, sticky=W, padx=10, pady=5)
 
def viewProducts():
    row = 1
    list = separator.grid_slaves()
    for l in list:
        l.destroy()
   
    cursor = conn.cursor()
    cursor.execute("Select * from products")
    addHeaders()
    for product in cursor.fetchall():
        Label(separator, text=product[1], background=color, width=10).grid(row=row, column=0, sticky=W+E+N+S , padx=10, pady=5)
        Label(separator, text=product[2], background=color, width=10).grid(row=row, column=1, sticky=W+E+N+S , padx=10, pady=5)
        Label(separator, text=product[3],background=color, width=10).grid(row=row, column=2, sticky=W+E+N+S , padx=10, pady=5)
        Label(separator, text=product[4],background=color, width=10).grid(row=row, column=3, sticky=W+E+N+S , padx=10, pady=5)
        Label(separator, text=product[5],background=color, width=10).grid(row=row, column=4, sticky=W+E+N+S , padx=10, pady=5)        
        btn_a1 = Button(separator, text="Update", width=7, command=lambda prod=product: updateProduct(product))
        btn_a2 = Button(separator, text="Delete", width=7, command=lambda prod=product: deleteProduct(product[0]))
 
        btn_a1.grid(row=row, column=5, sticky=W, padx=5, pady=5)
        btn_a2.grid(row=row, column=6, sticky=E, padx=5, pady=5)
        row += 1
 
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
 
def addHeaders():    
    separator.grid(row=6, column=0, columnspan=5, pady=5, sticky=W+E+N+S)
    Label(separator, text="Name", background=color, width=10).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(separator, text="Price", background=color, width=10).grid(row=0, column=1, sticky=W, padx=10, pady=5)
    Label(separator, text="Size",background=color, width=10).grid(row=0, column=2, sticky=W, padx=10, pady=5)
    Label(separator, text="Description",background=color, width=10).grid(row=0, column=3, sticky=W, padx=10, pady=5)
    Label(separator, text="Timestamp",background=color, width=20).grid(row=0, column=4, sticky=W, padx=10, pady=5)
    Label(separator, text="Action", background=color, width=10).grid(row=0, column=5, sticky=W, padx=10, pady=5, columnspan=2)
 

color = "#d9d7d7"
bgColor = "#031222"
fgColor = "#f8b4c1"
 
root = Tk()
root.title("Simple Inventory System")
root.geometry("650x600")
root.resizable(0, 0)
root.configure(bg = bgColor)
 
Label(root, text="PRODUCT INFORMATION", bg= bgColor, font = "Century_Gothic 16 bold",fg = fgColor).grid(row=0, column=1, sticky=E, padx=10, pady=5)
Label(root, text="Product Name: ",  bg= bgColor, font = "Century_Gothic 12 ",fg = fgColor).grid(row=1, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Price: ",  bg= bgColor, font = "Century_Gothic 12 ",fg = fgColor).grid(row=2, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Size: ",  bg= bgColor, font = "Century_Gothic 12 ",fg = fgColor).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Description: ",  bg= bgColor, font = "Century_Gothic 12 ",fg = fgColor).grid(row=4, column=0, sticky=W, padx=10, pady=5)
 
e1 = Entry(root, width=45)
e2 = Entry(root, width=45)
e3 = Entry(root, width=45)
e4 = Entry(root, width=45)
 
e1.grid(row=1, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e2.grid(row=2, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e3.grid(row=3, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e4.grid(row=4, column=1, sticky=W, padx=10, pady=5, columnspan=2)
 
btn1 = Button(root, text="Update Product", width=15, state=DISABLED)
btn2 = Button(root, text="Add Product", width=15, state=NORMAL, command=addProduct)
 
btn1.grid(row=5, column=1, sticky=W, pady=5)
btn2.grid(row=5, column=1, sticky=E,  pady=5)
 
separator = Canvas(root, height=100, width=420, background=color, relief=SUNKEN)
addHeaders()
viewProducts()
root.mainloop()