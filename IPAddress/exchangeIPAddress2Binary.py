def decode(ipAddress):
    extractIP = ipAddress.split(".")
    finalIP = []
    while len(extractIP) != 0:
        firstIP = int(extractIP[0])
        res = ""
        bits = [128, 64, 32, 16, 8, 4, 2, 1]
        while len(bits) != 0:
            if bits[0] <= firstIP:
                firstIP -= bits[0]
                res += "1"
                bits.pop(0)
            else:  
                bits.pop(0)
                res += "0"
        finalIP.append(res)
        extractIP.pop(0)
    return ".".join(finalIP)
    
def main():
    ipAddress = "192.168.1.21"
    res = decode(ipAddress)
    print(res)

if __name__ == "__main__":
    main()