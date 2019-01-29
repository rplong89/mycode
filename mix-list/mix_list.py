#!/usr/bin/env python3
# Make a list to work with
my_list = [ "192.168.0.5", 5060, "UP" ]

# Print the first element in the list concatenated to a descriptive string.
print("The first item in the list (IP): " + my_list[0] )

# Print the second element, converted to a string, in the list concatenated to a descriptive string.
print("The second item in the list (port): " + str(my_list[1]) )

# Print the third element in the list concatenated to a descriptive string.
print("The last item in the list (state): " + my_list[2] )

# Create new list to work with
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# Add the missing text elements to the list
new_list.append(" or ")
new_list.append("I am unable to ping ports ")
new_list.append(", ")
new_list.append(".")
new_list.append("or ")

# Print sentence all concatenated together
print("When I ssh into IP addresses " + new_list[3] + new_list[6] + new_list[4] + new_list[8] + new_list[7] + str(new_list[0]) + new_list[8] + new_list[1] + new_list[8] + new_list[10] + str(new_list[2]) + new_list[9])
