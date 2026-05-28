id="MNSS6"

lap = 0
ph = 0
tab = 0

while True:

    print("\n== MENU ==")
    print("1. xem ton kho")
    print("2. nhap kho")
    print("3. xuat kho")
    print("4. canh bao")
    print("5. thoat")

    a = input("nhap lua chon: ")

    # xem ton kho
    if a == "1":

        print("\n== TON KHO ==")

        print("Laptop (" + str(lap) + "): ", end="")
        for i in range(lap):
            print("*", end="")
        print()

        print("Phone (" + str(ph) + "): ", end="")
        for i in range(ph):
            print("*", end="")
        print()

        print("Tablet (" + str(tab) + "): ", end="")
        for i in range(tab):
            print("*", end="")
        print()

    # nhap kho
    elif a == "2":

        print("\n1 laptop")
        print("2 phone")
        print("3 tablet")

        loai = input("chon hang: ")

        while True:

            sl = int(input("nhap so luong: "))

            if sl < 0:
                print("So luong khong hop le, nhap lai")
                continue
            else:
                break

        if loai == "1":
            lap += sl
            print("da nhap laptop")

        elif loai == "2":
            ph += sl
            print("da nhap phone")

        elif loai == "3":
            tab += sl
            print("da nhap tablet")

        else:
            print("khong co mat hang nay")

    # xuat kho
    elif a == "3":

        print("\n1 laptop")
        print("2 phone")
        print("3 tablet")

        loai = input("chon hang: ")

        while True:

            sl = int(input("nhap so luong: "))

            if sl < 0:
                print("So luong khong hop le, nhap lai")
                continue
            else:
                break

        if loai == "1":

            if sl > lap:
                print("Khong du hang")
            else:
                lap -= sl
                print("xuat thanh cong")

        elif loai == "2":

            if sl > ph:
                print("Khong du hang")
            else:
                ph -= sl
                print("xuat thanh cong")

        elif loai == "3":

            if sl > tab:
                print("Khong du hang")
            else:
                tab -= sl
                print("xuat thanh cong")

        else:
            print("khong co mat hang nay")

    # canh bao
    elif a == "4":

        print("\n== CANH BAO ==")

        if lap < 10:
            print("[CANH BAO] Laptop sap het, con", lap)

        if ph < 10:
            print("[CANH BAO] Phone sap het, con", ph)

        if tab < 10:
            print("[CANH BAO] Tablet sap het, con", tab)

    # thoat
    elif a == "5":
        print("ket thuc chuong trinh")
        break

    else:
        print("chon sai roi")
