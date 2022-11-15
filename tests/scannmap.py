import nmap

scanner = nmap.PortScanner()
ip_addr = input("Adresse IP à scanner : ")

scanner.scan(ip_addr,'1-1024', '-v -sT') # équivalent de "nmap [ip] -p 1-1024 -v -sT"
print(scanner.scaninfo())
scanfinished = True