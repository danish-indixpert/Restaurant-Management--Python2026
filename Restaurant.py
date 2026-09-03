import json
ordermenu=[]
class Order:
    def __init__(self,order_id,date,menu,category,table_status):
        self.order_id=order_id
        self.date=date
        self.menu=menu
        self.category=category
        self.table_status=table_status

        orde={
            "order_id":order_id,
            "date":date,
            "menu":menu,
            "category":category,
            "table_status":table_status
        }

        ordermenu.append(orde)
        print("Order Successfull")
    def order_process(self):
        with open("Order.json",'w') as file:
            json.dump(ordermenu,file,indent=4)
class Table:
    def __init__(self,big_table,medium_table,small_table):
        self.big_table=big_table
        self.medium=medium_table
        self.small_table=small_table

    def book_table(self):
        with open("Table.json",'r') as readfile:
            tables=json.load(readfile)
            print("==========")
            print("Table Menu")
            print("==========")
            print("1. Small Table")
            print("2. Medium Table")
            print("3. Big Table")
            table_choice=input("Enter your choice: ")
            order_book_id=input("Enter Order ID: ")
            for table in tables:
                if table["order_id"]==order_book_id:
                    if table["status"]=="Booked":
                        print("table is already book")
                        return 
                    else:
                        table["status"]="Booked"
                    print("table book successfull")
                

                with open("Table.json",'w') as file:
                    json.dump(tables,file,indent=4)
                    
                return
            print("order id not found")
                        

obj=Table(big_table=5,medium_table=8,small_table=10)
obj.book_table()