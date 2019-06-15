import random
import ipaddress

subnet = ipaddress.IPv4Network((random.getrandbits(32), random.randint(8, 30)), strict=False)
host = random.choice(list(subnet.hosts()))
print("Find the subnet ID, broadcast address and prefix length for the following")
print("IP address %s with mask %s" % (host, subnet.netmask))

user_id = input("Enter subnet id: ")
user_bcast = input("Enter broadcast address: ")
user_plength = input("Enter prefix length: ")
user_nhosts = subnet.num_addresses - 2
if (subnet.prefixlen > 15):
    user_nhosts = input("Enter tne number of usable addresses in the subnet: ")

flag_id = user_id == str(subnet.network_address)
flag_bcast = user_bcast == str(subnet.broadcast_address)
flag_plength = int(user_plength) == subnet.prefixlen
flag_nhosts = int(user_nhosts) == subnet.num_addresses - 2

if flag_id and flag_bcast and flag_plength and flag_nhosts:
    print("All the answers are correct! Good job!")
    exit(0)

if not flag_id:
    print("You made a mistake identifying subnet ID.\nYour answer was %s, "
          "while the correct is %s" % (user_id, str(subnet.network_address)))
if not flag_bcast:
    print("You made a mistake identifying broadcast address.\nYour answer was %s, "
          "while the correct is %s" % (user_bcast, str(subnet.broadcast_address)))
if not flag_plength:
    print("You made a mistake identifying prefix length.\nYour answer was %s, "
          "while the correct is %s" % (user_plength, subnet.prefixlen))
if not flag_nhosts:
    print("You made a mistake identifying the number of usable addresses in the subnet.\nYour answer was %s, "
          "while the correct is %s" % (user_nhosts, subnet.num_addresses - 2))
