# FRAME Meta Model aligned with technology V1.3

Script: `tools/fixes/2026-11-06_metamodel_V1.3.py`.


## Meta-model connectors without a V1.3 rule (9) – need a decision

- Abstraction «» Role (Role) → ITS_Service (ITS_Service)
- Association «adheres to» DataObject (Data_Object) → Specification (Specification)
- Usage «Call» Low Level Function (Low_Level_Function) → Component (Component)
- Usage «Instantiate» Interface (Interface) → FRAME_Low_Level_Data_Flow (Low_Level_Data_Flow)
- Usage «Instantiate» Terminator/ Subterminator (Terminator) → Terminator/ Subterminator (Terminator)
- Usage «» DataObject (Data_Object) → InformationObject (Information_Object)
- Usage «» FRAME_Low_Level_Data_Flow (Low_Level_Data_Flow) → Interface (Interface)
- Usage «» Role (Role) → Component (Component)
- Usage «» Terminator/ Subterminator (Terminator) → Application (Application)
