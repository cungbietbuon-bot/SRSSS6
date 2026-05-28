id="thss6"

sl1 = 0
sl2 = 0
sl3 = 0

while True:

    print("\n===== MENU =====")
    print("1 xem kho")
    print("2 nhap hang")
    print("3 xuat hang")
    print("4 canh bao")
    print("5 thoat")

    x = input("chon: ")

    if x == "1":

        print("\nLaptop:", sl1)
        print("Laptop: ", end="")
        for i in range(sl1):
            print("*", end="")
        print()

        print("Phone:", sl2)
        print("Phone: ", end="")
        for i in range(sl2):
            print("*", end="")
        print()

        print("Tablet:", sl3)
        print("Tablet: ", end="")
        for i in range(sl3):
            print("*", end="")
        print()

    elif x == "2":

        print("1 laptop")
        print("2 phone")
        print("3 tablet")

        loai = input("nhap loai: ")

        while True:

            n = int(input("so luong: "))

            if n < 0:
                print("nhap lai")
                continue
            else:
                break

        if loai == "1":
            sl1 = sl1 + n

        elif loai == "2":
            sl2 = sl2 + n

        elif loai == "3":
            sl3 = sl3 + n

        else:
            print("sai")

    elif x == "3":

        print("1 laptop")
        print("2 phone")
        print("3 tablet")

        loai = input("nhap loai: ")

        while True:

            n = int(input("so luong: "))

            if n < 0:
                print("nhap lai")
                continue
            else:
                break

        if loai == "1":

            if n > sl1:
                print("khong du hang")
            else:
                sl1 = sl1 - n

        elif loai == "2":

            if n > sl2:
                print("khong du hang")
            else:
                sl2 = sl2 - n

        elif loai == "3":

            if n > sl3:
                print("khong du hang")
            else:
                sl3 = sl3 - n

    elif x == "4":

        if sl1 < 10:
            print("Laptop sap het")

        if sl2 < 10:
            print("Phone sap het")

        if sl3 < 10:
            print("Tablet sap het")

    elif x == "5":
        print("bye")
        break

    else:
        print("chon sai")
