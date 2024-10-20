import os    # Why do we import os?
import pickle
import time

#1 To add elementa
def insert(n):
    for i in range(n):
        p_no=input("Enter product number:")
        p_name=input("Enter product's name:")
        p_company=input("Enter product's company of origin:")
        p_price=input("Enter product's price:")
        p_quantity=input("Enter product's quantity:")
        p_date=input("Enter product's date of purchase:")
        p_rec={"Product Number":p_no,"Name":p_name,"Company":p_company,                #Dictionary, list and tuple work in this form.
               "Price":p_price,"Quantity":p_quantity,"Date of purchase":p_date}
        f=open("product.dat","ab")                                                     #'.dat' is what?
        pickle.dump(p_rec,f)
        print(p_rec)
        f.close()
#2 To display all elements
def read():
    f=open("product.dat","rb")
    print("Product Number",
                  "\tName",
                  "\t\tCompany",
                  "\tPrice",
                  "\t\tQuantity",
                  "\tDate of Purchase")
    while True:
        try:
            p_rec=pickle.load(f)
            print(p_rec["Product Number"],
                  "\t\t",
                  p_rec["Name"],
                  "\t\t",
                  p_rec["Company"],                                   #print() can work in this form too.
                  "\t\t",
                  p_rec["Price"],
                  "\t\t",
                  p_rec["Quantity"],
                  "\t\t",
                  p_rec["Date of purchase"])
        except EOFError:
            break
    f.close()
#3 To display specific elements
def search(p):
    f=open("product.dat","rb")
    flag=False
    while True:
        try:
            p_rec=pickle.load(f)
            if p_rec["Product Number"]==p:
                print("Product number",
                  "\tName",
                  "\t\tCompany",
                  "\tPrice",
                  "\t\tQuantity",
                  "\tDate of Purchase")
                print(p_rec["Product Number"],
                  "\t\t",
                  p_rec["Name"],
                  "\t\t",
                  p_rec["Company"],                                   
                  "\t\t",
                  p_rec["Price"],
                  "\t\t",
                  p_rec["Quantity"],
                  "\t\t",
                  p_rec["Date of purchase"])
                flag=True
        except EOFError:
            break
    if flag==False:
        print("No record found.")
    f.close()

#4 To add new elemets(In exisitng data)
def update(r,a,b,c,d,e):
    f=open("product.dat","rb")
    reclst=[]
    while True:
        try:
            p_rec=pickle.load(f)
            reclst.append(p_rec)
        except EOFError:
            break
    f.close()
    f1=open("product.dat","wb")
    for i in range(len(reclst)):
        if reclst[i]["Product Number"]==r:
            reclst[i]["Name"]=a
            reclst[i]["Company"]=b
            reclst[i]["Price"]=c
            reclst[i]["Quantity"]=d
            reclst[i]["Date of purchase"]=e
    for x in reclst:
        pickle.dump(x,f1)
        f.close()
    print("Record updated successfully.")
    reclst.clear()

#5 To remove elements
def delete(r):
    f=open("product.dat","rb")
    reclst=[]
    while True:
        try:
            p_rec=pickle.load(f)
            reclst.append(p_rec)
        except EOFError:
            break
    f.close()
    f=open("product.dat","wb")
    for x in reclst:
        if x["Product Number"]==r:
            continue
        pickle.dump(x,f)
        f.close()
def main():
    count=0
    print('''=====================================================================================
=                           CANTEEN MANAGEMENT PROGRAM                              =
=====================================================================================''')
    time.sleep(1)
    while True:
        if count==0:
            print("1.CREATE PRODUCTS")
            time.sleep(1)
            print("2.DISPLAY PRODUCTS")
            time.sleep(1)
            print("3.SEARCH PRODUCTS")
            time.sleep(1)
            print("4.MODIFY PRODUCT RECORD")
            time.sleep(1)
            print("5.DELETE PRODUCT RECORD")
            time.sleep(1)
            print("6.EXIT")
            time.sleep(1)
        else:
            print("1.CREATE PRODUCTS")
            print("2.DISPLAY PRODUCTS")
            print("3.SEARCH PRODUCTS")
            print("4.MODIFY PRODUCT RECORD")
            print("5.DELETE PRODUCT RECORD")
            print("6.EXIT")
        choice=int(input("Enter your choice:"))
        count+=1
        if choice==1:
            n=int(input("Enter number of elements:"))
            insert(n)
            continue
        elif choice==2:
            read()
            continue
        elif choice==3:
            p=input("Enter product number:")
            search(p)
            continue
        elif choice==4:
            r=input("Enter product number:")
            a=input("Enter product name:")
            b=input("Enter company:")
            c=input("Enter price:")
            d=input("Enter quantity:")
            e=input("Enter purchase date:")
            update(r,a,b,c,d,e)
            continue
        elif choice==5:
            r=input("Enter product number:")
            delete(r)
            print("Record deleted successfully.")
            continue
        elif choice==6:
            print("Exiting program",end="")
            for i in range(2):
                time.sleep(0.5)
                print(".",end="")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            print("Program has been terminated.")
            break
        else:
            print("Wrong input.")
            continue
if __name__=="__main__":
    main()      
