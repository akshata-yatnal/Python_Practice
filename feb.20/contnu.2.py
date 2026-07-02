cart=[10,20,30,600,700,800,70,90]
for item in cart:
    if item>700:
        print("to place order insurence must required,we cant provide")
        continue
    print("processing item:",item)
