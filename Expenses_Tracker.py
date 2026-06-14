expenses = []

while True:

    if len(expenses) == 0:
        print("\nNo expenses yet!!!")
    else:
        print(f"\n{'No.':<5} {'Category':<15} {'Amount':<10}")
        print("-" * 30)
        for i in range(len(expenses)):
            cat = expenses[i]["category"]
            amt = expenses[i]["amount"]
            print(f"{i+1:<5} {cat:<15} Rs.{amt:<10.2f}")

    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View total spent")
    print("3. View spending by category")
    print("4. Quit")

    
    choice = input("\nEnter choice (1/2/3/4): ")

    if choice not in ["1", "2", "3", "4"]:
         print("Invalid choice! Please enter 1, 2, 3 or 4. Try again.")
         continue  
    else :
         
             if choice == "1":
                 cat = input("Enter category (Food/Transport/Shopping/Other): ")
                 amt = float(input("Enter amount: Rs."))
                 expenses.append({"category": cat, "amount": amt})
                 print(f"Expense added! Rs.{amt} for {cat}.")

             elif choice == "2":
                 if len(expenses) == 0:
                     print("No expenses yet!")
                 else:
                     total = 0
                     for i in range(len(expenses)):
                         total += expenses[i]["amount"]
                     print(f"\nTotal spent: Rs.{total:.2f}")

             elif choice == "3":
                 if len(expenses) == 0:
                     print("No expenses yet!")
                 else:
                     category_totals = {}
                     for i in range(len(expenses)):
                         cat = expenses[i]["category"]
                         amt = expenses[i]["amount"]
                         if cat in category_totals:
                             category_totals[cat] += amt
                         else:
                             category_totals[cat] = amt
                     print("\n--- Spending by Category ---")
                     for cat in category_totals:
                         print(f"{cat:<15} Rs.{category_totals[cat]:>7.2f}")

             elif choice == "4":
                 print("Goodbye! Spend wisely!")
                 break
    
          
    
