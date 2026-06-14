# Detection-as-Code Lab

## Overview

This project demonstrates Detection-as-Code using Sigma rules, Windows event telemetry, Splunk detection logic, and MITRE ATT&CK mapping.

The objective of this lab is to create reusable security detections that can be version-controlled, reviewed, shared, and mapped to known adversary techniques.

Detection-as-Code helps security teams manage detections using the same principles applied to software development, improving consistency, documentation, and detection coverage.

---

## Repository Structure

```text
Detection-as-Code-Lab
│
├── README.md
│
├── sigma
│   ├── powershell_execution.yml
│   ├── cmd_execution.yml
│   ├── account_discovery.yml
│   ├── failed_logons.yml
│   └── privileged_logons.yml
│
└── mappings
    └── mitre_mapping.md
```

---
## Sigma Rules

- [PowerShell Execution](sigma/powershell_execution.yml)
- [Command Shell Execution](sigma/cmd_execution.yml)
- [Account Discovery](sigma/account_discovery.yml)
- [Failed Logons](sigma/failed_logons.yml)
- [Privileged Logons](sigma/privileged_logons.yml)

## MITRE Mapping

- [MITRE ATT&CK Coverage](mappings/mitre_mapping.md)

### PowerShell Execution Detection

Detects execution of PowerShell on Windows systems.

**MITRE ATT&CK:** T1059.001 – PowerShell

---

### Command Shell Execution Detection

Detects execution of the Windows Command Prompt.

**MITRE ATT&CK:** T1059.003 – Windows Command Shell

---

### Account Discovery Detection

Detects account discovery activity using commands such as:

* whoami.exe
* net.exe

**MITRE ATT&CK:** T1087 – Account Discovery

---

### Failed Logons Detection

Detects failed Windows authentication attempts.

**MITRE ATT&CK:** T1110 – Brute Force

---

### Privileged Logons Detection

Detects logon sessions that receive elevated privileges.

**MITRE ATT&CK:** T1078 – Valid Accounts

---

## MITRE ATT&CK Coverage

| Sigma Rule              | Technique ID | Technique             |
| ----------------------- | ------------ | --------------------- |
| PowerShell Execution    | T1059.001    | PowerShell            |
| Command Shell Execution | T1059.003    | Windows Command Shell |
| Account Discovery       | T1087        | Account Discovery     |
| Failed Logons           | T1110        | Brute Force           |
| Privileged Logons       | T1078        | Valid Accounts        |

---

## Detection Engineering Workflow

The workflow used in this project includes:

1. Identify attacker behavior
2. Map activity to MITRE ATT&CK
3. Develop Sigma detection logic
4. Validate detection requirements
5. Document detection purpose
6. Maintain detections through version control

---

## Detection Philosophy

Detection-as-Code enables security teams to:

* Standardize detection development
* Improve documentation quality
* Track detection changes over time
* Share detection logic across platforms
* Support SOC operations and threat hunting activities
* Improve detection coverage and visibility

---

## Skills Demonstrated

* Detection Engineering
* Detection-as-Code
* Sigma Rule Development
* MITRE ATT&CK Mapping
* Windows Security Monitoring
* Threat Detection
* Threat Hunting
* Security Operations (SOC)
* Blue Team Methodology
* Security Documentation

---

## Future Improvements

Potential future enhancements include:

* Additional Sigma rules
* Sigma-to-Splunk conversions
* Sigma-to-Microsoft Sentinel conversions
* Detection testing procedures
* False positive analysis
* Detection coverage dashboards

---

## Author

**Agata Gabara**

Cybersecurity Analyst | SOC Analyst | Threat Hunter

GitHub: https://github.com/ag48665
