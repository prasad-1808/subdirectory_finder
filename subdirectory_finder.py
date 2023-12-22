import argparse

parser=argparse.ArgumentParser(description="For getting input target")
parser.add_argument("-t","--target",required=True,help="Target URL")

args=parser.parse_args()
target=args.target.strip()

target_lst=[]

with open("input.txt","r") as file:
    target_lst=file.readlines()

# print(*target_lst)
print("\n\n\n\n\n\n\n\n")
for i in target_lst:
    print("Sub directory list for "+i+"\n")
    l1=i.split("/")
    dum_lst=[]

    for j in l1:
        if j != '' and ".com" not in j and j != "https:":
            dum_lst.append(j)
    domain=l1[0]+"//"+l1[2]

    s=domain
    for i in dum_lst:
        s+="/"+i
        print(s)

    print("----------------------------------------------------------------------------------------------------------------")


# l1 = target.split("/")
# dum_lst = []

# for j in l1:
#     if j != '' and ".com" not in j and j != "https:":
#         dum_lst.append(j)

# domain = l1[0] + "//" + l1[2]

# s = domain
# print(s)
# for i in dum_lst:
#     s += "/" + i
#     print(s)
