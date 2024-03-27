# Problem One

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Water": 1.50, "Soda": 2.00}
restaurant_menu["Main Course"]["Steak"] = 17.99
del restaurant_menu["Starters"]["Bruschetta"]
print("Updated Restaurant Menu:")

for category, items in restaurant_menu.items():
    print(f"{category}:")
    for item, price in items.items():
        print(f"\t{item}: ${price}")




# Problem Two - Task One
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_number, customer_name):
    if hotel_rooms.get(room_number):
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} has been booked for {customer_name}.")
        else:
            print(f"Sorry, room {room_number} is already booked.")
    else:
        print("Invalid room number.")

def checkout_customer(room_number):
    if hotel_rooms.get(room_number):
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"{customer_name} has checked out from room {room_number}.")
        else:
            print(f"Room {room_number} is not booked.")
    else:
        print("Invalid room number.")

def display_room_status():
    print("Room Status:")
    for room_number, details in hotel_rooms.items():
        print(f"Room {room_number}: {details['status'].capitalize()} - {details['customer'] if details['customer'] else 'Available'}")

book_room("103", "Alexa")
checkout_customer("102")
display_room_status()

# Problem Two - Task Two
products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

def search_product(product_name):
    matching_products = []
    for product_id, details in products.items():
        if details["name"].lower() == product_name.lower():
            matching_products.append((product_id, details))
    return matching_products

search_result = search_product("laptop")
if search_result:
    print("Matching products found:")
    for product_id, details in search_result:
        print(f"Product ID: {product_id}, Name: {details['name']}, Category: {details['category']}, Price: ${details['price']}")
else:
    print("No matching products found.")




# Problem Three - Task One

class TicketTracker:
    def __init__(self):
        self.service_tickets = {}

    def open_ticket(self, ticket_id, customer, issue):
        if ticket_id in self.service_tickets:
            print("Ticket ID already exists. Please choose a different ID.")
        else:
            self.service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
            print("New ticket opened successfully.")

    def update_status(self, ticket_id, new_status):
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
        else:
            print("Ticket ID not found.")

    def display_tickets(self, status=None):
        if status:
            filtered_tickets = {ticket_id: ticket_info for ticket_id, ticket_info in self.service_tickets.items() if ticket_info["Status"] == status}
            if filtered_tickets:
                for ticket_id, ticket_info in filtered_tickets.items():
                    print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
            else:
                print("No tickets found with the specified status.")
        else:
            for ticket_id, ticket_info in self.service_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

tracker = TicketTracker()
tracker.service_tickets.update(service_tickets)
tracker.open_ticket("Ticket003", "Charlie", "Tech support needed")
tracker.update_status("Ticket001", "closed")
print("All tickets:")
tracker.display_tickets()

print("\nOpen tickets:")
tracker.display_tickets(status="open")




# Problem Four - Task One
# **** go over *****
import copy
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
weekly_sales_copy = copy.deepcopy(weekly_sales)
weekly_sales_copy["Week 2"]["Electronics"] = 18000

print("Original weekly_sales:")
print(weekly_sales)
print("\nCopied weekly_sales with updated Electronics sales for Week 2:")
print(weekly_sales_copy)


