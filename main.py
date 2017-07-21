def LoadPickle():
    import pickle
    f = open("pickle-data", "rb")
    return_data = pickle.load(f)
    f.close()
    return return_data

def SavePickle(to_do_list):
    import pickle
    f = open("pickle-data","wb")
    pickle.dump(to_do_list,f)
    f.close()

def RemoveIndex(to_do_list):
    for list_num in range(0,len(to_do_list)):
        print("{}. {}".format(list_num,to_do_list[list_num]))
    input_number = input("Enter the number to delete or Exit to leave.")
    if input_number == "Exit":
        return to_do_list
    elif int(input_number) > len(to_do_list):
        print("Number too high")
        return to_do_list
    else:
        del to_do_list[int(input_number)]
        return to_do_list

def main():
    from pathlib import Path
    to_do_list = []
    my_file = Path("pickle-data")
    if my_file.is_file():
        to_do_list = LoadPickle()
    exit_time = False
    while not exit_time:
        prompt = input("Please enter what to do. Read/Write/Remove/Exit\n")
        if prompt == "Read":
            if my_file.is_file():
                to_do_list = LoadPickle()
                for line in to_do_list:
                    print("{}".format(line))
            else:
                print("No data in file.")
        elif prompt == "Write":
            to_do_list.append(input("Please enter to do: \n"))
            SavePickle(to_do_list)
        elif prompt == "Remove":
            to_do_list = RemoveIndex(to_do_list)
            SavePickle(to_do_list)
        elif prompt == "Exit":
            exit_time = True


if __name__=="__main__":
    main()