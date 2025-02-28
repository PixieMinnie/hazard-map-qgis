# hazard-map-qgis
# Hazard Map for Debris Flow and Landslide Risk Assessment

## Overview
This project involves a **hazard map** developed in **QGIS** to assess debris flow and landslide risks. It utilizes elevation data, rainfall records, and historical landslide occurrences to analyze terrain susceptibility to mass movement. The project aligns with climate change impact studies, particularly in alpine regions like the Swiss Alps.

## Data Sources
The analysis is based on the following datasets:
- **Digital Elevation Model (DEM)**: [SRTM data]
- **Landslide Inventory**: [USGS Global Landslide Catalog]
- **Climate Data**: [CH2018]

## Methodology
1. **Data Preprocessing**
   - Loaded DEM and landslide inventory in QGIS.
   - Reprojected data to an appropriate CRS.
   - Conducted raster and vector data cleaning.

2. **Terrain Analysis**
   - Computed **slope, aspect, and curvature** from DEM.

3. **Hazard Mapping**
   - Combined **landslide occurrences with topographic factors**.
   - Used **weighted overlay** (slope, precipitation, lithology) to create a susceptibility index.

4. **Visualization & Export**
   - Styled the hazard map using QGIS **categorization and symbology**.
   - Exported final raster and vector layers.
   - Created **Python scripts** for automated analysis (available in repository).

## Results & Applications
- The final hazard map highlights **high-risk zones** for debris flows and landslides.
- Can be integrated with climate projections to study future hazard evolution.
- Useful for **risk assessment, infrastructure planning, and climate adaptation strategies**.

## Repository Structure
```
/qgis_hazard_map
├── data/  # Raw and processed datasets (not included in repo due to size)
├── scripts/  # Python scripts for data analysis & modeling
├── qgis_project.qgz  # Main QGIS project file
└── README.md  # This document
```

## Future Enhancements
- **Integration with Machine Learning** to refine hazard predictions.
- **Enhanced climate impact analysis** using dynamic projections.
- **Web-based visualization** for stakeholder engagement.

---
### Author
**Minal Londhe**  
Expertise: Climate Analyst | Engineering Geology | Python for Geospatial Analysis  


