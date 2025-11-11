# 🏫 School Fee Management System

students = []  # List to store [name, class, fee_status]

while True:
    print("\n====== School Fee Management System ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Fee Status")
    print("4. Show Students Who Haven't Paid")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        student_class = input("Enter class: ")
        fee_status = input("Has the fee been paid? (yes/no): ").lower()
        students.append([name, student_class, fee_status])
        print("✅ Student added successfully!")

    elif choice == 2:
        print("\n--- All Students ---")
        if len(students) == 0:
            print("No student record found.")
        else:
            for s in students:
                print("Name:", s[0], "| Class:", s[1], "| Fee Paid:", s[2])

    elif choice == 3:
        name = input("Enter student name to update: ")
        found = False
        for s in students:
            if s[0].lower() == name.lower():
                s[2] = input("Enter new fee status (yes/no): ").lower()
                print("✅ Fee status updated!")
                found = True
                break
        if not found:
            print("❌ Student not found.")

    elif choice == 4:
        print("\n--- Students Who Haven't Paid ---")
        unpaid_found = False
        for s in students:
            if s[2] == "no":
                print("Name:", s[0], "| Class:", s[1])
                unpaid_found = True
        if not unpaid_found:
            print("🎉 All students have paid their fees!")

    elif choice == 5:
        print("👋 Exiting program... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")







# 🏨 Hotel Room Booking System

rooms = [101, 102, 103, 104, 105]   # Available room numbers
booked_rooms = []                   # Booked rooms list

while True:
    print("\n====== HOTEL ROOM BOOKING SYSTEM ======")
    print("1. Show Available Rooms")
    print("2. Book a Room")
    print("3. Cancel Booking")
    print("4. Show All Bookings")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Available Rooms ---")
        if len(rooms) == 0:
            print("❌ No rooms available.")
        else:
            for r in rooms:
                print("Room:", r)

    elif choice == 2:
        print("\n--- Book a Room ---")
        if len(rooms) == 0:
            print("❌ All rooms are booked.")
        else:
            name = input("Enter guest name: ")
            print("Available rooms:", rooms)
            room_no = int(input("Enter room number to book: "))

            if room_no in rooms:
                rooms.remove(room_no)
                booked_rooms.append([name, room_no])
                print(f"✅ Room {room_no} booked successfully for {name}!")
            else:
                print("❌ Room not available or already booked.")

    elif choice == 3:
        print("\n--- Cancel Booking ---")
        name = input("Enter guest name to cancel booking: ")
        found = False
        for b in booked_rooms:
            if b[0].lower() == name.lower():
                booked_rooms.remove(b)
                rooms.append(b[1])
                print(f"✅ Booking cancelled for {name}. Room {b[1]} is now available.")
                found = True
                break
        if not found:
            print("❌ No booking found for that name.")

    elif choice == 4:
        print("\n--- All Bookings ---")
        if len(booked_rooms) == 0:
            print("No bookings yet.")
        else:
            for b in booked_rooms:
                print(f"Guest: {b[0]} | Room: {b[1]}")

    elif choice == 5:
        print("👋 Exiting program... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
