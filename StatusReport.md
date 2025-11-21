# Update on Datasets
After attempting to store our original datasets we have decided not to use the following dataset:

### Chicago 311 Service Requests

https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/data_preview

**Reasoning:** When uploading the file into Visual Studio Code, the file appeared to be too big. We tried to stream the data by uploading sections of it instead of downloading the entire dataset at once and creating a smaller time gap, but this process led to the dataset taking over 30 minutes to load. Thus, for efficiency purposes we decided to not use this dataset and look for other datasets that align with our research goal.

### CTA Bus Stops

https://data.cityofchicago.org/Transportation/CTA-Bus-Stops-Shapefile/pxug-u72f/about_data

**Reasoning:** This dataset required Geographic Information System (GIS) software to view and utilize. We, unfortunately, do not have the proper knowledge of GIS software and ultimately decided against using this dataset.

### Chicago Street Centerlines

https://catalog.data.gov/dataset/transportation-2be00

**Reasoning:** This dataset required Geographic Information System (GIS) software to use. We are unfamiliar with this type of software and decide to utilize other dataset instead. 

### Demographic Data

https://www.housingstudies.org/data-portal/browse/?view_as=view-table

Reasoning: While we were able to view this dataset on the website, we were unable to download it and conduct our own analysis. Therefore, we were unable to use this dataset for our research. 

# FAIR Analysis:

### Affordable Housing

https://www.chicago.gov/city/en/depts/dcd/supp_info/citywide-affordable-rental-housing-aalysis.html 

**Findable:** The data is published on the Chicago Data Portal, which is a searchable open-data platform. The dataset for affordable housing is clearly indexed and labeled with description about the metadata. However, the dataset doesn’t have a persistent globally unique identifier like a DOI, which can make it hard for long term citation and automated discovery.

**Accessible:** The data portal supports standard web protocols so the metadata and data are retrievable. Additionally all the information regarding their analysis is openly downloadable. There doesn’t appear to be any restricted access issues, however there wasn’t a detailed license on some of the datasets which could make re-use restrictions unclear. In addition, this makes it unclear if data or metadata has been changed or removed.

**Reusable:** The dataset includes meaningful attributes about affordable housing in Chicago, there is detailed metadata, and is maintained by the City of Chicago. However, the license for re-use isn’t clear and documentation of data collection methods or update frequency are unknown. 

### Chicago Crime Reports:

https://data.cityofchicago.org/stories/s/Crimes-2001-to-present-Dashboard/5cd6-ry5g 

**Findable:** The crime dataset is published in the Chicago Data Portal which is an open-data platform. It is well indexed and contains information about the metadata. However, the dataset does not appear to have a DOI.

**Accessible:** This dataset is able to be retrieved via API and downloading it. The portal follows standard web protocols. Additionally, the platform provides information about when the dataset was last updated and license for usage is clear.

**Reusable:** This data is easily reusable for research and analysis purposes. License is clearly listed however it is unclear whether there are restrictions about if this dataset can be combined with other datasets. Overall, all of the columns provide descriptions and transparency about ownership and update frequency is provided. 

### Chicago Park District Facilities 

https://data.cityofchicago.org/Parks-Recreation/Parks-Chicago-Park-District-Facilities-current-/5yyk-qt9y 

**Findable:** This dataset is available on the Chicago Data Portal. It is easily searchable and columns are well labeled. However, the dataset does not contain a DOI.

**Accessible:** This dataset is able to be retrieved via API or downloaded into various formats like CSV or XLSX. The website provides information about the dataset and when it was last updated in addition to following standard protocols.

**Reusable:** The dataset contains rich, detailed metadata that make it ideal for reuse. However, the license for usage is unclear.

### Libraries

https://data.cityofchicago.org/Education/Libraries-Locations-Contact-Information-and-Usual-/x8fc-8rcq/about_data 

**Findable:** This dataset is published on the Chicago Data Portable which is an open-access platform making it easily findable. The source of the data is clear but DOI for the dataset is not provided.

**Accessible:** The portal follows standard web protocols and the dataset is able to be retrieved via API endpoint or downloaded into various formats. The website provides well documentation about where the data came from, metadata, and when it was last updated.

**Reusable:** The license for usage is linked in the website and contains detailed explanations about the data and metadata, making it ideal for various research goals.

### Neighborhood Boundaries

https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9 

**Findable:** The neighborhood boundaries dataset is published in the open-data platform, Chicago Data Portable. It is easily searchable and findable and contains good descriptions about how to utilize the data outside of the web platform.

**Accessible:** The dataset is able to be downloaded to an API endpoint or in other formats making it extremely accessible. The metadata is easy to interpret and well labeled.

**Reusable:** The usage license is not clearly listed, however this dataset is very versatile in the ways it can be used. There are possibilities to combine this data with other datasets or utilize GIS software for spatial analysis. Additionally, it is transparent about how the data was collected and the accuracy of the data.  

# Updated Timeline

### By each of the following dates we will have…

### Thursday, October 16th:
- Committed our detailed project plan outlining our goals, research questions, team member roles and responsibilities, datasets, project timeline, known constraints, and gaps
    - Completed

### Tuesday, October 21st:
- Analyzed our chosen datasets, ensuring they are accessible and of quality
    - Completed
- Performed a FAIR analysis on the datasets, documenting our findings
    - Completed
- Identified and documented processes to ensure ethical data handling and handle potential constraints
    - Completed

### Tuesday, October 28th:
- Begun the process of cleaning, organizing, and storing our datasets
    - Completed
- Connected our project to a data lifecycle structure
    - Completed

### Tuesday, November 4th:
- Finished the process of cleaning, organizing, and storing our datasets
    - Completed
- Begun working with our data to create visualizations and derive meaningful statistics.
    - In Progress
- Begun the data enrichment, extraction, and integration processes
    - In Progress

### Thursday, November 20th:
- Committed our detailed interim status report, updating our project plan if necessary
    - Completed

### Thursday, December 4th:
- Assessed any necessary changes based on progress and feedback
- Finalize any statsical findings
- Finalized our visualizations and automated process
- Begun our final report of our findings
- Ensured reproducibility and transparency
- Finalized our metadata and documentation

### Wednesday, December 10th: 
- Committed our final report, visualizations, and automated process


# Our Contribution Summaries

### Megan:
My contributions included cleaning, organizing, exploring, and integrating our Chicago datasets. These datasets included crime reports, library locations, park facilities, affordable housing metrics, and neighborhood boundaries. I preprocessed the datasets by removing irrelevant fields, handling missing values, and standardizing formats and naming conventions. I then converted all of the location based datasets into GeoDataFrames and spatially joined the crimes, libraries, and parks with their respective neighborhoods to enable neighborhood-level comparisons. From these new datasets, I began some initial exploratory data analysis. Moving forward, we will be able to use these datasets to create meaningful statistics and visualizations in order to support inference and answer our research questions. 

### Rachel:

