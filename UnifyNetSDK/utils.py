from ipaddress import ip_address


def is_ipv4(ip):
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False
