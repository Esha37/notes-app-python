print("Notes App")

while True:
    print("\nMenu:")
    print("1. Add note:")
    print("2. View Notes:")
    print("3. Exit")

    choice=input("Enter your Choice:")
    if choice == "1":
      note=input("Enter your note:")

      with open("notes_app.txt", "a") as file:
       file.write(note + "\n")
      print("Note saved successfully")
    
    elif choice == "2":
     try:
        with open("notes_app.txt", "r") as file:
         content = file.read()

        if content == "" :
         print("Notes not found.")
        else:
          print("All Notes:")
          print(content)
     except FileNotFoundError:
          print("No notes found")

    elif choice == "3":
          print("Goodbye")
          break

else:
 print("Invalid choice")