# Smart Warehouse Automation & Inventory Management System
## AFW Limited – Warehouse Redesign, Inventory Control & SOP Framework

[![Git LFS Tracked](https://img.shields.io/badge/Git%20LFS-Enabled-blue.svg)](https://git-lfs.github.com)
[![Data Security](https://img.shields.io/badge/Data%20Security-Sanitized%20%26%20Protected-green.svg)](#data-security--confidentiality-protection)
[![SOP Annexures](https://img.shields.io/badge/SOP%20Annexures-25%20Standardized-purple.svg)](#sop-annexures--operations-manuals)

---

## Executive Summary

This repository presents the comprehensive engineering study, spatial layout blueprints, operational SOPs, and inventory optimization models developed for **AFW**. 

The primary objective of this project was to analyze depot bottlenecks across regional distribution networks, redesign warehouse spatial utilization, standardize Carry & Forwarding (C&F) operations, and formulate mathematical inventory management strategies (EOQ, Safety Stock, Reorder Point, and ABC Analysis) for high-velocity Fast-Moving Consumer Goods (FMCG) distribution (including Fortune edible oils, grains, and allied food products).

---

## Technical Author & Academic Credentials

- **Author:** Vipul Kumar Chobisa (MBA Tech. / IT Operations & AI-Ops Specialist)
- **Project Title:** *Design of a Warehouse: A Case Study of AFW Limited*
- **Sponsoring Organization:** AFW Limited (C&F Operations & Logistics Division)
- **Academic Program:** MBA (Technology Management) / B.Tech Computer Engineering
- **Authorization & Credentials:** Officially authorized internship letters (2013, 2014) and college thesis artifacts included in repository (`INTERNSHIP/` & `Report final/`).

---

## Data Security & Confidentiality Protection

> [!IMPORTANT]
> **Confidentiality & Data Protection Compliance:**
> Raw commercial sales transactions, 4-year historical sales ledgers (FY09-10 through FY13-14), line-wise SKU classifications, Demand Forecasting raw datasets, and internal MRP presentations have been **removed and sanitized** from this repository to enforce corporate data security, prevent unauthorized exposure, and protect proprietary business intelligence.
> 
> All remaining Excel spreadsheets, telemetry workbooks, and financial analysis tables have been obfuscated and secured. Video media formats are excluded via `.gitignore`.

---

## Mathematical Inventory Optimization Formulas

To transition from ad-hoc replenishment to systematic control, the repository incorporates formal mathematical inventory control models:

### 1. Economic Order Quantity (EOQ)

The Economic Order Quantity balances annual order placement costs against inventory holding costs:

$$EOQ = \sqrt{\frac{2 \cdot D \cdot S}{H}}$$

Where:
- $D$ = Annual Demand (units/year) derived from sanitized inventory telemetry.
- $S$ = Ordering / Setup Cost per order ($\text{INR } / \text{order}$).
- $H$ = Annual Carrying / Holding Cost per unit ($\text{INR } / \text{unit} / \text{year} = i \cdot C$, where $i$ is holding rate percentage and $C$ is unit purchasing cost).

---

### 2. Reorder Point (ROP) & Safety Stock ($SS$)

To guarantee zero stockouts during lead time variances across C&F depots:

$$ROP = (d \times L) + SS$$

Where:
- $d$ = Average Daily Demand ($\text{units} / \text{day}$).
- $L$ = Replenishment Lead Time ($\text{days}$).
- $SS$ = Safety Stock buffer, computed under demand uncertainty using:

$$SS = Z_{\alpha} \times \sigma_L = Z_{\alpha} \times \sqrt{L \cdot \sigma_d^2 + d^2 \cdot \sigma_L^2}$$

Where:
- $Z_{\alpha}$ = Standard normal distribution factor corresponding to targeted service level (e.g., $Z = 1.65$ for $95\%$ service level, $Z = 2.33$ for $99\%$ service level).
- $\sigma_d$ = Standard deviation of daily demand.
- $\sigma_L$ = Standard deviation of supplier replenishment lead time.

---

### 3. Total Annual Inventory Cost ($TAC$)

$$TAC = (D \cdot C) + \left( \frac{D}{Q} \cdot S \right) + \left( \frac{Q}{2} \cdot H \right) + (SS \cdot H)$$

Where:
- $Q$ = Order quantity (set to $EOQ$ for optimal cost minimization).

---

## Warehouse Layout Designs & Depot Catalog

The project includes **18 spatial layout blueprints, 3D renderings, and presentation assets** engineered to eliminate congestion, establish dedicated pick/pack zones, optimize aisle widths, and streamline dock door throughput:

| Depot Location | File Name | Format | Spatial Focus / Description |
| :--- | :--- | :--- | :--- |
| **Bareilly Gvapl** | `Bareily gvapl.png` | PNG | Regional distribution center, optimized bay allocation |
| **Bareilly Main** | `Bareily.png` | PNG | Primary storage flow layout, high-density pallet racking |
| **Delhi Facility 3** | `Delhi3.png` | PNG | Multi-dock loading bay and cross-docking zone |
| **Delhi Facility 4** | `delhi4.png` | PNG | Fast-moving SKU staging area |
| **Ghaziabad** | `Ghazizbad.png` | PNG | Staging and dispatch zone layout |
| **Lucknow** | `Lucknow.png` | PNG | Main hub receiving & outbound buffer design |
| **Ranchi Final** | `Rachi final.png` | PNG | Final floor map with forklift travel aisles |
| **Faizabad** | `faizabad.png` | PNG | Mid-tier depot layout optimization |
| **Muzaffarpur 1** | `muzzufurpur1.png` | PNG | Primary inbound storage zone |
| **Muzaffarpur 2** | `muzzufurpur 2.png` | PNG | Secondary stack zone allocation |
| **Muzaffarpur 3** | `muzzafurpur3.png` | PNG | Finished product staging design |
| **Shahbad** | `shahbad.png` | PNG | Regional stockyard and pallet flow map |
| **Siliguri Final** | `siliguri final.png` | PNG | North-East gateway warehouse blueprint |
| **Varanasi** | `varanasi.png` | PNG | High-density stacking & picking grid |
| **Kolkata Central** | `KOLKATA2.ppt` | PPT | Executive layout presentation & flow analysis |
| **Dhanbad** | `layout/revise/Dhanbad.png` | PNG | Revised depot layout blueprint |
| **Malda** | `layout/revise/Malda layout.tif` | TIF | High-resolution spatial masterplan |
| **Asansol** | `layout/revise/asansole.png` | PNG | Revised regional stock distribution layout |

---

## SOP Annexures & Operations Manuals

The repository houses **25 standardized operating annexures, audit frameworks, and C&F manuals** to enforce operational compliance:

1. `CF Operations SOP Final.doc`: Master C&F Operating Manual.
2. `sop 1.docx`: Standardized receiving, binning, and dispatch instructions.
3. `Audit CFA_Depot Annexures 13 14.xls`: CFA depot audit checklist and scorecards.
4. `Annexure -1D.xlsx`: Stock reconciliation and damage report template.
5. `Annexure -2.docx`: Inbound material receipt notification protocol.
6. `Annexure -3.doc` & `Annexure -3 (A).doc`: Vehicle inspection and dock safety checklists.
7. `Annexure -4.docx`: Physical verification and stack tally sheets.
8. `Annexure -5.docx`: FIFO/FEFO stock rotation enforcement protocols.
9. `Annexure -6.xls`, `Annexure -6 (A).doc`, `Annexure -6 (B).doc`: Non-conforming stock & leakage management procedures.
10. `Annexure -8.docx`: Secondary transport dispatch logs.
11. `Annexure -10 (A).docx`: Warehouse security and entry/exit controls.
12. `anx 12.xlsx`: Depot space utilization & volume tracking workbook.
13. `Annexure -14.pdf`: Claims settlement and transit damage authorization guidelines.
14. `Annexure -15.doc`: Customer return handling & credit note approval workflow.
15. `Annexure-16.docx`, `Annexure-16 (A).docx`, `Annexure-16 (B).docx`: Pest control & hygiene audit standards.
16. `Annexure-17.doc`: Cold storage & environmental conditions log.
17. `ANNEXURE -18.docx` & `Annexure-18.docx`: Emergency response & material safety data protocols.
18. `New Annuxure.xlsx`: Updated depot performance KPI reporting framework.
19. `From the desk of VC.docx`: Executive summary notes and operational recommendations.

---

## Repository Structure

```
afw-inventory/
├── .gitattributes                                  # Git LFS rules for large media/binary assets
├── .gitignore                                      # Exclusion rules (videos & temporary files)
├── README.md                                       # Repository master documentation
├── INTERNSHIP/                                     # Thesis, Layouts, SOP Annexures, Secured Workbooks
│   ├── Anexure/                                    # 25 SOP Annexures & Manuals
│   ├── Assignment/                                 # Academic assignments & zone studies
│   ├── layout/                                     # 15 Warehouse layout image blueprints
│   │   └── revise/                                 # 3 Additional revised depot designs (TIF, PNG)
│   ├── Project/                                    # ABC Analysis, Central Layouts, Reports
│   ├── south/                                      # Southern region depot layout studies
│   ├── Warehousing/                                # Warehousing ABC analysis by region (Secured)
│   ├── Viul Kumar Chobisa MBA(Tech.) ... .pdf      # Complete Academic Master Thesis PDF
│   ├── Vipul Kumar Chobisa - Internship Letter.pdf # Official AFW Internship Letter (2013)
│   └── Vipul kumar Chobisa - Internship Letter - 2014.pdf # Internship Letter (2014)
├── SUMMER TRAINING/                                # Historical Reference Literature & Company Data Archives
│   └── AFW Data/                                   # Reference receipt & stock data (Secured)
├── Report final/                                   # Final thesis sections (Executive Summary, Index)
└── pdf report new/                                 # Consolidated PDF thesis report parts (1.pdf - 5.pdf)
```

---

## Git LFS Tracking Rules

To support high-resolution CAD/TIF renders and binary document formats without bloating Git history, the following extensions are tracked via Git LFS:

```gitattributes
*.xls filter=lfs diff=lfs merge=lfs -text
*.xlsx filter=lfs diff=lfs merge=lfs -text
*.pdf filter=lfs diff=lfs merge=lfs -text
*.ppt filter=lfs diff=lfs merge=lfs -text
*.pptx filter=lfs diff=lfs merge=lfs -text
*.doc filter=lfs diff=lfs merge=lfs -text
*.docx filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
*.tif filter=lfs diff=lfs merge=lfs -text
*.tiff filter=lfs diff=lfs merge=lfs -text
*.jpg filter=lfs diff=lfs merge=lfs -text
*.jpeg filter=lfs diff=lfs merge=lfs -text
*.png filter=lfs diff=lfs merge=lfs -text
*.rtf filter=lfs diff=lfs merge=lfs -text
*.bmp filter=lfs diff=lfs merge=lfs -text
*.gif filter=lfs diff=lfs merge=lfs -text
```

---

## How to Clone & Access

Because this repository utilizes **Git LFS**, ensure `git-lfs` is installed prior to cloning:

```bash
# 1. Install Git LFS (if not already installed)
git lfs install

# 2. Clone the repository with LFS assets
git clone https://github.com/VipulChobisa-AIOps/Smart-Warehouse-Automation-System.git

# 3. Pull LFS binary objects if not fetched automatically
cd Smart-Warehouse-Automation-System
git lfs pull
```
