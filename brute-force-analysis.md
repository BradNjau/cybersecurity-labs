# SOC Lab 2 – Brute Force Attack Detection

## Objective
Analyze system logs to detect unauthorized login attempts

## Tools Used
- Linux (auth.log)
- grep, awk, sort

## Activity Performed
- Reviewed authentication logs
- Filtered failed login attempts
- Identified repeated login failures from specific IPs

## Findings
- Multiple failed login attempts detected
- Repeated attempts from a single IP address
- Pattern indicates possible brute-force attack

## Analysis
- High number of failed attempts suggests automated attack
- Targeted common usernames such as root/admin

## Conclusion
- Detected suspicious login activity consistent with brute-force attack behavior
- Learned how to analyze logs and identify attack patterns
