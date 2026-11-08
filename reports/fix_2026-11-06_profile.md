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

## Correction: target names of the embedded technology V1.2

The first conversion used the stereotype names of the toolbox file in this repository (`releases/5.1.1/toolbox`, technology **V1.0**:
`componentof`, `belongsto`). The model itself carries a newer technology, **FRAME Architecture V1.2** (t_document TECHNOLOGY), which
Enterprise Architect uses for this model; it defines `component of` and `belongs to` instead. All connectors were therefore aligned with V1.2:

```
FRAME_Profile::componentof → FRAME_Profile::component of   2613
FRAME_Profile::belongsto   → FRAME_Profile::belongs to      871
```

Every FRAME connector stereotype used in the model is now defined in the embedded technology (see `reports/mdg_technology.md`, produced by `tools/mdg.py`).
The toolbox files in `releases/` and `drafts/latest/` (V1.0) are outdated. The V1.2 technology extracted from the model is in
`drafts/latest/toolbox/FRAME_Technology_V1.2_embedded.xml`, but it lacks the stereotype images and most scripts, so a complete
V1.2 file has to be generated in Enterprise Architect before release 5.3 (see `drafts/latest/toolbox/README.md`).
