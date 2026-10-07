from typing import Dict, Any, Optional
def audit_targets(target_config: dict, stealth_mode=False: bool) -> Optional[Dict[str, int, bool, str, Any]:
    flagged_ports = []
    valid_ports = []
    raw_ports = target_config.get("raw_ports", [])
    content_ports = [] # List to be used the casted ports
    try:
        for everyport in raw_ports:
            try:
                content_ports.append(int(everyport)) # Cast strings to integers
            except ValueError as e:
                print(f"Invalid port entry {everyport}: {e}")

        port_sort = set(content_ports) # Remove duplicate ports
    
        for everyport in port_sort:
            if stealth_mode:
                if everyport == 80: # Skip port 80
                    continue
            if everyport in target_config["critical_ports"]:
                flagged_port.append(port) # Flag port in the critical_ports collection
            else:
                valid_ports.append(port)
    except ValueError as e:
        print(f"Invalid port entries: {e}")
    finally:
        print("Audit log flushed to disk.")
