# # Định nghĩa cách đọc
# SoTuNhien = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
# DonVi = ['mươi', 'mốt','hai', 'ba', 'bốn', 'lăm', 'sáu', 'bảy', 'tám', 'chín']
# Chuc = ['linh', 'mười','hai', 'ba', 'bốn', 'lăm', 'sáu', 'bảy', 'tám', 'chín']
# Lop = ['tỷ', 'triệu', 'nghìn']
# Cum = ['trăm', 'chục', 'đơn vị']

# # group 3 số thành 1 lớp dưới
# def nhomCum3So(so):
#     chieudai_so = len(so)
#     # sodu>0: tức là cụm đầu tiên không chứa đủ 3 số
#     # songuyen: số cụm chứa đủ 3 số ['trăm', 'chục', 'đơn vị']
#     sodu, songuyen = chieudai_so % len(Cum), chieudai_so//len(Cum)
    
#     # Nhóm 3 số thành 1 lớp dưới
#     list_CumLe = so[:sodu]
#     list_CumChan = so[sodu:]
    
#     list_Cum3So = []
#     if list_CumLe != "":
#         list_Cum3So = [list_CumLe]    

#     begin = 0
#     end = begin +3
#     for _ in range(songuyen):                          
#         list_Cum3So.append(list_CumChan[begin:end])
#         begin = end 
#         end = begin +3
#     return list_Cum3So

# # "Thêm tiền tố lớp cho mỗi cụm (cấu trúc tiền tố hình: cautruc_lop,cum_code_docso.png)";
# def themTienTo_Lop(list_Cum3So):   
#     so_label = len(list_Cum3So)
#     # so_label = tongso_cum - 1 # tính số nhãn tiền tố (trừ lớp đầu tiên không gán nhãn)   
    
#     soLop = len(Lop)
#     list_TienTo = []
#     if so_label==1: # Trường hợp <1000, ko thêm tiền tố
#         return list_TienTo, list_Cum3So
#     elif so_label>1 and so_label <= soLop: # Trường hợp <1tỷ, ko thêm tiền tố
#         list_TienTo = [*Lop[-so_label+1:]]
#     else: #Trường hợp >1tỷ
#         "Nguyên tắc thêm vào ptử cuối của list";
#         id_Lop =-1 # id_Lop = [-3,-2,-1]
#         sochu_ty = 0
#         for i_label in range(so_label):
#             if id_Lop < (-soLop): 
#                 id_Lop =-1 # Nếu vượt qua soLop thì gám lại =-1

#                 # thêm vào vị trí đầu tiên
#                 list_TienTo.insert(0, Lop[id_Lop])
                
#                 # tăng id_Lop
#                 id_Lop -= 1

#             elif i_label !=0:
#                 # thêm vào vị trí đầu tiên
#                 list_TienTo.insert(0, Lop[id_Lop])
                
#                 # Giảm id_Lop
#                 id_Lop -= 1

#                 # Thêm chữ tỷ:
#                 if list_TienTo[0] == Lop[0]: # Lop[0] = "tỷ"
#                     list_TienTo[0] += (" "+Lop[0])*sochu_ty                     
#                     sochu_ty += 1 
#     return list_TienTo, list_Cum3So

# # " Định nghĩa: 1 lớp gồm 3 cụm, 1 cụm chứa 3 số ";
# # Phân tách số theo lớp
# def phanCum_themTienTo (so):
#     # Nhóm 3 số thành 1 cụm: 
#     # list_Cum3So: đầy đủ các số, list_CumLe (chứa tối đa 2 số), chứa đúng 3 số
#     list_Cum3So = nhomCum3So(so)
#     list_TienTo, list_Cum3So = themTienTo_Lop(list_Cum3So)
#     return list_TienTo, list_Cum3So
    
# # Đọc số có 2 chữ số
# def docSoChuc(so2ChuSo):
    
#     if so2ChuSo[0] == "0":
#         return "linh" +" "+ SoTuNhien[int(so2ChuSo[1])]
#     elif so2ChuSo[0] == "1": # Hàng chục là số 1        
#         # Xét các số hàng đơn vị
#         if so2ChuSo[1] == "0":
#             return Chuc[1] # Số 10
#         elif so2ChuSo[1] == "1":
#             return Chuc[1] + " "+ SoTuNhien[1]# Số 11
#         else:
#             return Chuc[1] + " " +DonVi[int(so2ChuSo[1])]   

#     # Các trường hợp còn lại:    
#     else:
#         if DonVi[0] == DonVi[int(so2ChuSo[1])]:
#             return SoTuNhien[int(so2ChuSo[0])] +" " + DonVi[int(so2ChuSo[1])] 
#         # Xử lý chữ Ba mươi mươi                      
#         else:
#             return SoTuNhien[int(so2ChuSo[0])] +" " + DonVi[0] +" "+ DonVi[int(so2ChuSo[1])]

# # Đọc số có 3 chữ số:
# def docSoTram(so):
    
#     if so[1:] == "00":
#         return SoTuNhien[int(so[0])]+" " +Cum[0]
#     else:
#         return SoTuNhien[int(so[0])]+" " +Cum[0]+" "+docSoChuc(so[1:])

# # Tách số trong chuỗi lớp dưới:
# def docso_TungCum(so):
#     # ketQuaDocLopDuoi =[]
#     chieudai_so = len(so)
#     if chieudai_so == 1:
#         return SoTuNhien[int(so)]
#     elif chieudai_so == 2:
#         return docSoChuc(so)
#     else:        
#         return docSoTram(so)

# # Đọc các lớp từ hàng trăm về đơn vị trong cụm
# def doc_Cum3so(list_cum3So):
#     kq_DocSo =[]
#     # Đọc các số theo từng lớp
#     for lop in list_cum3So:
#         if lop != "":
#             kq_DocSo.append(docso_TungCum(lop))
#     return kq_DocSo        

# # Ghép lớp:
# def ghepCacLop(list_TienTo, ketqua_DocCum):
#     ketQuaDocSo = ''  
#     if list_TienTo == []:
#         ketQuaDocSo = ketqua_DocCum[0]
#     elif list_TienTo != []:
#         for i_cum in range(len(ketqua_DocCum)):
#             if i_cum < len(list_TienTo):
#                 ketQuaDocSo += (ketqua_DocCum[i_cum] + " " +list_TienTo[i_cum] + " ")                
#             else: ketQuaDocSo +=  ketqua_DocCum[i_cum]
#     else:
#         # Số chỉ nằm ở hàng trăm trở lại (cụm đầu tiên)
#         ketQuaDocSo += ketqua_DocCum[0]
       
#     # Viết hoa chữ đầu chuỗi
#     ketQuaDocSo = ketQuaDocSo.capitalize()
#     return ketQuaDocSo

# # Đọc số
# def docso(so):    
#     # Phân lớp theo cụm 3 số:
#     list_TienTo, list_Cum3So = phanCum_themTienTo(so)
    
#     # Đọc số từng cụm 1 
#     ketqua_DocCum = doc_Cum3so(list_Cum3So)

#     # Ghép các lớp
#     ketQuaDocSo = ghepCacLop(list_TienTo, ketqua_DocCum)   
    
#     return ketQuaDocSo
    
# # Test hàm đọc các số:
# so = []
# n = input('Nhập vào số tiền muốn rút: ')
# so.append(n)
# for i in range(len(so)):
#     so[i] = str(so[i])
#     print(f'Số tiền bạn rút là: {docso(so[i])} đồng')


a = "121,000"
unit = {4: "tỷ", 3: "triệu", 2: "nghìn"}
digit = {"0": "không", "1": "một", "2": "hai"}
split_a = a.split(",")
print(split_a)

# donvi = unit[len(split_a)]
# print(donvi)

res = ""
for i in range(len(split_a)):
    if len(split_a[i]) == 1:
        res += digit[i[0]]
        continue
    if i == 1:
        break
    for d in range(len(split_a[i])):
        if len(split_a[i]) == 3 and d == 0:
            res += digit[split_a[i][d]] + " trăm "
        elif len(split_a[i]) == 2 and split_a[i][d] != "1":
            res += digit[split_a[i][d]]
        elif d == 2:
            res += "mốt "
        else:
            res += digit[split_a[i][d]] + " "
        
    res += unit[len(split_a)]
print(res)