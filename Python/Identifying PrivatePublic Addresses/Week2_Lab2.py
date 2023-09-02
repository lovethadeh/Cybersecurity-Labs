# fill your information here
stud_id = "1153017"
stud_name = "LOVETH LUMUMBA ADEH" 
stud_Lab = "Lab 2"
stud_date = "SUMMER 2023"
# =======================================


# STEP 1
def repeat_string(word:str, num:int):
    """
    Method should receive a string and an integer. 
    the method returns a string that has the enterd string repeated the 
    number entered. Put a space between the repeated string. See examples below:
    
    >>>repeat_string("London", 3)
    London London London  
    
    >>>repeat_string("Hello", 5)
    Hello Hello Hello Hello Hello
    
    Notice the space between the words
    
    """
repeat_string("London", 3)
print (repeat_string)

 

# STEP 2
def number_of_cents(change:float): # if entered an integer, ex 20, it will be converted to float, ex 20.00
    """
    Takes in a dollar value including cents and returns the cents in the value entered 
    
    >>> number_of_cents(1.25)
    25
    >>> number_of_cents(20)
    0
    >>> number_of_cents(134.02)
    2
    """

    pass

# STEP 3
def max_of_min(num1, num2, num3, num4):
    
    '''
    Method receives 4 numbers. 
    Takes the firsts two(2) and returns minimum. 
    Takes the second two(2) and returns their minimum. 
    takes both minimum numbers and returns maximum.
    could use min() and max() functions 
    
    Examples:
    
    >>>max_of_min(35, 5.1, 7, 6)
    6
    
    >>>max_of_min(35, 5.1, 5, 6)
    5.1
    '''
    pass





# STEP 4
def ip_class(ip:str):
    '''
    IP Addresses for this LAB 2 do not need to be validated
    
    Function takes in a ip address in string format. 
    Returns which class the IP address belongs too. 
    IP address 8.8.8.8 is Class A
    
    print which class the IP address belongs to
    First Octet:
    class A: 1 to 126
    loopback:127
    clsss B: 128 to 191
    class C: 192 to 223
    
    Think how you can split a string. 
    '''
    
    pass


# STEP 5
def private_IP_address(ip):
    """
    Function takes in a ip address in string format. 
    Returns Private or Public for IP address given. 
    
    private IP address are  
    Private class A is in range 10.0.0.0 through 10.255.255.255
    Private class B is in range 172.16.0.0 through 172.31.255.255
    Private class C is in range 192.168.0.0 through 192.168.255.255
    all other IP Address are public
    
    Think how you can split a string. 
    
    """
    pass


 
#Testing repeat_string method not marked
print("Author: {0} ID: {1} \n".format(stud_name, stud_id))  
print("Testing repeat_string: \n") 
print("Testing 'London' and 3:\n", repeat_string("London", 3))
print("Testing 'Hello' and 5:\n", repeat_string("Hello", 5))

#create another test of your own ( MARKED )
print("\n---------------------------------------------------------\n")


#Testing max_of_min ( not MARKED )
print("Author: {0} ID: {1}\n".format(stud_name, stud_id)) 
print("Testing max_of_min: \n") 
print("Testing, group 1: 35 & 5.1 amd group 2: 7 & 6. Results: ", max_of_min(35, 5.1, 7, 6))
print("Testing, group 1: 5.1 & 6amd group 2: 25 & 5.11 Results: ", max_of_min(5.1,6, 25, 5.11))

#create another test of your own  ( MARKED )

print("\n---------------------------------------------------------\n")

print("Author: {0} ID: {1}\n".format(stud_name, stud_id)) 
print("testing results: \n") 
print("Testing 1.25 Results: ", number_of_cents(1.25))
print("Testing 20 Results: ", number_of_cents(20))
print("Testing 134.02 Results: ", number_of_cents(134.02))

#create another test of your own ( MARKED )

print("\n---------------------------------------------------------\n")

print("Author: {0} ID: {1}\n".format(stud_name, stud_id)) 
print("testing ip_class: \n") 
print("10.25.0.1 is", ip_class("10.25.0.1"))
print("127.25.0.1 is", ip_class("127.25.0.1"))
print("128.25.0.1 is",ip_class("128.25.0.1"))
print("192.32.1.1 is",ip_class("192.32.1.1"))
print("8.8.8.8 is",ip_class("8.8.8.8"))


#create another test of your own
print("\n---------------------------------------------------------\n")

print("Author: {0} ID: {1}\n".format(stud_name, stud_id)) 
print("testing private_ip_class: \n") 
print("130.25.0.1 is:", private_IP_address("130.25.0.1"))
print("172.25.0.1 is:", private_IP_address("172.25.0.1"))
print("192.25.0.1 is:", private_IP_address("192.25.0.1"))
print("192.168.0.1 is:", private_IP_address("192.168.0.1"))
print("8.8.8.8 is:", private_IP_address("8.8.8.8"))
print("10.25.0.1 is:", private_IP_address("10.25.0.1"))

#create another test of your own
