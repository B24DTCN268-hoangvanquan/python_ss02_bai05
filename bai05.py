name_patient = input("Nhập tên bệnh nhân: ")
age = int(input("Nhập tuổi bệnh nhân: "))
blood_oxygen = int(input("Nhập nồng độ Oxy trong máu: "))
heart_rate = int(input("Nhập nhịp tim: "))
health_ins = input("Có thể BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): ")

if health_ins == "yes" or health_ins == "no":
    if (blood_oxygen > 0 and blood_oxygen < 90) or (heart_rate > 120):
        print("Báo động ĐỎ (Cấp cứu khẩn)")
    elif (blood_oxygen > 90 and blood_oxygen < 95) or (heart_rate > 100 and heart_rate < 120):
        print("Báo động VÀNG (Theo dõi sát)")
    else:
        print("XANH (Khám thường)")

    if (age > 0 and age < 6) or age > 80:
        print("Miễn phí (0 VND)")
    elif health_ins == "Yes":
        print("Giảm 50% (250000 VND)")
    else:
        print("Thu 100% (500000 VND)")
else:
    print("Lỗi không hợp lệ!")