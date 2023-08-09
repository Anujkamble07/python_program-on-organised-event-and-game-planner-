# from json.decoder import JSONDecodeError
# import operations
# import json
# # "Organizer": "",2

# from json import JSONDecodeError

# print("Welcome to Meet app")
# tp=open("C:\\Users\\RUSHAB\\Desktop\\python\\exam_project\\organizers.json",'r+')
# try:
#     cp=json.load(tp)
#     if 'admin@edyoda.com' not in str(cp):
#         operations.Register('organizer','members.json','organizers.json','admin','admin@edyoda.com','admin')
#     tp.close()
# except JSONDecodeError:
#     operations.Register('organizer','members.json','organizers.json','admin','admin@edyoda.com','admin')
# c=1
# while True:
#     print("Press:")
#     print("1: Register")
#     print("2: Login")
#     print("0: Exit")
#     try:
#         c=int(input())
#     except ValueError:
#         print("Please enter valid choice")
#         continue
#     if c==1:
#         print("Press :")
#         print("1: Register as Organizer")
#         print("2: Register as Member")
#         try:
#             in1=int(input())
#         except ValueError:
#             print("Please enter valid choice")
#         if in1==1:
#             print("Enter Full Name:")
#             F=input()
#             print("Enter Email:")
#             E=input()
#             print("Enter Password:")
#             P=input()
#             if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
#                 print("Please enter valid data")
#                 continue
#             else:
#                 operations.Register('organizer','members.json','organizers.json',F,E,P)
#                 print("Registered successfully as Organizer")
#         elif in1==2:
#             print("Enter Full Name:")
#             F=input()
#             print("Enter Email:")
#             E=input()
#             print("Enter Password:")
#             P=input()
#             if (len(F)*len(E)*len(P))==0 or '@' not in E or '.com' not in E:
#                 print("Please enter valid data")
#                 continue
#             else:
#                 operations.Register('member','members.json','organizers.json',F,E,P)
#                 print("Registered successfully as Member")
#         else:
#             print("Please enter valid choice!")
#     elif c==2:
#         print("Press: ")
#         print("1: Login as Organizer")
#         print("2: Login as Member")
#         try:
#             in1=int(input())
#         except ValueError:
#             print("Please enter valid choice")
#         if in1==1:
#             print("Enter Email:")
#             E=input()
#             print("Enter Password:")
#             P=input()
#             s=operations.Login('organizer','members.json','organizers.json',E,P)
#             if s==False:
#                 print("Invalid Credentials")
#                 continue
#             else:
#                 t=open('organizers.json','r')
#                 cnt=json.load(t)
#                 t.close()
#                 n=""
#                 for i in range(len(cnt)):
#                     if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
#                         n=cnt[i]["Full Name"]
#                         break
#                 print("Welcome "+str(n))
#                 while True:
#                     print("Press :")
#                     print("1: Create Event")
#                     print("2: View all Events created")
#                     print("3: View Event Details by ID")
#                     print("4: Update Event")
#                     print("5: Delete Event")
#                     print("0: Logout")
#                     try:
#                         i1=int(input())
#                     except ValueError:
#                         print("Please enter valid choice")
#                     print(i1)
#                     if i1==1:
#                         Ev_ID=operations.AutoGenerate_EventID()
#                         print("Event ID Generated - "+str(Ev_ID))
#                         print("Enter Event Name:")
#                         Ev_Name=input()
#                         print("Enter Start Date (YYYY-MM-DD):")
#                         St_dt=input()
#                         print("Enter Start Time (HH:MM:SS):")
#                         St_t=input()
#                         print("Enter End Date (YYYY-MM-DD):")
#                         En_dt=input()
#                         print("Enter End Time (HH:MM:SS):")
#                         En_t=input()
#                         print("Enter Total Seats:")
#                         try:
#                             Cap=int(input())
#                         except ValueError:
#                             print("Please enter valid data")
#                             continue
#                         if (len(Ev_Name)*len(Ev_ID)*len(St_dt)*len(En_dt)*len(str(Cap)))==0 or len(St_dt)!=10 or len(En_dt)!=10 or len(St_t)!=8 or len(En_t)!=8 or St_dt>En_dt or (St_dt==En_dt and St_t>En_t):
#                             print("Please enter valid data")
#                             continue
#                         else:
#                           operations.Create_Event(n,'events.json',Ev_ID,Ev_Name,St_dt,St_t,En_dt,En_t,[],Cap,Cap)
#                           print("Event created successfully")
#                     elif i1==2:
#                         ev_details=operations.View_all_events('events.json')
#                         if len(ev_details)==0:
#                             print("No Events created yet! \n")
#                         else:
#                             for i in range(len(ev_details)):
#                                 print("Event ID: "+str(ev_details[i]['ID']))
#                                 print("Event Name: " +str(ev_details[i]['Name']))
#                                 print("Organizer: " +str(ev_details[i]['Organizer']))
#                                 print("Start Date: " +str(ev_details[i]['Start Date']))
#                                 print("Start Time: " +str(ev_details[i]['Start Time']))
#                                 print("End Date: " +str(ev_details[i]['End Date']))
#                                 print("End Time: " +str(ev_details[i]['End Time']))
#                                 print("Total Users Registered: "+str(len(ev_details[i]["Users Registered"])))
#                                 print("Seats Available: "+str(ev_details[i]['Seats Available']))
#                                 print('\n')
#                     elif i1==3:
#                         print("Enter Event ID")
#                         ev_id=input()
#                         f14=open('events.json','r')
#                         try:
#                             c14=str(json.load(f14))
#                             if ev_id not in c14:
#                                 print("Invalid event ID")
#                                 continue
#                         except JSONDecodeError:
#                             print("Events not available")
#                             continue
#                         d=operations.View_Event_ByID('events.json',ev_id)
#                         print("Event Name: " +str(d[0]['Name']))
#                         print("Organizer: " +str(d[0]['Organizer']))
#                         print("Start Date: " +str(d[0]['Start Date']))
#                         print("Start Time: " +str(d[0]['Start Time']))
#                         print("End Date: " +str(d[0]['End Date']))
#                         print("End Time: " +str(d[0]['End Time']))
#                         print("Total Seats: "+str(d[0]["Capacity"]))
#                         print("Seats Available: "+str(d[0]['Seats Available']))
#                         print('\n')
#                     elif i1==4:
#                         print("Enter Event ID:")
#                         ev_id=input()
#                         print("Enter detail to be Updated ( Name || Start Date || Start Time || End Time || End Date ): ")
#                         dtl=input()
#                         print("dtl::::",dtl)
#                         print("Enter new value:")
#                         updtl=input()
                        
#                         f11=open('events.json','r')
#                         try:
#                             print("inside try ::::")
#                             c11=str(json.load(f11))
#                             print(c11)
#                             f11.close()
#                         except JSONDecodeError:
#                             print("No events created")
#                             f11.close()
#                             continue
#                         if ev_id not in c11:
#                             print("Invalid event ID")
#                             continue
#                         if (len(ev_id)*len(dtl)*len(updtl))==0:
#                             print("Please enter valid data")
#                             continue
#                         else:
#                             print("inside else.........")
#                             ch=operations.Update_Event(n,'events.json',ev_id,dtl,updtl)
                        
#                         if ch==False:
#                             print("Cannot update event")
#                         else:
#                             print("Event updated successfully")
#                     elif i1==5:
#                         print("Enter Event ID")
#                         event_id=input()
#                         f1=open('events.json','r')
#                         try:
#                             c1=str(json.load(f1))
#                             f1.close()
#                         except JSONDecodeError:
#                             print("No events created")
#                             f1.close()
#                             continue
#                         if event_id not in c1:
#                             print("Invalid event ID")
#                             continue
#                         if len(event_id)==0:
#                             print("Please enter valid data")
#                             continue
#                         else:
#                             o1=operations.Delete_Event(n,'events.json',event_id)
#                         if o1==True:
#                             print("Event deleted successfully")
#                         else:
#                             print("Cannot delete event")
#                     elif i1==0:
#                         break
#                     else:
#                         print("Ivalid Option")
#         elif in1==2:
#             print("Enter Email:")
#             E=input()
#             print("Enter Password:")
#             P=input()
#             s=operations.Login('member','members.json','organizers.json',E,P)
#             if s==False:
#                 print("Invalid Credentials")
#                 continue
#             else:
#                 t=open('members.json','r')
#                 cnt=json.load(t)
#                 t.close()
#                 n=""
#                 for i in range(len(cnt)):
#                     if cnt[i]["Email"]==E and cnt[i]["Password"]==P:
#                         n=cnt[i]["Full Name"]
#                         break
#                 print("Welcome "+str(n))
#                 while True:
#                     print("Press:")
#                     print("1: View Registered Events")
#                     print("2: Register for an Event")
#                     print("3: Update Password")
#                     print("4: View Event Details by ID")
#                     print("0: Logout")
#                     try:
#                         i3=int(input())
#                     except ValueError:
#                         print("Please enter valid choice")
#                     if i3==1:
#                         all_events=[]
#                         upcoming_ongoing=[]
#                         operations.fetch_all_events('events.json',n,all_events,upcoming_ongoing)
#                         print("All Upcoming/Ongoing Events: ")
#                         for i in range(len(upcoming_ongoing)):
#                             print("Event Name: " +str(upcoming_ongoing[i]['Name']))
#                             print("Start Date: " +str(upcoming_ongoing[i]['Start Date']))
#                             print("Start Time: " +str(upcoming_ongoing[i]['Start Time']))
#                             print("End Date: " +str(upcoming_ongoing[i]['End Date']))
#                             print("End Time: " +str(upcoming_ongoing[i]['End Time']))
#                             print("Organizer: " +str(upcoming_ongoing[i]['Organizer']))
#                             print('\n')
#                     elif i3==2:
#                         l=operations.View_all_events('events.json')
#                         if len(l)==0:
#                             print("No events available")
#                         else:
#                             print("All Events: ")
#                             for i in range(len(l)):
#                                 t=l[i]
#                                 print("Event ID: "+str(t['ID']))
#                                 print("Event Name: " +str(t['Name']))
#                                 print("Organizer: "+str(t['Organizer']))
#                                 print("Start Date: " +str(t['Start Date']))
#                                 print("Start Time: " +str(t['Start Time']))
#                                 print("End Date: " +str(t['End Date']))
#                                 print("End Time: " +str(t['End Time']))
#                                 print("Seats Available: "+str(t['Seats Available']))
#                                 print("Total Seats: "+str(t['Capacity']))
#                                 print('\n')
#                         print("Enter Event ID: ")
#                         event_ID=input()
#                         ch=operations.Register_for_Event('events.json',event_ID,n)
#                         f44=open('events.json','r')
#                         c44=str(json.load(f44))
#                         if event_ID not in c44:
#                             print("Invalid Event ID")
#                         if ch==True:
#                             print("Successfully Registered")
#                         else:
#                             print("Event seats are full! \n")
#                     elif i3==3:
#                         print("Enter new password")
#                         pswd=input()
#                         if(len(pswd))<4:
#                             print("Please enter valid data")
#                             continue
#                         op=operations.Update_Password('members.json',n,pswd)
#                         if op==True:
#                             print("Password updated successfully")
#                         else:
#                             print("Cannot update password")
#                     elif i3==4:
#                         print("Enter Event ID")
#                         ev_id=input()
#                         f14=open('events.json','r')
#                         try:
#                             c14=str(json.load(f14))
#                             if ev_id not in c14:
#                                 print("Invalid event ID")
#                                 continue
#                         except JSONDecodeError:
#                             print("Events not available")
#                             continue
#                         d=operations.View_Event_ByID('events.json',ev_id)
#                         print("Event Name: " +str(d[0]['Name']))
#                         print("Start Date: " +str(d[0]['Start Date']))
#                         print("Start Time: " +str(d[0]['Start Time']))
#                         print("End Date: " +str(d[0]['End Date']))
#                         print("End Time: " +str(d[0]['End Time']))
#                         print("End Time: " +str(d[0]['End Time']))
#                         print("Organizer: "+str(d[0]["Organizer"]))
#                         print("Seats Available: "+str(d[0]['Seats Available']))
#                         print('\n')
#                     elif i3==0:
#                         break
#                     else:
#                         print("Invalid Choice, Please enter again")
#                         continue
#     elif c==0:
#         break
#     else:
#         print("Invalid Choice, Please enter again")
#         continue

import operations
import json
from json import JSONDecodeError

print("Welcome to Game Rental App")
while(1):
    print("Press: ")
    print("1. Register as Seller")
    print("2. Register as Gamer")
    print("3. Login as Seller")
    print("4. Login as Gamer")
    print("5. Exit")
    in1=int(input())
    if in1==1:
        print("Enter Email ID")
        Email_ID=input()
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        print("Enter Contact Number")
        Contact_Number=input()
        try:
            f=open('Sellers.json','r')
            content=json.load(f)
            if Username in str(content):
                print("Username already exists !!")
                continue
        except JSONDecodeError:
            pass
        if "@admin.com" not in Email_ID or (len(Email_ID)*len(Username)*len(Password)*len(Contact_Number))==0 or len(str(Contact_Number))!=10 or len(Password)<=4:
            print("Please Enter Valid Data !!")
            continue
        else:
            operations.Register('seller','Gamers.json','Sellers.json',Email_ID,Username,Password,Contact_Number)
            print("Registered Successully as Seller")
            continue
    elif in1==2:
        print("Enter Email ID")
        Email_ID=input()
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        print("Enter Contact Number")
        Contact_Number=input()
        if ".com" not in Email_ID or (len(Email_ID)*len(Username)*len(Password)*len(Contact_Number))==0 or len(Contact_Number)!=10 or len(Password)<=4:
            print("Please Enter Valid Data")
            continue
        else:
            operations.Register('gamer','Gamers.json','Sellers.json',Email_ID,Username,Password,Contact_Number)
            print("Registered Successully as Gamer")
            continue
    elif in1==3:
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        ch=operations.Login('seller','Gamers.json','Sellers.json',Username,Password)
        if ch==True:
            f=open('Sellers.json','r')
            content=json.load(f)
            user_details=[]
            for i in range(len(content)):
                if content[i]["Username"]==Username:
                    user_details=content[i]
                    break
            print("Welcome "+str(Username))
            while(1):
                print("Press: ")
                print("1. Create Product")
                print("2. Update Product")
                print("3. View all created Products")
                print("4. View Product Details by ID")
                print("5. View User Profile")
                print("6. Logout")
                in2=int(input())
                if in2==1:
                    Product_id=operations.AutoGenerate_ProductID()
                    print("Product ID generated is "+str(Product_id))
                    print("Enter Product Name")
                    Product_Name=input()
                    print("Enter Product Type")
                    Product_type=input()
                    print("Enter Price per Day")
                    Price_per_day=int(input())
                    print("Enter Total Stock Available")
                    total_stock=int(input())
                    if len(Product_Name)*len(Product_type)==0 or Price_per_day<=0 or total_stock<=0:
                        print("Please enter valid data !!")
                        continue
                    operations.Create_Product(Username,'Products.json',Product_id,Product_Name,Product_type,Price_per_day,total_stock)
                    print("Product Created Successfully")
                elif in2==2:
                    print("Enter Product ID")
                    Product_id=input()
                    print("Enter Detail to be updated(Product Title | Product Type | Price Per Day | Total Stock Available)")
                    Detail_to_be_updated=input()
                    print("Enter Updated detail")
                    Updated_detail=input()
                    ch=operations.Update_Product(Username,'Products.json',Product_id,Detail_to_be_updated,Updated_detail)
                    if ch==True:
                        print("Product updated successfully !!")
                    else:
                        print("Product not updated !!")
                elif in2==3:
                    details=operations.Fetch_all_Products_created_by_seller(Username,'Products.json')
                    if len(details)==0:
                        print("No Products Created !!")
                    else:
                        for i in range(len(details)):
                            print("Product ID: "+str(details[i]["Product ID"]))
                            print("Product Title: "+str(details[i]["Product Title"]))
                            print("Product Type: "+str(details[i]["Product Type"]))
                            print("Price Per Day: "+str(details[i]["Price Per Day"]))
                            print("Total Stock Available: "+str(details[i]["Total Stock Available"]))
                            print('\n')
                elif in2==4:
                    print("Enter Product ID")
                    Product_Id=input()
                    details=operations.Fetch_Product_By_ID('Products.json',Product_Id)
                    if len(details)==0:
                        print("Invalid ID")
                    else:
                         for i in range(len(details)):
                            print("Product Title: "+str(details[i]["Product Title"]))
                            print("Product Type: "+str(details[i]["Product Type"]))
                            print("Price Per Day: "+str(details[i]["Price Per Day"]))
                            print("Total Stock Available: "+str(details[i]["Total Stock Available"]))
                            print('\n')
                         continue
                elif in2==5:
                    print("Enter Username")
                    usrnm=input()
                    details=operations.View_User_Details('Gamers.json',usrnm)
                    if len(details)==0:
                        print("Invalid Username")
                    else:
                        for i in range(len(details)):
                            print("Email: "+str(details[i]["Email"]))
                            print("Contact Number: "+str(details[i]["Contact Number"]))
                            print("Wishlist: "+str(details[i]["Wishlist"]))
                            print("Cart: ")
                            cart=details[i]["Cart"]
                            for j in range(len(cart)):
                                print("  Product ID: "+str(cart[j]["Product ID"]))
                                print("  Quantity: "+str(cart[j]["Quantity"]))
                                print("  Price Per Day: "+str(cart[j]["Price"]))
                                print("  Booking Start Date: "+str(cart[j]["Booking Start Date"]))
                                print("  Booking End Date: "+str(cart[j]["Booking End Date"]))
                                print('\n')
                            print('\n')
                        continue
                elif in2==6:
                    break
                else:
                    print("Please Enter valid input")
        else:
            print("Invalid Credentials !!")
    elif in1==4:
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        ch=operations.Login('gamer','Gamers.json','Sellers.json',Username,Password)
        if ch==True:
            print("Welcome "+str(Username))
            in3=1
            while(in3!=7):
                print("Press: ")
                print("1. View all Product")
                print("2. Manage wishlist")
                print("3. Manage cart")
                print("4. Place order")
                print("5. Update Profile")
                print("6. View Orders")
                print("7. Logout")
                in3=int(input())
                if in3==1:
                    l=operations.Fetch_all_products('Products.json')
                    if len(l)==0:
                        print("No Products created !!")
                    else:
                        for i in range(len(l)):
                            print("Product ID: "+str(l[i]["Product ID"]))
                            print("Product Title: "+str(l[i]["Product Title"]))
                            print("Product Type: "+str(l[i]["Product Type"]))
                            print("Price Per Day: "+str(l[i]["Price Per Day"]))
                            print("Total Stock Available: "+str(l[i]["Total Stock Available"]))
                            print('\n')
                        continue
                elif in3==2:
                    print("Press: ")
                    print("1. Add item to wishlist")
                    print("2. Remove Item from wishlist")
                    in31=int(input())
                    if in31==1:
                        print("Enter Product ID")
                        Product_Id=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                        except JSONDecodeError:
                            print("No products created !!")
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        else:
                            ch=operations.Add_item_to_wishlist(Username,Product_Id,'Gamers.json')
                            if ch==True:
                                print("Added item successfully !!")
                                continue
                            else:
                                print("Cannot add item !!")
                                continue
                    if in31==2:
                        print("Enter Product ID")
                        Product_Id=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                        except JSONDecodeError:
                            print("No products created !!")
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        else:
                            ch=operations.Remove_item_from_wishlist(Username,Product_Id,'Gamers.json')
                            if ch==True:
                                print("Removed item successfully !!")
                                continue
                            else:
                                print("Cannot remove item !!")
                                continue
                    else:
                        print("Please Enter Valid choice")
                elif in3==3:
                    print("Press: ")
                    print("1. Add item to cart")
                    print("2. Remove Item from cart")
                    print("3. View Cart")
                    in31=int(input())
                    if in31==1:
                        print("Enter Product ID")
                        Product_Id=input()
                        print("Enter Quantity")
                        Quantity=int(input())
                        print("Enter Booking Start Date (YYYY-MM-DD)")
                        Booking_start_date=input()
                        print("Enter Booking End Date (YYYY-MM-DD)")
                        Booking_end_date=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                            f.close()
                        except JSONDecodeError:
                            print("No products created !!")
                            f.close()
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        can_add=operations.Add_item_to_cart(Username,Product_Id,Quantity,'Gamers.json',Booking_start_date,Booking_end_date,'Products.json')
                        f.close()
                        if can_add==True:
                            print("Added item successfully !!")
                            continue
                        else:
                            print("Cannot add item to cart !!")
                            continue
                    if in31==2:
                        print("Enter Product ID")
                        Product_Id=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                            f.close()
                        except JSONDecodeError:
                            print("No products created !!")
                            f.close()
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        can_remove=operations.Remove_item_from_cart(Username,Product_Id,'Gamers.json')
                        if can_remove==True:
                            print("Item removed successfully from cart !!")
                        else:
                            print("Cannot remove item")
                    elif in31==3:
                        cart=operations.View_Cart(Username,'Gamers.json')
                        if len(cart)==0:
                            print("Cart Empty !!")
                        else:
                            for i in range(len(cart)):
                                print("Product ID: "+str(cart[i]["Product ID"]))
                                print("Quantity: "+str(cart[i]["Quantity"]))
                                print("Price Per Day: "+str(cart[i]["Price"]))
                                print("Booking Start Date: "+str(cart[i]["Booking Start Date"]))
                                print("Booking End Date: "+str(cart[i]["Booking End Date"]))
                                print('\n')
                    else:
                        print("Please Enter Valid choice")
                elif in3==4:
                    Order_id=operations.AutoGenerate_OrderID()
                    print("Order ID genrated is "+str(Order_id))
                    order_placed=operations.Place_order(Username,'Gamers.json',Order_id,'Orders.json','Products.json')
                    if order_placed==True:
                        print("Order Placed Successfully with Order ID "+str(Order_id))
                    else:
                        print("Order Unsuccessful !!")
                elif in3==5:
                    print("Enter Detail to be updated ( Email | Password | Contact Number )")
                    Detail_to_be_updated=input()
                    print("Enter Updated detail")
                    Updated_detail=input()
                    upd=operations.Update_User('Gamers.json',Username,Detail_to_be_updated,Updated_detail)
                    if upd==True:
                        print("Profile Updated successfully !!")
                    else:
                        print("Cannot Update Profile !!")
                elif in3==6:
                    orders=operations.Fetch_all_orders('Orders.json',Username)
                    if len(orders)==0:
                        print("No orders placed !!")
                    else:
                        for i in range(len(orders)):
                            print("Order ID: "+str(orders[i]["Order ID"]))
                            print("Items: ")
                            cart=orders[i]["Items"]
                            for j in range(len(cart)):
                                print("  Product ID: "+str(cart[j]["Product ID"]))
                                print("  Quantity: "+str(cart[j]["Quantity"]))
                                print("  Price Per Day: "+str(cart[j]["Price"]))
                                print("  Booking Start Date: "+str(cart[j]["Booking Start Date"]))
                                print("  Booking End Date: "+str(cart[j]["Booking End Date"]))
                                print('\n')
                            print("Total Cost: "+str(orders[i]["Total Cost"]))
                elif in3==7:
                    break
                else:
                    print("Please Enter Valid choice")
        else:
            print("Invalid Credentials !!")
    elif in1==5:
        break
    else:
        print("Please Enter Valid choice")                    