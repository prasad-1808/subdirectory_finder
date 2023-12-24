import argparse

def main():

    parser = argparse.ArgumentParser(description="For getting input target and output file")
    parser.add_argument("-t", "--target", required=True, help="Input file containing target URLs")
    parser.add_argument("-o", "--output", required=True, help="Output file to write subdirectories")

    Duplicated_lst=[]

    args = parser.parse_args()
    input_file_path = args.target.strip()
    output_file_path = args.output.strip()

    target_lst = []

    with open(input_file_path, "r") as file:
        target_lst = file.readlines()

    with open(output_file_path, "w") as output_file:
        for i in target_lst:
            output_file.write("Sub directory list for " + i + "\n")
            l1 = i.split("/")
            dum_lst = []

            for j in l1:
                if j != '' and ".com" not in j and j != "https:":
                    dum_lst.append(j)
            domain = l1[0] + "//" + l1[2]

            s = domain
            Duplicated_lst.append(s)
            output_file.write(s + "\n")
            for i in dum_lst:
                s += "/" + i
                output_file.write(s + "\n")
                Duplicated_lst.append(s)

            output_file.write("----------------------------------------------------------------------------------------------------------------\n")


    # print(*Duplicated_lst,sep="\n")

    Non_duplicated_lst=sorted(list(set(Duplicated_lst)))
    with open(output_file_path, "a") as output_file:
        output_file.write("\n\n\nThe Non duplicated list: \n")
        for i in Non_duplicated_lst:
            if i!="" and i!="\n":
                output_file.write(i+"\n")

if __name__ == "__main__":
    main()


