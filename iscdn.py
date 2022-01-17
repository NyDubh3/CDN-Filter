import json
import ipaddress


def load_json(path):
    with open(path) as fp:
        return json.load(fp)


cdn_ip_cidr = load_json('cdn_ip_cidr.json')

def check_cdn_cidr(ips):
    if isinstance(ips, str):
        ips = set(ips.split(','))
    else:
        return False
    for ip in ips:
        try:
            ip = ipaddress.ip_address(ip)
        except Exception as e:
            print(e)
            return False
        for cidr in cdn_ip_cidr:
            if ip in ipaddress.ip_network(cidr):
                return True


def do_check():
    all = 0
    nocdnip = 0
    file = open("ip.txt")
    print("以下为非CDN IP：\n")
    while True:
        ip = file.readline().strip('\n')
        if ip == '':
            break
        all = all + 1
        if not check_cdn_cidr(ip):
            nocdnip = nocdnip + 1
            print(ip)
        if not ip:
            break
    file.close()
    print("\n总IP数：" + str(all) + "，有效IP数：" + str(nocdnip) +"，剔除CDN IP数：" + str(all-nocdnip))
    
do_check()