# SOC Analysis Lab 1 – Traffic Investigation

## Objective
Analyze network traffic and identify suspicious patterns

## Tools Used
- Wireshark

## Activity Performed
- Captured live network traffic
- Generated ICMP traffic using ping command
- Browsed websites to generate normal traffic

## Findings

### DNS Traffic
- Observed domain requests such as google.com
- Traffic appeared normal

### ICMP Traffic
- Continuous ICMP packets detected from one source
- High frequency of packets over short time

### Analysis
- The ICMP activity could indicate a ping flood or network scanning behavior
- DNS activity appeared legitimate

## Conclusion
- Identified difference between normal and potentially suspicious traffic
- Gained understanding of traffic analysis and threat detection basics
