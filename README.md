# Some magic?

Add to /etc/config/firewall:

config ipset
        option name 'vpn_ip'
        option match 'dst_net'
        option loadfile '/tmp/lst/ip.lst'


config ipset
        option name 'vpn_subets'
        option match 'dst_net'
        option loadfile '/tmp/lst/subnet.lst'


config rule
        option name 'mark_subnet'
        option src 'lan'
        option dest '*'
        option proto 'all'
        option ipset 'vpn_subnets'
        option set_mark '0x1'
        option target 'MARK'
        option family 'ipv4'
