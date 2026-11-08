# FRAME Meta Model aligned with technology V1.3

Script: `tools/fixes/2026-11-06_metamodel_V1.3.py`.

- element Requirement: stereotype FRAME_Reqirement → FRAME_Requirement
- reversed: «component of» High Level Function → Low Level Function  becomes  Low Level Function → High Level Function
- reversed: «component of» Fuctional Area → Low Level Function  becomes  Low Level Function → Fuctional Area
- reversed: «IN» FRAME_Low_Level_Data_Flow → Terminator/ Subterminator  becomes  Terminator/ Subterminator → FRAME_Low_Level_Data_Flow
- reversed: «OUT» Terminator/ Subterminator → FRAME_Low_Level_Data_Flow  becomes  FRAME_Low_Level_Data_Flow → Terminator/ Subterminator
- reversed: «component of» Fuctional Area → High Level Function  becomes  High Level Function → Fuctional Area
- Association → «belongs to»: User_Need → UserNeedTopic
- reversed: «belongs to» UserNeedGroup → UserNeedService  becomes  UserNeedService → UserNeedGroup
- reversed: «belongs to» UserNeedService → UserNeedTopic  becomes  UserNeedTopic → UserNeedService

## Meta-model connectors without a V1.3 rule (15) – need a decision

- Abstraction «» Requirement (Requirement) → Specification (Specification)
- Abstraction «» Role (Role) → ITS_Service (ITS_Service)
- Association «adheres to» DataObject (Data_Object) → Specification (Specification)
- Association «defines» FRAME_Low_Level_Data_Flow (Low_Level_Data_Flow) → DataObject (Data_Object)
- Usage «Call» Low Level Function (Low_Level_Function) → Component (Component)
- Usage «Instantiate» Interface (Interface) → FRAME_Low_Level_Data_Flow (Low_Level_Data_Flow)
- Usage «Instantiate» Terminator/ Subterminator (Terminator) → Terminator/ Subterminator (Terminator)
- Usage «» Application (Application) → Low Level Function (Low_Level_Function)
- Usage «» Application (Application) → Physical Dataflow (Physical_Data_Flow)
- Usage «» Component (Component) → Physical Dataflow (Physical_Data_Flow)
- Usage «» DataObject (Data_Object) → InformationObject (Information_Object)
- Usage «» FRAME_Low_Level_Data_Flow (Low_Level_Data_Flow) → Interface (Interface)
- Usage «» InformationObject (Information_Object) → InformationObject (Information_Object)
- Usage «» Role (Role) → Component (Component)
- Usage «» Terminator/ Subterminator (Terminator) → Application (Application)
