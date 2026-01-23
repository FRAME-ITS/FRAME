# FRAME Architecture

![Version](https://img.shields.io/github/v/tag/FRAME-ITS/FRAME?label=version&style=flat-square)
![License](https://img.shields.io/github/license/FRAME-ITS/FRAME?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/FRAME-ITS/FRAME?style=flat-square)
![Open Issues](https://img.shields.io/github/issues/FRAME-ITS/FRAME?style=flat-square)
![Closed Issues](https://img.shields.io/github/issues-closed/FRAME-ITS/FRAME?style=flat-square)

The **FRAME Architecture** (originally the European ITS Framework Architecture) has been a foundational reference for Intelligent Transport Systems (ITS) in Europe for more than two decades.  
It was first published in 2000 as part of the EC‑funded **KAREN** project, following recommendations from the High Level Group on transport telematics and a supporting Council resolution.

The purpose of FRAME has always been to provide:
- A **systematic basis** for planning ITS implementations  
- A framework enabling **integration** of multiple ITS systems  
- A foundation for **interoperability**, including cross‑border use cases  
- A **shared modelling methodology** for ITS architects and implementers  

Development of the FRAME Architecture and the FRAME Toolbox continues, and this repository is the central place for issues, drafts, and releases.

## 📁 Repository Structure

The repository follows a clear structure to separate **stable releases** from **ongoing development**:

- `/releases/`        → Official, stable FRAME Architecture releases 
- `/drafts/`          → Working drafts preparing future releases 
- `/drafts/latest/`   → Most up‑to‑date working draft

### **Releases**

Stable, versioned FRAME Architecture packages, including:
- Enterprise Architect model files (`.qea`, `.xmi`)
- Documentation exports
- Methodology material

Releases are **immutable** once published.

### **Drafts**

Work‑in‑progress updates preparing the next FRAME release.  

Drafts follow the naming pattern: `<target-version>-draft.<iteration>`

Example: `2.1.0-draft.1`

The folder `/drafts/latest` always contains the most current working draft, including corrections to existing releases.

## 🧩 Working With FRAME Models

FRAME models are provided as:
- **XMI files** (model exchange)
- **QEA files** (Enterprise Architect project)
- **FRAME Toolbox** (required for stereotypes and modelling conventions)

To open a FRAME model in Enterprise Architect:

1. Create a **new, empty EA project**.  
2. Load the **FRAME Toolbox**.  
3. Import the FRAME `.xmi` file.  

> Importing the XMI before loading the toolbox will break stereotypes.


## 📚 Documentation and Resources

Additional FRAME information, descriptions, and background material can be found in the **Wiki** section of this repository.

Workshops, tutorials, and historical materials are available at:

- FRAME Online (legacy): https://frame-online.eu/
- FRAME Online (in development): https://frame-its.github.io/FRAME-online/


## 🔗 External Resources (Legacy Hosting)

Some legacy materials remain hosted externally:

- Complete FRAME Architecture (including eCall, Truck Parking, C‑ITS, NAP, NB)  
- FRAME Toolbox for EA import  
- FRAME Workshops and tutorials  

These will be progressively migrated into the structured `/releases` and `/drafts` directories.


## 🔄 Related Reference Architectures

FRAME is used as the methodological basis for several ongoing reference architecture developments within **NAPCORE**:

- **NAPCORE National Access Point Reference Architecture**  
  https://github.com/NAPCORE/NAP-Reference-Architecture

- **NAPCORE National Body Reference Architecture**  
  https://github.com/NAPCORE/NB-Reference-Architecture


## 🗨 Issues and Discussions

Questions, issues, and proposals for improvement can be submitted via the **Issues** tab.  
Please use appropriate labels to help categorise your contribution.

## 🤝 Contact

For workshop requests, cooperation, or general enquiries:  
https://frame-online.eu/
