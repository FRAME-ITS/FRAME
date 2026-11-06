# Direct fixes before the 5.3 pull request (2026-11-06)

Agreed by the git maintainer. Script: `tools/fixes/2026-11-06_direct_fixes.py` (one step per commit). EA Project Integrity check on the result: no problems found.

## Add the missing parent function of five low-level functions

- «component of» F3.1.1.5.11 Monitor Access to Urban Zones → F3.1.1.5 Provide Urban Traffic Management Facilities
- «component of» F3.1.1.5.12 Prevent Access to Urban Zones → F3.1.1.5 Provide Urban Traffic Management Facilities
- «component of» F3.1.1.5.21 Send Messages to Approaching Urban Vehicles → F3.1.1.5 Provide Urban Traffic Management Facilities
- «component of» F3.1.2.14.6 Send Messages to Approaching Inter-urban Vehicles → F3.1.2.14 Implement Inter-urban Management Traffic Strategy
- «component of» F6.5.8 Enable Final Approval of Trip Plan → F6.5 Prepare Trip Plan

## C-ITS user needs: Usage links to low-level functions become «served by»

- Usage → «served by»: 11.1.4.1 → F5.16.2 Output Commands and Dynamic Warnings
- Usage → «served by»: 11.1.4.1 → F5.16.1 Manage Communication from Vehicle to Driver
- Usage → «served by»: 11.2.4.1 → F5.16.1 Manage Communication from Vehicle to Driver
- Usage → «served by»: 11.2.4.1 → F5.16.2 Output Commands and Dynamic Warnings
- Usage → «served by»: 11.1.1.6 → F5.16.2 Output Commands and Dynamic Warnings
- Usage → «served by»: 11.1.1.6 → F5.16.1 Manage Communication from Vehicle to Driver
