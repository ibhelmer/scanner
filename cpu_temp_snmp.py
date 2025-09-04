#!/usr/bin/env python3
"""Retrieve CPU temperature via SNMP using pysnmp."""

import argparse
import sys

try:
    from pysnmp.hlapi import (
        SnmpEngine,
        CommunityData,
        UdpTransportTarget,
        ContextData,
        ObjectType,
        ObjectIdentity,
        getCmd,
    )
except ImportError:
    sys.stderr.write("pysnmp is required. Install with 'pip install pysnmp'.\n")
    raise


def fetch_temperature(host: str, community: str, oid: str, port: int) -> str:
    """Fetch a temperature value from an SNMP agent."""
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=0),
        UdpTransportTarget((host, port)),
        ContextData(),
        ObjectType(ObjectIdentity(oid)),
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        raise RuntimeError(errorIndication)
    elif errorStatus:
        raise RuntimeError(
            "%s at %s"
            % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
            )
        )
    else:
        for name, val in varBinds:
            return str(val)
    raise RuntimeError("No SNMP data received.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch CPU temperature via SNMP")
    parser.add_argument("host", help="SNMP agent hostname or IP address")
    parser.add_argument(
        "-c",
        "--community",
        default="public",
        help="SNMP community string (default: public)",
    )
    parser.add_argument(
        "-o",
        "--oid",
        default="1.3.6.1.4.1.2021.13.16.2.1.3.1",
        help="OID for CPU temperature",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=161,
        help="SNMP port number (default: 161)",
    )
    args = parser.parse_args()

    temperature = fetch_temperature(args.host, args.community, args.oid, args.port)
    print(f"CPU Temperature: {temperature}")


if __name__ == "__main__":
    main()
