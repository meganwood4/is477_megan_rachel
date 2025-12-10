# Data Cleaning Process

### Summary

The data cleaning process for this project focused on preparing five separate datasets for integration and visualization. These five datasets including crime data, library locations, park locations, affordable housing data, and neighborhood boundary data, initially had many differences. Because these datasets originated from a few different sources and used inconsistent formats, extensive cleaning and standardization were required before meaningful analysis could occur.

### Chicago Crime Dataset

The crime dataset was first cleaned by removing columns that were not relevant to the project’s goals. These included:

- Case Number
- Block
- IUCR
- Domestic
- Beat
- District
- Ward
- Community Area
- FBI Code
- X Coordinate
- Y Coordinate

Because the crimes dataset was by far our largest dataset, it was important to zone in on the specific data we wanted to look at in our visualizations. 

Then, records missing valid latitude or longitude values were removed to ensure that only entries with valid geometry were used. This step was important because all crime data points eventually would be mapped to specific neighborhoods.

### Libraries Dataset

The libraries dataset also required several cleaning steps before it could be used for analysis. First, unnecessary columns were removed, including:

- PHONE
- WEBSITE
- BRANCH EMAIL

These columns were not relevant to the geography-related goals of the project. 

Also, the geographic coordinates for each library were originally stored inside a single column labeled LOCATION, with both latitude and longitude contained in parentheses as a string. This format could not be used directly for mapping or spatial joins with geopandas. To fix this, the parentheses were removed using string replacement, and the values were split into two separate columns called “LATITUDE”, and “LONGITUDE.” These values were then converted from strings into floating-point numbers so that they could be used to create points later in the project.

### Chicago Park District Facilities Dataset

The parks dataset required fewer changes but still needed important cleaning for consistency. Two unnecessary system-generated columns were removed:

- the_geom
- GISOBJID

These fields were not needed because new geometry would be created using coordinate data. 

Additionally, the coordinate columns were renamed so that they matched the naming convention used across the other datasets. “X_COORD”was renamed to “LONGITUDE,” and “Y_COORD” was renamed to “LATITUDE.”

### Affordable Housing Dataset

The affordable housing dataset required a lot of preprocessing because it was in a different format than the previous datasets. Because the file contained extra header rows and formatting information, only the first 79 rows and relevant columns were retained. The neighborhood name field, labeled “Area,” was cleaned by removing extra whitespace and converting all text to uppercase to ensure consistency with the neighborhoods dataset. Entries labeled “CITY OF CHICAGO” were removed because they did not represent individual neighborhoods and would have caused errors during merging. A new column called PRI_NEIGH was created by reformatting the cleaned neighborhood names into title case to match the naming conventions used in the neighborhood boundaries dataset. Finally, only the following relevant columns were retained:

- PRI_NEIGH
- Total Units
- Total Affordable
- % Affordable

### Neighborhood Boundaries Dataset

The neighborhood boundaries data set also required cleaning. The primary neighborhood name column was cleaned by stripping extra spaces and converting all text to uppercase. This allowed for accurate matching with the cleaned affordable housing dataset. To ensure that both datasets aligned properly, only neighborhoods that existed in both datasets were retained. Finally, the neighborhood boundary geometry was converted into valid geometric objects using the Shapely library.

