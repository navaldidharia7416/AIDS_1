problem=["Over Heating","Battery dying quickly","System crash","viruses","Display not working","Other Problem"]
print("Hello I came from company services")
print("May I know yourname?")
name=input()
print("Thank you", name)
print("I am here to help you explore through your problem of laptop")
for i in range(0,6):
    print((i+1),".",problem[i])
print("Choose your problem")
num=input()
dict={
        "1":"Keep the Laptop on a Hard and Flat SurfaceMost laptops keep in cooling air through their bottoms.",
        "2":"Your battery drains much faster when it's hot, even when not in use.",
        "3":"Most PC or laptop crashes are the result of overheating, hardware faulty, corrupted system or driver corruption, etc.",
        "4":"A computer virus is a type of malware",
        "5":"check if your laptop's brightness level is set to maximum. If the display is still dim, try restarting the device.",
        "6":"Go to customer service tell their what is your problem."
    }
number=""
for i in num:
    number+=dict.get(i,"")+" "
print(number)
