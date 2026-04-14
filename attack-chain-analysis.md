# Final Lab – Attack Chain Analysis

## Scenario
Simulated attacker attempting to gain unauthorized access

## Attack Stages Observed

### 1. Reconnaissance
- Performed network scan using Nmap
- Identified open ports (e.g., SSH)

### 2. Access Attempt
- Multiple failed SSH login attempts detected

### 3. Network Evidence
- Observed repeated traffic to port 22 in Wireshark

### 4. Log Evidence
- Found multiple "Failed password" entries in auth.log

## Analysis
- Activity indicates attempted unauthorized access
- Pattern consistent with brute-force or credential guessing

## Conclusion
- No successful compromise detected (if true)
- Attack attempt successfully identified

## Key Learning
- Attacks follow patterns that can be detected
- Combining network + logs gives full visibility
