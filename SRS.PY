qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:

    print("\n== MENU ==")
    print("1. Xem ton kho")
    print("2. Nhap kho")
    print("3. Xuat kho")
    print("4. Canh bao ton kho")
    print("5. Thoat")

    chon = input("Nhap lua chon: ")

    if chon == "1":

        print("\n== TON KHO ==")

        print("Laptop:", qty_laptop)
        print("Bieu do: ", end="")
        for i in range(qty_laptop):
            print("*", end="")
        print()

        print("Phone:", qty_phone)
        print("Bieu do: ", end="")
        for i in range(qty_phone):
            print("*", end="")
        print()

        print("Tablet:", qty_tablet)
        print("Bieu do: ", end="")
        for i in range(qty_tablet):
            print("*", end="")
        print()

    elif chon == "2":

        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        loai = input("Nhap loai hang: ")

        while True:

            soluong = int(input("Nhap so luong nhap: "))

            if soluong < 0:
                print("Khong duoc nhap so am")
                continue
            else:
                break

        if loai == "1":
            qty_laptop = qty_laptop + soluong
            print("Da nhap Laptop")

        elif loai == "2":
            qty_phone = qty_phone + soluong
            print("Da nhap Phone")

        elif loai == "3":
            qty_tablet = qty_tablet + soluong
            print("Da nhap Tablet")

        else:
            print("Loai hang khong hop le")

    elif chon == "3":

        print("\n1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        loai = input("Nhap loai hang: ")

        while True:

            soluong = int(input("Nhap so luong xuat: "))

            if soluong < 0:
                print("Khong duoc nhap so am")
                continue
            else:
                break

        if loai == "1":

            if soluong > qty_laptop:
                print("Khong du hang")
            else:
                qty_laptop = qty_laptop - soluong
                print("Xuat Laptop thanh cong")

        elif loai == "2":

            if soluong > qty_phone:
                print("Khong du hang")
            else:
                qty_phone = qty_phone - soluong
                print("Xuat Phone thanh cong")

        elif loai == "3":

            if soluong > qty_tablet:
                print("Khong du hang")
            else:
                qty_tablet = qty_tablet - soluong
                print("Xuat Tablet thanh cong")

        else:
            print("Loai hang khong hop le")

    elif chon == "4":

        print("\n== CANH BAO ==")

        if qty_laptop < 5:
            print("Laptop sap het")

        if qty_phone < 5:
            print("Phone sap het")

        if qty_tablet < 5:
            print("Tablet sap het")

    elif chon == "5":

        print("Tam biet")
        break

    else:
        print("Nhap sai menu")
