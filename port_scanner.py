import socket
import ssl

from text import ports_info

important_ports = []
for x in ports_info:
    important_ports.append(x['port'])

def port_scan(target: str, timeout: float = 1.0):
    """Try to connect to target:port. If it's a TLS port, attempt an SSL handshake and print cert."""
    for port in important_ports:
        tls_ports = {443, 8443}  
        try:
            with socket.create_connection((target, port), timeout=timeout) as sock:
                print(f"[+] {target}:{port} is open (TCP).")
                if port in tls_ports:
                    # Perform TLS handshake
                    context = ssl.create_default_context()
                    try:
                        with context.wrap_socket(sock, server_hostname=target) as ssock:
                            cert = ssock.getpeercert()
                            print(f"    TLS handshake succeeded. Certificate subject: {cert.get('subject')}")
                    except ssl.SSLError as e:
                        print(f"    TLS handshake failed: {e!s}")
                else:
                    # Plain TCP (no TLS)
                    print(f"    (No TLS expected on port {port}; connection succeeded at TCP level.)")

        except (socket.timeout, ConnectionRefusedError) as e:
            print(f"[-] {target}:{port} is closed or unreachable ({e.__class__.__name__}: {e}).")
        except socket.gaierror as e:
            print(f"[-] DNS error resolving {target}: {e}")
        except Exception as e:
            print(f"[-] Unexpected error connecting to {target}:{port} -> {type(e).__name__}: {e}")







#port_scan('google.com')