# Some magic?

Your should configure router like this https://itdog.info/tochechnaya-marshrutizaciya-po-domenam-na-routere-s-openwrt/#%d0%b0%d0%b2%d1%82%d0%be%d0%bc%d0%b0%d1%82%d0%b8%d1%87%d0%b5%d1%81%d0%ba%d0%b0%d1%8f-%d1%83%d1%81%d1%82%d0%b0%d0%bd%d0%be%d0%b2%d0%ba%d0%b0-%d0%b8-%d0%bd%d0%b0%d1%81%d1%82%d1%80%d0%be%d0%b9%d0%ba%d0%b0-%d1%87%d0%b5%d1%80%d0%b5%d0%b7-shell-%d1%81%d0%ba%d1%80%d0%b8%d0%bf%d1%82

1. Setup Firewall:
1.1. Add to /etc/config/firewall:

config ipset
        option name 'vpn_ip'
        option match 'dst_net'
        option loadfile '/tmp/lst/ip.lst'

config rule
        option name 'mark_ip'
        option src 'lan'
        option dest '*'
        option proto 'all'
        option ipset 'vpn_ip'
        option set_mark '0x1'
        option target 'MARK'
        option family 'ipv4'

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


2. Owerwrite sctipt /etc/init.d/getdomains with UnicornsUpdater script source code
3. Start command /etc/init.d/network restart
4. Start command /etc/init.d/getdomains start

