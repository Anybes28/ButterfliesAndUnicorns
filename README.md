# Some magic?

Add to /etc/config/firewall:

config ipset
        option name 'vpn_ip'
        option match 'dst_net'
        option loadfile '/tmp/lst/ip.lst'

config ipset
        option name 'vpn_sunets'
        option match 'dst_net'
        option loadfile '/tmp/lst/subnet.lst'
