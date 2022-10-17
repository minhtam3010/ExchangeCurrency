import math
def convert(num):
    dv = ("", "một ", "hai ", "ba ", "bốn ","năm ", "sáu ", "bảy ","tám ", "chín ")
    chuc =("", "mốt ", "hai ", "ba ", "bốn ", "lăm ","sáu ","bảy ","tám ","chín ")

    if num<10:
        return  dv[num]

    elif num<20:
        return "mười " + dv[int(num%10)]

    elif num<100:
        return dv[int(num/10)] + "mươi " + chuc[int(num%10)]

    elif num<1000:
        if (int((num // math.pow(10, (math.log10(num) + 1) // 2))) % 10)==0 and num%100!=0:
            return dv[int(num/100)] + "trăm linh " +convert(int(num%100)) 
                    
        else:
            return dv[int(num/100)] + "trăm " +convert(int(num%100)) 
    elif num<1000000:
        if (int((num // math.pow(10, (math.log10(num) + 1) // 2))) % 10)==0 and (int((num // math.pow(10, (math.log10(num) ) // 2))) % 10)!=0 and num%1000!=0:
            return  convert(num // 1000) + "ngàn không trăm " + convert(int(num % 1000))
        elif (int((num // math.pow(10, (math.log10(num) + 1) // 2))) % 10)==0  and num%1000!=0:
            return convert(num // 1000) + "ngàn không trăm linh" + convert(int(num % 1000))
        return  convert(num // 1000) + "ngàn " + convert(int(num % 1000))

    elif num < 1000000000:    
        return convert(num // 1000000) + "triệu " + convert(int(num % 1000000))
    return convert(num // 1000000000)+ "tỷ "+ convert(int(num % 1000000000))

if __name__ == "__main__":
    n=input(" Nhập số tiền bạn muốn rút: ")
    print(" Số tiền bạn rút được:")
    print(" " +n+" VND")
    x=(int(n.replace(",","" )))
    print(convert(n)+"đồng")
