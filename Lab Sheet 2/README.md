
# ENCS351 - Lab 2: System Startup, Process Creation & Termination Simulation

This repository contains the complete implementation of Lab Sheet 2 for ENCS351 Operating Systems Lab.

## Files
- `system_startup.py` — Main program script
- `process_log.txt` — Log output with process lifecycle
- `report.md` — Report containing objectives, methodology, and observations

## How to Run
1. Ensure you are on a Linux/macOS system with Python 3 installed.
2. Run the program:
   ```bash
   python3 system_startup.py
   ```
3. View the generated log:
   ```bash
   cat process_log.txt
   ```

## Expected Output
**Console:**
```
System Starting...
System Shutdown.
```

**process_log.txt:**
```
2025-07-16 12:35:21,005 - Process-1 - Process-1 started
2025-07-16 12:35:21,006 - Process-2 - Process-2 started
2025-07-16 12:35:23,007 - Process-1 - Process-1 ended
2025-07-16 12:35:23,008 - Process-2 - Process-2 ended
```

## Author
Harsh Kumar  
B.Tech — Computer Science & Engineering  
ENCS351 - Operating Systems Lab
