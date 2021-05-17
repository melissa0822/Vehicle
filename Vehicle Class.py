#Vehicle class defination
class Vehicle:
    #constructor to initilizes value
    def __init__(self,make,model,color,fuelType,options):
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options= options
    #getter method
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getColor(self):
        return self.color
    def getFuelType(self):
        return self.fuelType
    def getOptions(self):
        return self.options
#Car class that is child class of Vehicle
class Car(Vehicle):
    #constructor to initilizes value
    def __init__(self,make,model,color,fuelType,options,engineSize,numDoors):
        Vehicle.__init__(self,make,model,color,fuelType,options)#calling super class constructor
        self.engineSize=engineSize
        self.numDoors=numDoors
    #getter method
    def getEngineSize(self):
        return self.engineSize
    def numDoors(self):
        return self.numDoors
    #print details method to print data
    
    def printDetails(self):
        dct_car={
        "car Make : ":self.make,
        "car model : ":self.model,
        "car Color : ":self.color,
        "car Fuel Type : ":self.fuelType,
        "car Options : ":self.options,
        "Car Engine Size : ":self.engineSize,
        "Car Number of Doors :":self.numDoors,
        }
        return dct_car
#Pickup class that is child class of Vehicle
class Pickup(Vehicle):
    #constructor to initilizes value
    def __init__(self,make,model,color,fuelType,options,cabStyle,bedLength):
        Vehicle.__init__(self,make,model,color,fuelType,options)#calling super class constructor
        self.cabStyle=cabStyle
        self.bedLength=bedLength
        #getter method
    def getCabStyle(self):
        return self.cabStyle
    def getBedLength(self):
        return self.bedLength
    #print details method to print data
    def printDetails(self):
        dct_pickup={
        "Pickup Make : ":self.make,
        "Pickup model : ":self.model,
        "Pickup Color : ":self.color,
        "Pickup Fuel Type : ":self.fuelType,
        "Pickup Options : ":self.options,
        "Pickup Cab Style : ":self.cabStyle,
        "Pickup Bed Length :":self.bedLength,
        }
        return dct_pickup

        
def vehicle_menu(option,garage):
    if(option==1):# if 1 Car data is to be add
        make=input("Enter Car Make : ")
        model=input("Enter Car Model : ")
        color=input("Enter Car Color : ")
        fuelType=input("Enter Car Fuel type : ")
        options=input("Enter Car option seprated by space : ")
        engineSize=int(input("Enter Car Engine Size : "))
        numDoors=int(input("Enter Car Number of Doors : "))
        p=Car(make,model,color,fuelType,options,engineSize,numDoors)#creating car object
        garage.append(p)#adding car object to garage list
        return True,garage

    elif(option==2):# if 2 pickup data is to be enter
        make=input("Enter Pickup Make : ")
        model=input("Enter Pickup Model : ")
        color=input("Enter Pickup Color : ")
        fuelType=input("Enter Pickup Fuel type : ")
        options=input("Enter Pickup option seprated by space : ")
        cabStyle=input("Enter Pickup Cab Style : ")
        bedLength=int(input("Enter Pickup bed length : "))
        t=Pickup(make,model,color,fuelType,options,cabStyle,bedLength)# creating pickup object
        garage.append(t)#adding pick up object to garage list
        return True,garage
    else:# if other option is enter then exit
        return False,garage

garage=[]# list to hold Vehicle objects
make_vehicle=True
while(make_vehicle):# loop that will takes user input
    option = int(input("Enter \n1 for Car \n2 for Pickup \n3 for exit \n")) #option from which user can choose
    make_vehicle,garage=vehicle_menu(option,garage)
#printing vehicle details
print("Vehicles Details is :")
print("----------------------------")
for v in garage:
    details=v.printDetails()#calling printDetails method
    for key,value in details.items():
        print (key,value)
