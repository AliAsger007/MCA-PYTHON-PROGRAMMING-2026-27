p1 = float(input("Enter price of product 1: "))
q1 = int(input("Enter quantity of product 1: "))
p2 = float(input("Enter price of product 2: "))
q2 = int(input("Enter quantity of product 2: "))
p3 = float(input("Enter price of product 3: "))
q3 = int(input("Enter quantity of product 3: "))

subtotal = p1*q1 + p2*q2 + p3*q3
discount = subtotal * 0.10
amount = subtotal - discount
gst = amount * 0.18
final = amount + gst

print("Subtotal:", subtotal)
print("Discount:", discount)
print("GST:", gst)
print("Final Amount:", final)
