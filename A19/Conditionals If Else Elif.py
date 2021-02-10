
is_cold = True
is_raining = False

if is_raining and is_cold:
    print("Bring umbrella or jacket or both")
elif is_raining and not(is_cold):
    print("Bring umbrella")
elif not(is_raining) and is_cold:
    print("Bring umbrella")
else:
    print("Shirt is fine!")

# Another example


amount = 51
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your pin")