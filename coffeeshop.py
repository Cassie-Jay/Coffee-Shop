small = 2
med=3
large=4 
espresso= 0.50
cold_brew= 1

size=input("What size cup do you want?   ")
coffee=input("What type of coffee do you want? Brewed, Espresso, or cold brew  " )
flavor=input("Do you want a flavored syrup? yes or no    " )



if size == "small" and coffee == 'espresso':
    total= (int(small)) + (float(espresso)) 
elif size == "small" and coffee =="brewed":
    total =(float(small))
elif size == "small" and coffee == "cold brew":
    total = (float(small)) + (float(cold_brew))
elif size =="medium" and coffee == 'espresso':
    total= (float(med))+(float(espresso))
elif size == "medium" and coffee== "cold brew":
    total= (float(med))+ (float(cold_brew))
elif size == "medium" and coffee =="brewed":
    total=(float(med))
elif size =="large" and coffee == 'espresso':
    total=(float(large)) + (float(espresso))
elif size =="large" and coffee == "cold brew":
    total=(float(large)) + float((cold_brew))
elif size == "large" and coffee =="brewed":
    total=(float(large))
    

if flavor == "yes":
    flavoring=input("What type of flavoring? Hazelnut, Vanilla or Caramel.")
    total=total +0.50
    
else:
    total=total
    
tip= total *1.15

print("You asked for a",size,"cup of",coffee,"coffee with",flavor,"syrup.")
print("Your cup of coffee costs $",total,".")
print("Your price with a tip is $",(round(tip,2)),".")