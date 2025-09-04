# scanner

This repository contains an example Python script for reading CPU temperature via SNMP using the `pysnmp` library.

## Usage

```
python3 cpu_temp_snmp.py HOST [-c COMMUNITY] [-o OID] [-p PORT]
```

Replace `HOST` with the SNMP agent address. Adjust the OID to match your device's temperature sensor.
