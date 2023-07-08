import re, sys, subprocess

def get_ttl(ip_address):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    out = out.split()
    out = out[12].decode('utf-8')
    ttl_value = re.findall(r"\d{1,3}", out)
    return ttl_value

def get_os(ttl):
    ttl = int(ttl[0])
    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"

ip_address = sys.argv[1]
ttl = get_ttl(ip_address)
os_name = get_os(ttl)
print("%s (ttl -> %s): %s" % (ip_address, ttl[0], os_name))