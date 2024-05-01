from ipaddress import ip_address


def is_ipv4(ip: str):
    # 判断传入的字符串是否为ipv4格式地址
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False
