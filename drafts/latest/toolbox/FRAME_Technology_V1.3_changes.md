# FRAME MDG technology V1.3 – changes against V1.2 (embedded in FRAME.qea)

Built by `tools/fixes/2026-11-06_mdg_technology_V1.3.py`.

- stereotype «Impacts» renamed «impacts» (10 occurrences)
- stereotype «deliverd by» renamed «delivered by» (7 occurrences)
- Quick Linker: «Component of» → «component of» (3 rules)
- Quick Linker: «Defines» → «defines» (13 rules)
- Quick Linker: «instant of» → «instants of» (1 rules)
- Quick Linker: «associated» → «associate» (1 rules)
- Quick Linker reversed: «component of» Functional_Area → Low_Level_Function  becomes  Low_Level_Function → Functional_Area
- Quick Linker reversed: «component of» Functional_Area → High_Level_Function  becomes  High_Level_Function → Functional_Area
- Quick Linker reversed: «component of» High_Level_Function → Low_Level_Function  becomes  Low_Level_Function → High_Level_Function
- Quick Linker reversed: «belongs to» User_Need_Group → User_Need_Service  becomes  User_Need_Service → User_Need_Group
- Quick Linker reversed: «belongs to» User_Need_Service → User_Need_Topic  becomes  User_Need_Topic → User_Need_Service
- Quick Linker reversed: «belongs to» User_Need_Topic → User_Need  becomes  User_Need → User_Need_Topic
- Quick Linker reversed: «associate» Mission_Statement → ITS_Vision  becomes  ITS_Vision → Mission_Statement
- Quick Linker added: «component of» Terminator → Terminator
- Quick Linker added: «component of» High_Level_Function → High_Level_Function
- Quick Linker added: «component of» Functional_Area → System
- Quick Linker added: «IN» System → High_Level_Data_Flow
- Quick Linker added: «OUT» High_Level_Data_Flow → System
- Quick Linker added: «IN» Functional_Area → Low_Level_Data_Flow
- Quick Linker added: «OUT» Low_Level_Data_Flow → Functional_Area
- Quick Linker: Application – 4 rules merged into 3
- Quick Linker: ITS_Service – 4 rules merged into 3
- Quick Linker: ITS_Service_Added_Value – 2 rules merged into 1
- Quick Linker: ITS_Service_Process – 4 rules merged into 3
- Quick Linker: ITS_Vision – 3 rules merged into 2
- Quick Linker: Low_Level_Data_Flow – 7 rules merged into 6
- Quick Linker: Low_Level_Function – 8 rules merged into 6
- Quick Linker: Mission_Statement – 2 rules merged into 1
- Quick Linker: Role – 4 rules merged into 3
- Quick Linker: Terminator – 6 rules merged into 5
- Quick Linker: User_Need – 4 rules merged into 3
- Quick Linker: TDF_LowLevelFunction – 4 rules merged into 3
- Quick Linker: UML links hidden (_HideUmlLinks) for Functional_Area, High_Level_Function, Low_Level_Function, High_Level_Data_Flow, Low_Level_Data_Flow, Terminator, Datastore, System, User_Need, User_Need_Topic, User_Need_Service, User_Need_Group
- model images added from V1.0: 7 (start-page images)
