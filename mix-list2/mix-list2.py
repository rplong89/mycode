#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']

# Add my new list
# my_proto = []

print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protoa)

# Make a copy of the list to fiddle with
my_proto = proto.copy()
print(my_proto)

# Add some duplicate data and display it
my_proto.extend(proto)
print("Before Trim")
print(my_proto)

# I just don't like dns
for banana in range(my_proto.count('dns')):
	my_proto.remove('dns')

# Print adjusted list
print("After Trim")
print(my_proto)

# Print the number of occurences of https (have to make count a string!
print("The number of occurences of https in the list is now: " + str(my_proto.count("http")) )

# Print the number of occurences of dns (have to make count a string!
print("The number of occurences of dns in the list is now: " + str(my_proto.count("dns")) )