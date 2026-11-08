# FRAME Meta Model, third pass

Script: `tools/fixes/2026-11-06_metamodel_3_V1.3.py` (decided by the git maintainer).

- Usage «» Role → Component  becomes  Component «owned by» Role
- deleted: Abstraction «» Role → ITS_Service (path via ITS Service Process)
- Usage «» Terminator/ Subterminator → Application  becomes  «defines»
- Usage «Instantiate» Terminator/ Subterminator → Terminator/ Subterminator  becomes  «component of»
- deleted: Usage «Instantiate» Interface → FRAME_Low_Level_Data_Flow (path via Physical Data Flow)
- deleted: Usage «Call» Low Level Function → Component (path via Application)
- deleted: Usage «» FRAME_Low_Level_Data_Flow → Interface (path via Physical Data Flow)
- deleted: Usage «» DataObject → InformationObject (duplicate after merging DataObject into Data_Object)
- moved to Data_Object: «adheres to» DataObject → Specification
- deleted: Association «contains» FRAME_Low_Level_Data_Flow → DataObject (duplicate after merging DataObject into Data_Object)
- element DataObject merged into Data_Object and deleted
