# import json
# import string
# import random
# from json import JSONDecodeError
# from datetime import datetime,date

# def AutoGenerate_EventID():
#     #generate a random Event ID
#     Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
#     return Event_ID

# def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
#     '''Register the member/ogranizer based on the type with the given details'''
#     if type.lower()=='organizer':
#         f=open(organizer_json_file,'r+')
#         d={
#             "Full Name":Full_Name,
#             "Email":Email,
#             "Password":Password
#         }
#         try:
#             content=json.load(f)
#             if d not in content:
#                 content.append(d)
#                 f.seek(0)
#                 f.truncate()
#                 json.dump(content,f)
#         except JSONDecodeError:
#             l=[]
#             l.append(d)
#             json.dump(l,f)
#         f.close()
#     else:
#         f=open(member_json_file,'r+')
#         d={
#             "Full Name":Full_Name,
#             "Email":Email,
#             "Password":Password
#         }
#         try:
#             content=json.load(f)
#             if d not in content:
#                 content.append(d)
#                 f.seek(0)
#                 f.truncate()
#                 json.dump(content,f)
#         except JSONDecodeError:
#             l=[]
#             l.append(d)
#             json.dump(l,f)
#         f.close()


# def Login(type,members_json_file,organizers_json_file,Email,Password):
#     '''Login Functionality || Return True if successful else False'''
#     d=0
#     if type.lower()=='organizer':
#         f=open(organizers_json_file,'r+')
#     else:
#         f=open(members_json_file,'r+')
#     try:
#         content=json.load(f)
#     except JSONDecodeError:
#         f.close()
#         return False
#     for i in range(len(content)):
#         if content[i]["Email"]==Email and content[i]["Password"]==Password:
#             d=1
#             break
#     if d==0:
#         f.close()
#         return False
#     f.close()
#     return True

# def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
#     '''Create an Event with the details entered by organizer'''
#     d={
#         "ID":Event_ID,
#         "Name":Event_Name,
#         "Start Date":Start_Date,
#         "Start Time": Start_Time,
#         "End Date":End_Date,
#         "End Time": End_Time,
#         "User Registered": Users_Registered,
#         "Capacity": Capacity,
#         "Seats Available": Availability
#         }
#     f=open(events_json_file, 'r+')
#     try:
#       content= json.load(f)
#       if d not in content:
#         content.append(d)
#         f.seek(0)
#         f.truncate()
#         json.dump(content, f)
#     except JSONDecodeError:
#        return False

# def View_Events(org,events_json_file):
#     '''Return a list of all events created by the logged in organizer'''
#     f=open(events_json_file, "r+")
#     content=json.load(f)
#     list_of_events=[]
#     for i in range (0,len(content)):
#         if content[i]["Organizer"]==org:
#             list_of_events.append(content[i])
#     f.close()
#     return list_of_events

# def View_Event_ByID(events_json_file,Event_ID):
#     '''Return details of the event for the event ID entered by user'''
#     f=open(events_json_file, "r+")
#     content=json.load(f)
#     list_of_events=[]
#     for i in range (0,len(content)):
#         if content[i]["ID"] == Event_ID:
#             list_of_events.append(content[i])
#             break
#     f.close()
#     return list_of_events

# def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
#     '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
#     || Return True if successful else False'''
#     f=open(events_json_file, "r+")
#     print(org)
#     try:
#         previous_data = json.load(f)
#         print(previous_data)
#         flag_check = False
#         for i in range(0,len(previous_data)):
#             if previous_data[i]["ID"]== event_id :#and previous_data[i]["Organizer"]==org:
#                 print(previous_data[i])
#                 previous_data[i][detail_to_be_updated]=updated_detail
#                 flag_check=True
#         f.seek(0)
#         f.truncate()
#         json.dump(previous_data, f)
#         if flag_check==True:
#             return True
#         else:
#             return False
#     except JSONDecodeError :
#         return False
#     except Exception as e:
#         print(e)
 
# def Delete_Event(org,events_json_file,event_ID):
#     '''Delete the Event with the entered Event ID || Return True if successful else False'''
#     f=open(events_json_file, "r+")
#     try:
#         previous_data = json.load(f)
#         new_data = []
#         flag_check = False
#         for i in range(0,len(previous_data)):
#             if previous_data[i]["ID"]==event_ID: #and previous_data[i]["Organizer"]==org:
#                 flag_check = True
#                 continue
#             else:
#                  new_data.append(previous_data[i])
#         f.seek(0)
#         f.truncate()
#         json.dump(new_data, f)
#         if flag_check==True:
#             return True
#         else:
#             return False
#     except JSONDecodeError:
#         return False

# def Register_for_Event(events_json_file,event_id,Full_Name):
#     '''Register the logged in member in the event with the event ID entered by member. 
#     (append Full Name inside the "Users Registered" list of the selected event)) 
#     Return True if successful else return False'''
#     date_today=str(date.today())
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     '''Write your code below this line'''
#     try:
#         with open(events_json_file, "r+") as f:
#             content = json.load(f)
#             for i in range (len(content)):
#                 if content[i]["ID"] == event_id:
#                    content[i]["Users Registered"].append({"Full_Name":Full_Name, "Date": date_today, "Time": current_time})
#                    f.seek(0)
#                    f.truncate()
#                    json.dump(content, f)
        
#             return True
#         return False
#     except JSONDecodeError:
#         return False
       
# def fetch_all_events(events_json_file,Full_Name,event_id,event_details):
#     # upcoming_ongoing
#     '''View Registered Events | Fetch a list of all events of the logged in memeber'''
#     '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
#     date_today=str(date.today())
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     '''Write your code below this line'''
#     f=open(events_json_file, "r+")
#     content=json.load(f)
#     list_of_events=[]
#     for i in range (0,len(content)):
#         if content[i]["ID"] == event_id:
#            content[i]["Users Registered"].append({"Full_Name":Full_Name, "Date": date_today, "Time": current_time})
#         list_of_events.append(content[i])
#         break
#     f.close()
#     return list_of_events

# def Update_Password(members_json_file,Full_Name,new_password):
#     '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
#     f=open(members_json_file, "r+")
#     try:
#         previous_data = json.load(f)
#         flag_check = False
#         for i in range(0,len(previous_data)):
#             if previous_data[i]["Full Name"] == Full_Name:
#                previous_data[i]["Password"] == new_password
#                flag_check = True
#         f.seek(0)
#         f.truncate()
#         json.dump(previous_data, f)
#         if flag_check==True:
#             return True
#         else:
#             return False
#     except JSONDecodeError:
#         return False

# def View_all_events(events_json_file):
#     '''Read all the events created | DO NOT change this function'''
#     '''Already Implemented Helper Function'''
#     details=[]
#     f=open(events_json_file,'r')
#     try:
#         content=json.load(f)
#         f.close()
#     except JSONDecodeError:
#         f.close()
#         return details
#     for i in range(len(content)):
#         details.append(content[i])
#     return details
import json
import string
import random
from json import JSONDecodeError
from datetime import datetime

def Register(type,gamers_json_file,sellers_json_file,Email_ID,Username,Password,Contact_Number):
    '''Register Function || Already Given'''
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
        return True
    elif type.lower()=='gamer':
        f=open(gamers_json_file,'r+')
        d={
            "Email":Email_ID,
            "Username":Username,
            "Password":Password,
            "Contact Number":Contact_Number,
            "Wishlist":[],
            "Cart":[],
        }
        try:
            content=json.load(f)
            if d not in content and d["Username"] not in str(content):
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()

def Login(type,gamers_json_file,sellers_json_file,Username,Password):
    '''Login Functionality || Return True if successfully logged in else False || Already Given'''
    d=0
    if type.lower()=='seller':
        f=open(sellers_json_file,'r+')
    else:
        f=open(gamers_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        return False
    for i in range(len(content)):
        if content[i]["Username"]==Username and content[i]["Password"]==Password:
            d=1
            break
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()
    if d==0:
        return False
    return True

def AutoGenerate_ProductID():
    '''Return a autogenerated random product ID || Already Given'''
    product_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    return product_ID

def AutoGenerate_OrderID():
    '''Return a autogenerated random product ID || Already Given'''
    Order_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Order_ID

def days_between(d1, d2):
    '''Calculating the number of days between two dates || Already Given'''
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def Create_Product(owner,product_json_file,product_ID,product_title,product_type,price_per_day,total_stock_available):
    '''Creating a product || Return True if successfully created else False'''
    '''---------Write your code below---------'''
    
    # Load product data from product_json_file
    with open(product_json_file, 'r') as f:
        products_data = json.load(f)

    # Check if the product_ID already exists
    if product_ID in products_data:
        print(f"Product with ID '{product_ID}' already exists.")
        return False

    # Create a new product entry
    product_entry = {
        'owner': owner,
        'product_title': product_title,
        'product_type': product_type,
        'price_per_day': price_per_day,
        'total_stock_available': total_stock_available
    }

    # Add the new product entry to the products_data
    products_data[product_ID] = product_entry

    # Save updated data back to the product_json_file
    with open(product_json_file, 'w') as f:
        json.dump(products_data, f, indent=4)

    print(f"Product '{product_ID}' created successfully.")
    return True
    # d={
    #     "Seller Username":owner, 
    #      "Product ID": product_ID,
    #      "Product Title": product_title,
    #      "Product Type": product_type, 
    #       "Price Per Day": price_per_day, 
    #       "Total Stock Available": total_stock_available}
    #   }
    # f=open(product_json_file,'r+')
    # try:
    #   content=json.load(f)
    #   if d not in content:
    #    content.append(d)
    #    f.seek(0)
    #    f.truncate()
    #    json.dump(content,f)
    # except JSONDecodeError:
    #   return False



def Fetch_all_Products_created_by_seller(owner,product_json_file):
    '''Get all products created by the seller(owner)'''
    '''---------Write your code below---------'''
    
    # Load product data from product_json_file
    with open(product_json_file, 'r') as f:
        products_data = json.load(f)

    # Filter products created by the seller(owner)
    seller_products = []
    for product_id, product_info in products_data.items():
        if product_info['owner'] == owner:
            seller_products.append(product_info)

    return seller_products
    # f=open(events_json_file, "r+")
    # content=json.load(f)
    # list_of_all_Products_created_by_seller=[]
    # for i in range (0,len(content)):
    #     if content[i]["Seller Username"] == owner:
    #        content[i]["Users Registered"].append({"owner_name":owner})
    #     list_of_all_Products_created_by_seller=[].append(content[i])
    #     break
    # f.close()
    # return list_of_all_Products_created_by_seller=[]
    

def Fetch_all_products(products_json_file):
    '''Get all products created till now || Helper Function'''
    '''Already Given'''
    All_Products_list=[]
    f=open(products_json_file,'r')
    try:
        content=json.load(f)
        All_Products_list=content
    except JSONDecodeError:
        pass
    return All_Products_list

def Fetch_Product_By_ID(product_json_file,product_ID):
    '''Get product deatils by product ID'''
    Details=[]
    f=open(product_json_file,'r+')
    content1=json.load(f)
    for i in range(len(content1)):
        if content1[i]["Product ID"]==product_ID:
            Details.append(content1[i])
            break
    f.close()
    return Details

def Update_Product(Username,product_json_file,product_ID,detail_to_be_updated,new_value):
    '''Updating Product || Return True if successfully updated else False'''
    d=0
    f=open(product_json_file,'r+')
    content2=json.load(f)
    for i in range(len(content2)):
        if content2[i]["Product ID"]==product_ID and detail_to_be_updated in content2[i].keys() and content2[i]["Seller Username"]==Username and detail_to_be_updated!="Product ID":
            content2[i][detail_to_be_updated]=new_value
            d=1
            break
    f.seek(0)
    f.truncate()
    json.dump(content2,f)
    f.close()
    if d==1:
        return True
    return False

def Add_item_to_wishlist(Username,product_ID,gamers_json_file):
    '''Add Items to wishlist || Return True if added successfully else False'''
    '''---------Write your code below---------'''

    # Load user data from gamers_json_file
    with open(gamers_json_file, 'r') as f:
        gamers_data = json.load(f)

    # Check if the user exists in the user data
    if Username not in gamers_data:
        print(f"User '{Username}' does not exist.")
        return False

    # Load product data from products_json_file
    with open('products.json', 'r') as f:
        products_data = json.load(f)

    # Check if the product_ID exists in the product data
    if product_ID not in products_data:
        print(f"Product with ID '{product_ID}' does not exist.")
        return False

    # Create a wishlist entry
    wishlist_entry = {
        'Product_ID': product_ID,
        'Product_Name': products_data[product_ID]['name'],
        'Price': products_data[product_ID]['price']
    }

    # Add the wishlist entry to the user's wishlist
    if 'wishlist' not in gamers_data[Username]:
        gamers_data[Username]['wishlist'] = []

    # Check if the product is already in the wishlist
    wishlist = gamers_data[Username]['wishlist']
    for item in wishlist:
        if item['Product_ID'] == product_ID:
            print(f"Product '{product_ID}' is already in {Username}'s wishlist.")
            return False

    gamers_data[Username]['wishlist'].append(wishlist_entry)

    # Save updated data back to the gamers_json_file
    with open(gamers_json_file, 'w') as f:
        json.dump(gamers_data, f, indent=4)

    print(f"Product '{product_ID}' added to {Username}'s wishlist successfully.")
    return True
    # f=open(gamers_json_file,'r+')
    # print(username)
    # try: 
    #    previous_data=json.load(f)
    #    print(previous_data)
    #    flag_check=False
    #    for i in range(0,len(previous_data)):
    #       if previous_data[i]["ID"]==event_id and previous_data[i]["username"]==username
    #       print(previous_data[i])
    #     #   previous_data[i][detail_to_be_updated]=updated_detail
    #       flag_check=True
    #    f.seek(0)
    #    f.truncate()
    #    json.dump(previous_data,f)
    #    if flag_check==True:
    #       return True
    #    else:
    #     return False
    # except JSONDecodeError:
    #      return False
    # except Exception as e:
    #     print(e)
       

def Remove_item_from_wishlist(Username,product_ID,gamers_json_file):
    '''Remove items from wishlist || Return True if removed successfully else False'''
    '''---------Write your code below---------'''
    
    # Load user data from gamers_json_file
    with open(gamers_json_file, 'r') as f:
        gamers_data = json.load(f)

    # Check if the user exists in the user data
    if Username not in gamers_data:
        print(f"User '{Username}' does not exist.")
        return False

    # Check if the user's wishlist is not empty
    if 'wishlist' not in gamers_data[Username] or not gamers_data[Username]['wishlist']:
        print(f"User '{Username}' has an empty wishlist. Nothing to remove.")
        return False

    # Find the product in the user's wishlist
    wishlist = gamers_data[Username]['wishlist']
    product_found = False
    for wishlist_item in wishlist:
        if wishlist_item['Product_ID'] == product_ID:
            product_found = True
            break

    if not product_found:
        print(f"Product with ID '{product_ID}' not found in {Username}'s wishlist.")
        return False

    # Update the user's wishlist to remove the item with the specified product_ID
    gamers_data[Username]['wishlist'] = [item for item in wishlist if item['Product_ID'] != product_ID]

    # Save updated data back to the gamers_json_file
    with open(gamers_json_file, 'w') as f:
        json.dump(gamers_data, f, indent=4)

    print(f"Product '{product_ID}' removed from {Username}'s wishlist successfully.")
    return True
    # f=open(gamers_json_file,"r+")
    # try:
    #    previous_data=json.load(f)
    #    new_data=[]
    #    flag_check=False
    #    for i in range(0,len(previous_data)):
    #       if previous_data[i]["ID"]==product_ID and previous_data[i]["username"]==Username:
    #          flag_check=True
    #          continue
    #       else:
    #          new_data.append(previous_data[i])
    #     f.seek(0)
    #     f.truncate()
    #     json.dump(new_data,f)
    #     if flag_check==True:
    #        return True
    #     else:
    #        return False
    # except JSONDecodeError:
    #    return False

    

def Add_item_to_cart(Username,product_ID,Quantity,gamers_json_file,booking_start_date,booking_end_date,products_json_file):
    '''Add item to the cart || Check whether the quantity mentioned is available || Return True if added successfully else False'''
    '''Add the Product ID, Quantity, Price, Booking Start Date, Booking End Date in the cart as list of dictionaries'''
    '''---------Write your code below---------'''
    
    with open(products_json_file, 'r') as f:
        products_data = json.load(f)

    
    if product_ID not in products_data:
        print(f"Product with ID '{product_ID}' does not exist.")
        return False

    
    product = products_data[product_ID]
    available_quantity = product['quantity']
    if Quantity > available_quantity:
        print(f"Only {available_quantity} units of Product '{product_ID}' are available.")
        return False

    
    with open(gamers_json_file, 'r') as f:
        gamers_data = json.load(f)

    
    if Username not in gamers_data:
        print(f"User '{Username}' does not exist.")
        return False

    
    cart_entry = {
        'Product_ID': product_ID,
        'Quantity': Quantity,
        'Price': product['price'],
        'Booking_Start_Date': booking_start_date,
        'Booking_End_Date': booking_end_date
    }


    if 'cart' not in gamers_data[Username]:
        gamers_data[Username]['cart'] = []

    gamers_data[Username]['cart'].append(cart_entry)

    # Update available quantity of the product
    products_data[product_ID]['quantity'] -= Quantity

    # Save updated data back to files
    with open(gamers_json_file, 'w') as f:
        json.dump(gamers_data, f, indent=4)

    with open(products_json_file, 'w') as f:
        json.dump(products_data, f, indent=4)

    print(f"Product '{product_ID}' added to {Username}'s cart successfully.")
    return True

    

def Remove_item_from_cart(Username,product_ID,gamers_json_file):
    '''Remove items from the cart || Return True if removed successfully else False'''
    '''---------Write your code below---------'''
    
    # Load user data from gamers_json_file
    with open(gamers_json_file, 'r') as f:
        gamers_data = json.load(f)

    # Check if the user exists in the user data
    if Username not in gamers_data:
        print(f"User '{Username}' does not exist.")
        return False

    # Check if the user's cart is not empty
    if 'cart' not in gamers_data[Username] or not gamers_data[Username]['cart']:
        print(f"User '{Username}' has an empty cart. Nothing to remove.")
        return False

    # Find the product in the user's cart
    cart = gamers_data[Username]['cart']
    product_found = False
    for cart_item in cart:
        if cart_item['Product_ID'] == product_ID:
            quantity_in_cart = cart_item['Quantity']
            product_found = True
            break

    if not product_found:
        print(f"Product with ID '{product_ID}' not found in {Username}'s cart.")
        return False

    # Update available quantity of the product in the user's cart
    gamers_data[Username]['cart'] = [item for item in cart if item['Product_ID'] != product_ID]

    # Save updated data back to the gamers_json_file
    with open(gamers_json_file, 'w') as f:
        json.dump(gamers_data, f, indent=4)

    print(f"Product '{product_ID}' removed from {Username}'s cart successfully.")
    return True
    # f=open(gamers_json_file,"r+")
    # try:
    #    previous_data=json.load(f)
    #    new_data=[]
    #    flag_check=False
    #    for i in range(0,len(previous_data)):
    #       if previous_data[i]["ID"]==product_ID and previous_data[i]["username"]==Username:
    #          flag_check=True
    #          continue
    #       else:
    #          new_data.append(previous_data[i])
    #     f.seek(0)
    #     f.truncate()
    #     json.dump(new_data,f)
    #     if flag_check==True:
    #        return True
    #     else:
    #        return False
    # except JSONDecodeError:
    #    return False
       
    


def View_Cart(Username,gamers_json_file):
    '''Return the current cart of the user'''
    f=open(gamers_json_file,'r')
    cart=[]
    try:
        content=json.load(f)
        for i in range(len(content)):
            if content[i]["Username"]==Username:
                cart=content[i]["Cart"]
                break
        return cart
    except JSONDecodeError:
        return cart

def Place_order(Username,gamers_json_file,Order_Id,orders_json_file,products_json_file):
    '''Place order || Return True is order placed successfully else False || Decrease the quantity of the product orderd if successfull'''
    '''---------Write your code below---------'''
    
    # Load user data from gamers_json_file
    with open(gamers_json_file, 'r') as f:
        gamers_data = json.load(f)

    # Check if the user exists in the user data
    if Username not in gamers_data:
        print(f"User '{Username}' does not exist.")
        return False

    # Check if the user's cart is not empty
    if 'cart' not in gamers_data[Username] or not gamers_data[Username]['cart']:
        print(f"User '{Username}' has an empty cart. Cannot place an order.")
        return False

    # Load order data from orders_json_file
    with open(orders_json_file, 'r') as f:
        orders_data = json.load(f)

    # Create a new order entry
    order_entry = {
        'Order_Id': Order_Id,
        'Username': Username,
        'Products': gamers_data[Username]['cart']
    }

    # Add the order entry to the orders_data
    orders_data.append(order_entry)

    # Update the user's cart to empty after placing the order
    gamers_data[Username]['cart'] = []

    # Save updated data back to files
    with open(gamers_json_file, 'w') as f:
        json.dump(gamers_data, f, indent=4)

    with open(orders_json_file, 'w') as f:
        json.dump(orders_data, f, indent=4)

    # Decrease the quantity of the ordered products in the products_data
    with open(products_json_file, 'r') as f:
        products_data = json.load(f)

    for product_entry in order_entry['Products']:
        product_ID = product_entry['Product_ID']
        quantity_ordered = product_entry['Quantity']
        products_data[product_ID]['quantity'] -= quantity_ordered

    with open(products_json_file, 'w') as f:
        json.dump(products_data, f, indent=4)

    print(f"Order '{Order_Id}' placed successfully for user '{Username}'.")
    return True
    

def View_User_Details(gamers_json_file,Username):
    '''Return a list with all gamer details based on the username || return an empty list if username not found'''
    '''---------Write your code below---------'''
    
    # Load user data from gamers_json_file
    with open(gamers_json_file, 'r') as f:
        gamers_data = json.load(f)

    # Check if the user exists in the user data
    if Username in gamers_data:
        return gamers_data[Username]

    # If the username is not found, return an empty list
    print(f"User '{Username}' not found.")
    return []
    # f=open(gamers_json_file,"r+")
    # content=json.load(f)
    # list_of_User=[]
    # for i in range(0,len(content)):
    #    if content[i]["username"]==Username:
    #       list_of_User.append(content[i])
    #       break
    # f.close()
    # return list_of_User
       
    

def Update_User(gamers_json_file,Username,detail_to_be_updated,updated_detail):
    '''Update the detail_to_be_updated of the user to updated_detail || Return True if successful else False'''
    '''---------Write your code below---------'''
    # def Update_User(gamers_json_file, Username, detail_to_be_updated, updated_detail):
    # Load user data from gamers_json_file
    with open(gamers_json_file, 'r') as f:
        gamers_data = json.load(f)

    # Check if the user exists in the user data
    if Username not in gamers_data:
        print(f"User '{Username}' does not exist.")
        return False

    # Check if the detail_to_be_updated exists in the user's data
    if detail_to_be_updated not in gamers_data[Username]:
        print(f"Detail '{detail_to_be_updated}' not found in {Username}'s data.")
        return False

    # Update the specified detail with the updated_detail
    gamers_data[Username][detail_to_be_updated] = updated_detail

    # Save updated data back to the gamers_json_file
    with open(gamers_json_file, 'w') as f:
        json.dump(gamers_data, f, indent=4)

    print(f"Detail '{detail_to_be_updated}' updated successfully for user '{Username}'.")
    return True

    # f=open(gamers_json_file,'r+')
    # print(username)
    # try: 
    #    previous_data=json.load(f)
    #    print(previous_data)
    #    flag_check=False
    #    for i in range(0,len(previous_data)):
    #       if previous_data[i]["username"]==Username
    #          print(previous_data[i])
    #          previous_data[i][detail_to_be_updated]=updated_detail
    #          flag_check=True
    #    f.seek(0)
    #    f.truncate()
    #    json.dump(previous_data,f)
    #    if flag_check==True:
    #       return True
    #    else:
    #     return False
    # except JSONDecodeError:
    #      return False
    # except Exception as e:
    #     print(e)
       

def Fetch_all_orders(orders_json_file,Username):
    '''Fetch all previous orders for the user and return them as a list'''
    orders=[]
    f=open(orders_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return orders
    for i in range(len(content)):
        if content[i]["Ordered by"]==Username:
            orders.append(content[i])
    return orders
    

