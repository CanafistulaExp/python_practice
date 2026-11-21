def display_menu():
  contact_book = {}
  
  n = 0
  while n != 6:
    print("""Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit""")
    n = float(input().replace(',', "."))
    if n == 1:
      name = input()
      if name in contact_book:
        print("Contact already exists!")
      else:
        phone = input()
        email = input()
        address = input()
        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")
    

    elif n == 2:
      name = input()
      if name not in contact_book:
        print("Contact not found!")

      else:
        print(f"""Name: {name}
Phone: {contact_book[name]["phone"]}
Email: {contact_book[name]["email"]}
Address: {contact_book[name]["address"]}""")

    elif n == 3:
      name = input()
      if name in contact_book:
        phone = input()
        email = input()
        address = input()

        if phone == '':
          phone = contact_book[name]['phone']
        if email == '':
          email = contact_book[name]['email']
        if address == '':
          address = contact_book[name]['address']

        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
      else:
        print("Contact not found!")

    elif n == 4:
      name = input()
      if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
        
      else:
        print("Contact not found!")

    elif n == 5:
      if contact_book == {}:
        print("No contacts available.")
      else:
        for key, value in contact_book.items():
          phone = contact_book[key]["phone"]
          email = contact_book[key]["email"]
          address = contact_book[key]["address"]
          print(f"""Name: {key}
Phone: {phone}
Email: {email}
Address: {address}
""")

    elif n == 6:
      return contact_book
    else:
      print("Invalid choice. Please try again.")

return contact_book
    

display_menu()
