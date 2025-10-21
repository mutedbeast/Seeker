import socket
import ssl
from text import ports_info  # keep your import as-is
from typing import List, Dict, Any

important_ports = [x['port'] for x in ports_info]
all_ports = set(range(1, 65536))
rest_ports = sorted(all_ports - set(important_ports))


def scan_port(target: str, port: int, timeout: float = 1.0, tls_ports: set | None = None) -> Dict[str, Any]:
    
    if tls_ports is None:
        tls_ports = {443, 8443}

    result = {"port": port, "open": False, "tls": False, "cert_subject": None, "error": None}
    try:
        with socket.create_connection((target, port), timeout=timeout) as sock:
            result["open"] = True
            if port in tls_ports:
                context = ssl.create_default_context()
                try:
                    with context.wrap_socket(sock, server_hostname=target) as ssock:
                        cert = ssock.getpeercert()
                        result["tls"] = True
                        result["cert_subject"] = cert.get("subject") if cert else None
                except ssl.SSLError as e:
                    result["error"] = f"TLS handshake failed: {e!s}"
            return result

    except (socket.timeout, TimeoutError) as e:
        result["error"] = f"timeout: {e}"
    except ConnectionRefusedError as e:
        result["error"] = f"connection refused: {e}"
    except socket.gaierror as e:
        result["error"] = f"dns error: {e}"
    except OSError as e:
        result["error"] = f"os error: {e}"
    except Exception as e:
        result["error"] = f"unexpected error: {type(e).__name__}: {e}"
    return result


def port_scan_main(target: str, verbose = False,timeout: float = 1.0, scan_rest_if_none: bool = True) -> List[Dict[str, Any]]:
    
    tls_ports = {443, 8443}
    results: List[Dict[str, Any]] = []

    print(f"Starting scan of {target} (timeout={timeout}s). Scanning {len(important_ports)} important ports...")
    for port in important_ports:
        r = scan_port(target, port, timeout=timeout, tls_ports=tls_ports)
        results.append(r)
        if r["open"]:
            print(f"[+] {target}:{port} is open (TCP).")
            if r["tls"]:
                print(f"    TLS handshake succeeded. Certificate subject: {r['cert_subject']}")
            elif r["error"]:
                print(f"    Note: {r['error']}")
            else:
                print(f"    (No TLS expected on port {port}; connection succeeded at TCP level.)")
        if verbose:
            print(f"[-] {target}:{port} closed or unreachable. {r['error']}")

    open_important = [r for r in results if r["open"]]
    if scan_rest_if_none and not open_important:
        print(f"No important ports were open — scanning remaining {len(rest_ports)} ports (this may take a while)...")
        for port in rest_ports:
            r = scan_port(target, port, timeout=timeout, tls_ports=tls_ports)
            results.append(r)
            if r["open"]:
                print(f"[+] {target}:{port} is open (TCP).")

    print("Scan complete.")
    return results



