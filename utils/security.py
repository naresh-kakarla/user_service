from ipaddress import ip_address, ip_network

ALLOWED_INTERNAL_NETWORKS = [
    "127.0.0.1/32",
    "10.0.0.0/8",
    "172.16.0.0/12",
    "192.168.0.0/16",
]


allowed_network = [ip_network(net) for net in ALLOWED_INTERNAL_NETWORKS]


def is_internal_request(request):
    remote_ip = request.META.get("REMOTE_ADDR")
    if not remote_ip:
        return False
    try:
        ip = ip_address(remote_ip)
        return any(ip in net for net in allowed_network)
    except ValueError:
        return False
