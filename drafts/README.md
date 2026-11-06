# FRAME – Working Drafts

This directory contains **working drafts** of the FRAME. Drafts represent ongoing development and are the primary place where updates, corrections, and improvements are made before they are included in an official release.

## 📂 Structure and Naming

Drafts follow the naming pattern:

```
<target-version>-draft.<iteration>
```

Examples:

```
1.1.0-draft.1 
1.1.0-draft.2 
2.0.0-draft.1
```

The folder:

```
/drafts/latest
```

always contains the **most up‑to‑date working draft**, including corrections to existing releases.

## 🧭 Purpose of This Directory

Drafts are used for:

- Preparing the next FRAME release  
- Incorporating feedback from Member States and experts  
- Correcting issues identified in published releases  
- Testing new modelling approaches  
- Updating documentation and high‑level views  

Once a draft is validated and approved, it becomes a new numbered release.

## 🛠 Working With Draft Models

To open draft models in Enterprise Architect:

1. Create a **new, empty EA project**.  
2. Load the **FRAME toolbox**.  
3. Import the draft `.xmi` file.  

Importing the XMI before loading the toolbox will break stereotypes.

## 📌 Relationship to Releases

Stable, published versions of the FRAME are available in:

```
/releases
```

Drafts should be considered **pre‑release material** and may change without notice.

When **ready for release**, clean the `drafts/latest` content since all will become a new tagged release and:

- commit, 
- tag (´vX.Y.Z´ to e.g. ´v2.1.1´) and 
- push. 

``` 
git add .
git commit -m "your commit message"
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

