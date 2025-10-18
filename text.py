description = '''Seeker is a lightweight command-line utility for directory indexing and TCP port scanning. It safely lists files, builds searchable indexes, and performs responsible port probes with concurrency controls. Designed for developers and sysadmins, Seeker emphasizes usability, error-handling, and explicit permission checks to avoid misuse during network scanning operations and compliance.
'''

usage = ''' For Directory Scanning : seeker.py -t [target] -o [operation] -c [command]
            For Port Scanning : seeker.py [target] [operation] 

'''

ports_info = [
    {"port": 20,   "service": "ftp-data", "proto": "tcp", "desc": "FTP data transfer"},
    {"port": 21,   "service": "ftp",      "proto": "tcp", "desc": "FTP control/command"},
    {"port": 22,   "service": "ssh",      "proto": "tcp", "desc": "Secure Shell"},
    {"port": 23,   "service": "telnet",   "proto": "tcp", "desc": "Telnet (insecure terminal)"},
    {"port": 25,   "service": "smtp",     "proto": "tcp", "desc": "Simple Mail Transfer"},
    {"port": 53,   "service": "dns",      "proto": "udp/tcp", "desc": "Domain Name System"},
    {"port": 67,   "service": "dhcp-server", "proto": "udp", "desc": "DHCP server"},
    {"port": 68,   "service": "dhcp-client", "proto": "udp", "desc": "DHCP client"},
    {"port": 69,   "service": "tftp",     "proto": "udp", "desc": "Trivial FTP"},
    {"port": 80,   "service": "http",     "proto": "tcp", "desc": "Hypertext Transfer Protocol"},
    {"port": 110,  "service": "pop3",     "proto": "tcp", "desc": "Post Office Protocol v3"},
    {"port": 119,  "service": "nntp",     "proto": "tcp", "desc": "Network News Transfer"},
    {"port": 123,  "service": "ntp",      "proto": "udp", "desc": "Network Time Protocol"},
    {"port": 135,  "service": "ms-rpc",   "proto": "tcp", "desc": "Microsoft RPC endpoint mapper"},
    {"port": 137,  "service": "netbios-ns","proto": "udp", "desc": "NetBIOS name service"},
    {"port": 138,  "service": "netbios-dgm","proto": "udp", "desc": "NetBIOS datagram service"},
    {"port": 139,  "service": "netbios-ssn","proto": "tcp", "desc": "NetBIOS session (SMB)"},
    {"port": 143,  "service": "imap",     "proto": "tcp", "desc": "Internet Message Access Protocol"},
    {"port": 161,  "service": "snmp",     "proto": "udp", "desc": "Simple Network Management Protocol"},
    {"port": 162,  "service": "snmp-trap","proto": "udp", "desc": "SNMP trap messages"},
    {"port": 179,  "service": "bgp",      "proto": "tcp", "desc": "Border Gateway Protocol"},
    {"port": 389,  "service": "ldap",     "proto": "tcp", "desc": "Lightweight Directory Access Protocol"},
    {"port": 443,  "service": "https",    "proto": "tcp", "desc": "HTTP over TLS/SSL"},
    {"port": 445,  "service": "microsoft-ds","proto": "tcp", "desc": "SMB over TCP/IP"},
    {"port": 465,  "service": "smtps",    "proto": "tcp", "desc": "SMTP over implicit TLS (legacy usage)"},
    {"port": 514,  "service": "syslog",   "proto": "udp", "desc": "Syslog"},
    {"port": 587,  "service": "smtp-submission","proto": "tcp", "desc": "Mail submission (SMTP)"},
    {"port": 636,  "service": "ldaps",    "proto": "tcp", "desc": "LDAP over SSL"},
    {"port": 993,  "service": "imaps",    "proto": "tcp", "desc": "IMAP over SSL"},
    {"port": 995,  "service": "pop3s",    "proto": "tcp", "desc": "POP3 over SSL"},
    {"port": 1080, "service": "socks",    "proto": "tcp", "desc": "SOCKS proxy (v4/v5)"},
    {"port": 1194, "service": "openvpn",  "proto": "udp/tcp", "desc": "OpenVPN default"},
    {"port": 1433, "service": "mssql",    "proto": "tcp", "desc": "Microsoft SQL Server"},
    {"port": 1521, "service": "oracle",   "proto": "tcp", "desc": "Oracle DB listener (default)"},
    {"port": 2049, "service": "nfs",      "proto": "tcp/udp", "desc": "Network File System"},
    {"port": 3306, "service": "mysql",    "proto": "tcp", "desc": "MySQL / MariaDB"},
    {"port": 3389, "service": "rdp",      "proto": "tcp", "desc": "Remote Desktop Protocol"},
    {"port": 5432, "service": "postgres", "proto": "tcp", "desc": "PostgreSQL"},
    {"port": 5900, "service": "vnc",      "proto": "tcp", "desc": "VNC remote desktop"},
    {"port": 6379, "service": "redis",    "proto": "tcp", "desc": "Redis key-value store"},
    {"port": 8080, "service": "http-alt", "proto": "tcp", "desc": "Alternative HTTP (web apps / proxies)"},
    {"port": 8443, "service": "https-alt","proto": "tcp", "desc": "Alternative HTTPS (admin consoles)"},
]
