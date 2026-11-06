# Connector stereotypes moved to FRAME_Profile

```
FrameNext::Componentof           → FRAME_Profile::componentof  1851
FRAME_Profile::component of      → FRAME_Profile::componentof  157
FrameNext::Servedby              → FRAME_Profile::served by    1746
FRAME_Profile::belongs to        → FRAME_Profile::belongsto    5
FrameNext::IN                    → FRAME_Profile::IN           1
FrameNext::OUT                   → FRAME_Profile::OUT          13
total 3773
```

Changed per connector: t_connector.Stereotype, the stereotype record in t_xref (FQName) and the stereotype text in the label. Connector type, direction, ends and diagram geometry unchanged.

## Label texts

After the conversion, labels that still showed an outdated stereotype text were aligned with the stereotype: 37× «Componentof» → «componentof», 744× «Belongsto» → «belongsto», 1× «abstraction» → «belongsto» on a «belongsto» link. Labels of UML standard stereotypes («call», «instantiate», «abstraction») are left as EA displays them.
