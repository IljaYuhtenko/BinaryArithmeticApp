import random
import ipaddress


def task1():
    subnet = ipaddress.IPv4Network((random.getrandbits(32), random.randint(8, 30)), strict=False)
    host = random.choice(list(subnet.hosts()))
    print("Find the subnet ID, broadcast address and prefix length for the following")
    print("IP address %s/%s" % (host, subnet.prefixlen))

    user_id = input("Enter subnet id: ")
    user_bcast = input("Enter broadcast address: ")
    user_nmask = input("Enter netmask using DDN: ")
    user_nhosts = subnet.num_addresses - 2
    if (subnet.prefixlen > 15):
        user_nhosts = input("Enter tne number of usable addresses in the subnet: ")

    flag_id = user_id == str(subnet.network_address)
    flag_bcast = user_bcast == str(subnet.broadcast_address)
    flag_nmask = user_nmask == str(subnet.netmask)
    flag_nhosts = int(user_nhosts) == subnet.num_addresses - 2

    if flag_id and flag_bcast and flag_nmask and flag_nhosts:
        print("All the answers are correct! Good job!")
        exit(0)

    if not flag_id:
        print("You made a mistake identifying subnet ID.\nYour answer was %s, "
              "while the correct is %s" % (user_id, str(subnet.network_address)))
    if not flag_bcast:
        print("You made a mistake identifying broadcast address.\nYour answer was %s, "
              "while the correct is %s" % (user_bcast, str(subnet.broadcast_address)))
    if not flag_nmask:
        print("You made a mistake identifying netmask.\nYour answer was %s, "
              "while the correct is %s" % (user_nmask, subnet.netmask))
    if not flag_nhosts:
        print("You made a mistake identifying the number of usable addresses in the subnet.\nYour answer was %s, "
              "while the correct is %s" % (user_nhosts, subnet.num_addresses - 2))


def task2():
    subnet = ipaddress.IPv4Network((random.getrandbits(32), random.randint(8, 24)), strict=False)
    hosts = random.choices(list(subnet.hosts()), k=4)
    subnets = [ipaddress.IPv4Network((str(host), random.randint(subnet.prefixlen, 30)), strict=False) for host in hosts]

    flag_no_overlap = True
    flags = [[0 for i in range(len(subnets))] for j in range(len(subnets))]
    user_flags = [[1 for i in range(len(subnets))] for j in range(len(subnets))]
    for i in range(len(subnets) - 1):
        for j in range(i + 1, len(subnets)):
            overlap = subnets[i].overlaps(subnets[j])
            flags[i][j] = overlap
            flags[j][i] = overlap
            user_flags[i][j] = not overlap
            user_flags[j][i] = not overlap
            if overlap:
                flag_no_overlap = False

    print("There are four different subnets:")
    for i in range(len(subnets)):
        print('%d. %s\%s' % (i + 1, subnets[i].network_address, subnets[i].prefixlen))
    print("Define, whether they do not overlap (N), or enter numbers of overlapping subnets like so, 1-2 or 2-1. "
          "Enter X, when you finish")
    user_is_right = False

    while True:
        user_in = input()
        if user_in == 'X':
            break
        if user_in == 'N':
            if flag_no_overlap:
                user_is_right = True
            break
        user_in = user_in.split('-')
        i = int(user_in[0]) - 1
        j = int(user_in[1]) - 1
        user_flags[i][j] = 1 - user_flags[i][j]
        user_flags[j][i] = 1 - user_flags[j][i]

    flag_any_wrong = False
    for i in range(len(subnets)):
        for j in range(len(subnets)):
            if not user_flags[i][j]:
                flag_any_wrong = True
                break
        if flag_any_wrong:
            break

    if flag_any_wrong:
        print("Actually,")
        for i in range(len(subnets) - 1):
            for j in range(i + 1, len(subnets)):
                if flags[i][j]:
                    print("Subnet %s overlaps with subnet %s" % (i + 1, j + 1))
        exit(1)
    else:
        user_is_right = True

    if user_is_right:
        print("You are right! Good job!")
        exit(0)


task1()
