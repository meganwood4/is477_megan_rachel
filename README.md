# Urban Planning and Crime

### Contributors: 
- Megan Wood

My contributions for the final leg of this project primarily focused on implementing the full Python data pipeline, including final data cleaning, dataset integration, merging and aggregating the datasets, and the creation of all visualizations. I then documented the data cleaning and integration processes and wrote explanations and conclusions for each of the visualizations. Finally, I created the project’s DCAT metadata file, the requirements.txt file, and the Snakefile for workflow automation.

- Rachel Li

My contributions for wrapping up this project included analyzing the data and visualizations, and writing the project report. I wrote a comprehensive summary of our overall project, motivations, findings, and an analysis of all our datasets used. Additionally, Using the visualizations made by Megan, I concluded our findings that helped shaped our reflection of the project and ideas for future work.

# Summary
In this project, we sought to understand how different aspects of urban infrastructures and housing demographics correlate with crime patterns across the city of Chicago. Our central goal was to examine measurable relationships between environmental factors such as access to public park facilities and libraries, the distribution of affordable housing units, and neighborhood boundary characteristics in relation to both the amount and types of crime committed in those areas. By studying these structural and social patterns, we aimed to uncover data-driven insight that can encourage safer, more equitable urban design and development. Cities are built on complex social and physical systems, and our research focuses on how particular features of the built environment may unintentionally encourage, reduce, or redistribute criminal activity.

Urban planners, community developers, and policymakers often make decisions that indirectly influence public safety indirectly through zoning laws, public infrastructure funding, and patterns of community investment. However, many of these decisions are not rooted in quantitative assessments of how people interact with public spaces or how neighborhood design may shape levels of risk. For example, accessible green spaces and well-maintained public libraries can function as community anchors that foster shared norms of social responsibility that can reduce crimes. On the other hand, zoning decisions that create sharp socioeconomic boundaries or disproportionately concentrate affordable housing in certain districts may contribute to an uneven distribution of opportunities, policing, and social tension. Our project seeks to address this by applying data science techniques to evaluate how specific characteristics of Chicago’s infrastructure relate to where and when crimes occur. Ultimately our research asks whether the physical and demographic landscape of Chicago helps protect residents or inadvertently puts certain communities at greater risk.

Our personal motivation for studying this topic is rooted in our experience growing up in Chicago. As residents, we have witnessed how conversations about public safety often overshadow discussions about structural inequality, resource allocation, and long-term urban development. Crime can feel like a result of individual actions, yet it is deeply connected to environmental conditions shaped by decades of policy decisions. As crime continues to be discussed as an urgent issue in neighborhoods across Chicago, we are curious about more than just the statistics. We would like to investigate underlying factors that shape these patterns and explore how proactive design can alleviate them. Our shared familiarity with Chicago’s diverse communities, from its complex history of urban development to socioeconomic disparities, makes this research personally meaningful.

Chicago is also an ideal setting for this kind of analysis due to its rich and publicly available data resources, and its distinct neighborhood histories. The city showcases clear patterns of socioeconomic segregation and public facility access– conditions that are crucial in studying how infrastructure affects crime. Chicago's unique combination of dense urban planning, community assets, and historical zoning practices offers a rich context for identifying statistically significant patterns. Although our analysis focuses on Chicago, the methods we employ could be replicated in other metropolitan areas. Insights from this study may serve as a model for understanding how urban design influences crime in other cities facing similar challenges.

Our overarching research question is: **How is urban infrastructure related to crime rates and types in the city of Chicago?** Within this central question, we aim to understand how the physical layout of Chicago and its housing demographics shape where, when, and how crime occurs. To develop a clearer picture, we break this into several more specific questions. These include: _Are areas with higher concentrations of affordable housing associated with higher or lower rates specific types of crimes?_ Affordable housing can act as a stabilizing force by providing long-term residence, as well as be correlated with higher policing presence and inequality, depending on surrounding conditions. We also wonder: _Are areas with higher access to public facilities more or less susceptible to crimes?_ These facilities can increase foot traffic and create a sense of community, but they may also attract crime depending on how facilities are utilized, maintained, and monitored.

Our overall finding is that the physical infrastructures we examined do not show a meaningful correlation with either higher or lower crime rates. Moreover, none of these infrastructures appear to cause crime. When we analyzed the number of libraries, number of parks, the percentage of affordable housing, and number of affordable housing units in relation to crime rates, we generally did not observe strong or consistent correlations. The only visualization that displayed a noticeable positive linear relationship was between the number of affordable housing units to crime. This pattern likely reflects the fact that neighborhoods with more housing units tend to be larger and therefore have more total crime because they contain more residents. Similarly, although we observed higher crime counts in areas with more public facilities, this does not indicate that these facilities contribute to crime. Instead, when considering all the variables together, our findings suggest that underlying factors such as population density, higher foot traffic, and differences in maintenance or surveillance across neighborhoods are more plausible explanations for the observed patterns.

# Data Profile

This project integrates several publicly available datasets from the Chicago Data Portal, an open-data platform maintained by the city of Chicago. These datasets support a wide range of civic, academic, and policy research and are updated regularly depending on the data provider. The following section will summarize each dataset used in this project, describe what information each dataset contains, and identify relevant ethical and legal considerations associated with their use.

- Affordable Housing Dataset
- https://www.chicago.gov/city/en/depts/dcd/supp_info/citywide-affordable-rental-housing-aalysis.html 

This dataset provides comprehensive data about affordable rental housing developments across Chicago. It includes information such as the types and number of affordable housing units in different neighborhoods. This information makes it possible to analyze the distribution and scale of affordable housing across all neighborhoods in Chicago.

In terms of the legal constraints, the dataset is publicly accessible and intended for civic use. However, it does not provide a clear, formal usage license. This means that while the dataset is openly published, it is not fully explicit about restrictions or allowances for redistribution or derivative works. Ethically, the data poses minimal risk since it only contains the total and percentage of affordable housing units in the neighborhood rather than personal resident data. However, because affordable housing carries social stigma in some contexts, researchers must take this into account and avoid interpreting or presenting the data in ways that inadvertently reinforce negative stereotypes about neighborhoods with higher concentrations of affordable housing.

- Chicago Crime Dataset
- https://data.cityofchicago.org/stories/s/Crimes-2001-to-present-Dashboard/5cd6-ry5g 

This dataset contains incident-level reports of crimes recorded by the Chicago Police Department, spanning more than two decades. The dataset includes fields such as the type of crime, date and time of the incident, location details, and case number. Because of its size and level of detail, it is a foundational dataset for criminology and public-safety related studies in Chicago.

Ethically and legally, this dataset requires careful consideration. Although all personally identifiable information is removed, crime data has the potential to reinforce harmful narratives about certain communities. Therefore, researchers must contextualize analyses and avoid oversimplified conclusions when using this dataset. The dataset is openly licensed however it is unclear whether there are restrictions about if this dataset can be combined with other datasets. Still, because reported crimes reflect both policing practices and crime rates, it is important to acknowledge potential systemic biases inherent in the data.

- Chicago Park District Facilities Dataset
- https://data.cityofchicago.org/Parks-Recreation/Parks-Chicago-Park-District-Facilities-current-/5yyk-qt9y 

This dataset contains information about parks and recreational facilities managed by the Chicago Park District. It includes fields such as park names, locations, facility attributes, amenities, and operating details. This data makes it possible to analyze the distribution of recreational resources across neighborhoods and explore potential relationships between access to public facilities and community health and safety outcomes.

While the dataset is publicly accessible and contains no sensitive personal data, its licensing terms are not explicitly stated. This lack of clarity does not prevent academic use but may limit reuse in commercial or redistributed contexts. Ethically, this dataset is considered low risk since it concerns public facilities rather than individuals. However, when interpreted alongside crime data, it is important to avoid implying that the presence or absence of facilities directly causes social outcomes without sufficient evidence.

- Libraries Dataset
- https://data.cityofchicago.org/Education/Libraries-Locations-Contact-Information-and-Usual-/x8fc-8rcq/about_data 

This dataset provides detailed information about Chicago Public Library branches including their locations, contact details, hours, and neighborhood placement. It is well documented and includes clear information about how the data is maintained and updated. 

Since libraries are public institutions, the dataset carries no privacy risks. The portal includes a dedicated usage license, reducing legal ambiguity and supporting broader reuse. The data is useful for examining spatial relationships between library access, neighborhood infrastructure, and social indicators such as crime or economic development. However, it is still important to avoid overinterpreting correlations without accounting for broader context.

- Neighborhood Boundaries Dataset
- https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9 

This dataset provides official geographic boundaries for Chicago’s neighborhoods. It includes geospatial metadata that allows researchers to map infrastructure and crime data to specific neighborhoods. Because neighborhood boundaries are widely used across academic and municipal planning contexts, this dataset is foundational for spatial analysis and aggregation of the other datasets used in this project.

Legally, the dataset is openly published but it does not explicitly state licensing details. Ethically, the data itself poses no risk but analyses that map sensitive datasets, like crime reports, onto neighborhood boundaries must be conducted responsibly. Spatial aggregation can reinforce stereotypes about communities if not contextualized within socioeconomic, demographic, and structural factors.

# Obtaining Datasets

To obtain the datasets we used throughout the project, they can be accessed through the links and then either downloaded into various formats or through API key. We chose to download the datasets rather than using API since the Chicago datasets were massive due to the extensive detail and amount of data collected throughout the years. Therefore, we had to download and clean the datasets to filter out irrelevant data for our project. This data can be viewed in our GitHub repository under the ‘data’ folder and in our Box folder.

Box link: https://uofi.box.com/s/p9a3i4fpm6a1ufodlp61uzyu2q80q6ee
Github link: https://github.com/meganwood4/is477_megan_rachel.git

### Data Quality

Assessing data quality is essential for determining the validity of our results, especially given the diversity of datasets used in this project. Because our research examines relationships between crime and forms of urban infrastructure including parks, libraries, affordable housing units, and neighborhood boundaries, we evaluated each dataset in terms of completeness, accuracy, consistency, temporal relevance, and potential sources of bias.

- Affordable Housing Dataset

The affordable housing dataset provides a comprehensive list of affordable rental properties across Chicago, including the number of affordable units within each building. In general, this dataset is complete with respect to property-level attributes, but it has several limitations. First, update frequency is not explicitly stated, which raises concerns about whether newly built or demolished properties are fully reflected. Some fields contained extra white spaces and unstandardized capitalizations. Despite these limitations, the dataset is consistent in structure and numerical fields (such as unit counts) that appeared reliable. The largest bias risk comes from the dataset's scope. It includes only developments formally recognized by the City of Chicago and may overlook informal or unregistered affordable housing arrangements, potentially underestimating the actual affordable housing landscape.

- Chicago Crime Reports Dataset

The crime dataset is one of the most robust sources, with millions of incident-level records spanning over two decades. It is updated frequently and includes detailed attributes such as crime type, date/time, location, and case number. However, crime data inherently reflects police activity, not strictly the occurrence of crime. Neighborhoods with higher police presence may show artificially inflated crime counts simply because more incidents are detected and reported. Additionally, missing values are rare but do appear in certain locations or secondary description fields. Overall, the dataset is reliable for analysis, but we must also acknowledge that crime reports measure both actual events and patterns of enforcement.

- Chicago Park District Facilities Dataset

This dataset was relatively small, containing only dozens or hundreds of records. It is easy to work with and contains well-organized metadata. It includes facility characteristics, amenities, and geographic placement. Therefore, this dataset shows high completeness and low likelihood of error. Their main limitation is the lack of context due to only containing information relating to its locations and amenities. It would be helpful if the dataset included information about facility quality, usage rates, open hours, or on-site surveillance since these factors could meaningfully influence crime patterns. Thus, while facility presence is accurately recorded, it may not fully reflect real-world accessibility or community engagement.

- Libraries Datasets

This dataset was also pretty small but contained well documented metadata. It includes information on branch type, hours, contact information, and location. There were little to no standardization errors and overall a well-rounded dataset. However, given that this dataset only contains information about the location and contact information, it would be even more useful if data about the facility usage or surveillance information was included as well– for our project specifically. Overall, this was a useful dataset to see a wider range of public amenities in relation to crime rates.

- Neighborhood Boundaries Dataset

The neighborhood boundaries dataset is widely used across research and municipal planning. It includes accurate and regularly maintained shapefiles representing the city’s community areas. Because nearly all Chicago datasets use community area boundaries for aggregation, this dataset provides a consistent spatial framework. Its quality is high, but there are still some constraints. Neighborhoods are treated as uniform spatial units which can cause complications when paired with crime locations. Therefore, this spatial generalization is the dataset’s primary limitation. Taken together, the datasets are of generally high quality and suitable for macro-level analysis. 

### Findings

Our overarching question of “How is urban infrastructure related to crime rates and types in Chicago?” guided a set of analyses combining infrastructure datasets with crime data. The analysis revealed that the relationship between Chicago’s urban infrastructure and crime rates is far more complex than simple correlations might suggest. When looking across neighborhoods, we found that the presence or density of libraries, parks, and affordable housing, whether measured by percentage or unit count, did not reliably predict higher or lower levels of crime. 

When examining public facilities such as libraries, we did not observe any consistent pattern between the number of libraries in a neighborhood and the total crime count. Some neighborhoods with multiple libraries reported high crime, while others reported low crime, and the same variability was present in neighborhoods with few or no libraries. The distribution was broad and scattered, and overall showed no linear or nonlinear tendency. Parks exhibited a similarly inconsistent relationship. Despite expectations that parks might either reduce crime by increasing positive community presence or increase crime by attracting loitering, no clear trend emerged in either direction. Crime levels varied widely among neighborhoods regardless of how many park facilities they contained.

Affordable housing, measured as the percentage of units designated affordable within each neighborhood, also did not show a clear connection to crime rates. Neighborhoods with high proportions of affordable housing sometimes had low crime levels, while some neighborhoods with low proportions had much higher crime. There was no meaningful pattern suggesting that affordable housing concentration either encourages or mitigates crime. In this respect, the data challenge common assumptions that affordable housing drives certain types of neighborhood outcomes.

The only variable that showed a visibly stronger relationship with crime was the total number of affordable housing units. Neighborhoods with more affordable units generally had higher total crime counts. At first glance this might appear to suggest a correlation, but considering the results of the other variables’ analysis, it strongly indicates that this relationship is driven not by affordable housing itself but by the size and overall density of the neighborhood. Areas with more total units tend to be larger and more populated. Because crime is typically measured as an absolute count rather than as a rate, neighborhoods with more residents naturally accumulate more total crime incidents. This suggests that the correlation between affordable housing unit count and crime arises from scale effects rather than from any causal relationship.

These findings point toward a broader interpretive conclusion that the urban features examined in this project, libraries, parks, affordable housing percentages, and affordable unit counts, are not strong predictors of crime outcomes in Chicago. Instead, underlying contextual factors seem to exert greater influence. Population density, neighborhood size, levels of commercial activity, socioeconomic inequality, policing activity, and community stability likely play much more substantial roles in determining where and how crime arises. In other words, the infrastructures we analyzed are embedded within larger systems of urban dynamics, and any observed associations are likely mediated by these underlying structural forces rather than caused directly by infrastructure itself.

However, there are a few limitations in the data and method that may partially obscure more subtle relationships. Because the analysis was conducted at the neighborhood level, it may overlook finer spatial patterns that occur at the block or street level. It also does not incorporate temporal changes such as the construction of new facilities or shifts in population that might reveal lagged effects. Moreover, factors such as the condition, usage frequency, and maintenance of public facilities are not captured in the datasets, nor are policing levels or reporting behaviors, all of which can largely influence crime data. Without socioeconomic variables like income or unemployment, the analysis cannot fully account for underlying factors.

Despite these limitations, the overall result remains clear. The infrastructures studied do not show meaningful or consistent correlations with crime, and none of them appear to cause crime. The observable patterns are better explained by population size, neighborhood density, and other contextual forces. These findings therefore reinforce the idea that crime in urban settings is shaped by multifaceted social and structural dynamics, rather than by the presence or absence of public facilities or affordable housing.

### Future Work

While our project provides valuable insights, it also reveals several limitations and opportunities for deeper research. Throughout this project, we learned that our research lacks the scale and results that accounts for all the underlying factors that influence crime. However, conducting this research was still beneficial in the sense that we can rule out the idea that the presence of physical infrastructures impacts crime rates. This creates a stepping stone for future work that can expand on the amount and types of factors to pinpoint what variables influence crimes. Therefore, here are several ideas for future work that could produce more robust and actionable findings.

1. Incorporating population and demographic variables

A major limitation of our current analysis is that it does not explicitly control for population or demographic factors. Demographics and population density are factors we did not consider while conducting our analysis, but discovered is essential to consider when connecting crime rates and underlying factors. Future work could incorporate socioeconomic indicators such as income, unemployment rates, racial segregation, and education levels– which could help show how infrastructure interacts with existing structural inequalities to shape crime patterns.

2. Examine infrastructure quality, not just presence

The datasets we used only track the existence of facilities, such as parks and libraries, not their condition, hours of operation, staffing, programming, or safety features. We discovered that these attributes could play a crucial role in interpreting our current findings. Future research could integrate new datasets or field observations that capture the quality and usability of infrastructure. For example, parks with high-quality lighting and frequent programming may deter crime, whereas neglected parks may attract it.

3. Improving the affordable housing analysis.

Affordable housing is complex and multifaceted. Given our dataset focuses only on formally designated affordable units, this limits our ability to accurately reflect our data to reality. Future research could build a more complete housing profile by adding eviction data, data on naturally occurring affordable housing, building code violations, and rental market dynamics. This could allow for a more comprehensive evaluation of how housing stability relates to crime.

4. Combining qualitative and quantitative methods

While we used quantitative data, this cannot fully capture lived experiences. The data we used is the data that is reported, meaning some details could have gone unnoticed. Interviews with community members, urban planners, librarians, crime-prevention specialists, or affordable housing residents could provide context that the numbers alone cannot. This mixed-methods approach would help interpret ambiguous findings and highlight community priorities.

5. Machine learning or statistical modeling

For this project, we utilized basic data analysis and visualizations to gather findings. However, future work could move beyond scatterplots to more sophisticated models like regressions, clustering, and random forests to identify multivariate relationships. Such models may uncover hidden patterns or interactions between datasets that are not visible through descriptive visualizations alone.

6. Ethical considerations and community impact

Finally, future work must continue to address ethical considerations. As mentioned in previous sections, crime data is deeply intertwined with histories of over-policing and racialized surveillance. In further research studies, researchers could adopt frameworks such as data justice or community centered data ethics to ensure that the work does not reinforce harmful stereotypes. Future work could also integrate community-led datasets or participatory mapping to produce findings that better reflect neighborhood realities.

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

# Data Integration Process

The data integration process for this project focused on combining multiple cleaned datasets into a single, unified dataset that could support neighborhood-level analysis. After each dataset was independently cleaned and standardized as described above, geographic relationships were used as the basis for integrating crime data, library locations, park locations, affordable housing information, and neighborhood boundaries.

The first step in the integration process involved converting all of the cleaned DataFrames into GeoDataFrames. The crime, library, and park datasets were each transformed from traditional DataFrames into GeoDataFrames by creating point geometries from their latitude and longitude coordinates. The neighborhoods dataset was already structured with polygon geometries representing the boundaries of each neighborhood. All GeoDataFrames were assigned the same coordinate reference system (EPSG:4326), ensuring that every dataset aligned correctly in geographic space. 
Once the datasets shared the same spatial reference system, spatial joins were performed to assign each point-based observation to a specific neighborhood. Each crime incident was matched to the neighborhood polygon in which it occurred, and any crimes that did not fall within a neighborhood boundary were removed to avoid inaccuracies. The same process was repeated for both libraries and parks, allowing each of these locations to be associated with a specific neighborhood. This step was critical to our project because it transformed raw point-based geographic data into neighborhood-level information that could be aggregated and compared.

After the spatial joins were completed, aggregation was performed to summarize data at the neighborhood level. For the parks dataset, duplicate park names within the same neighborhood were dropped before grouping to prevent overcounting. Then, the number of unique parks per neighborhood was calculated. A similar process was used for libraries, where unique branches were identified and counted within each neighborhood. 
Crime data integration involved grouping incidents by both neighborhood and crime type. First, total crime counts were calculated for each neighborhood by summing all crime occurrences. Then, a pivot table was created to transform individual crime types into separate columns, allowing crime patterns to be compared across neighborhoods in a structured format. This produced both an overall crime measure and a detailed breakdown of crime categories.

The affordable housing dataset was integrated using a traditional data merge rather than a spatial join. After neighborhood names were standardized during the cleaning phase, affordable housing data was merged into the main dataset using the neighborhood name as the common key. This allowed housing unit totals, affordable unit counts, and percent affordability to be directly compared against crime rates and public resource availability.

Finally, all integrated datasets were merged into a single master GeoDataFrame that contained neighborhood geometry, public resource counts, housing data, and crime statistics so that a spatial visualization could be created. Any remaining missing values were filled with zeros to ensure consistency and prevent errors during visualization. This fully integrated dataset served as the backbone of the project’s analytical workflow, supporting both the geographic maps and the statistical scatter plots used to explore relationships between crime and city infrastructure.

# Understanding our Data Visualizations

### 1. Total Crimes by Chicago Neighborhood

This map visualizes the spatial distribution of total crime across neighborhoods. Higher crime concentrations appear clustered in specific areas, showing that crime is unevenly distributed across the city.
   
### 2. Parks vs. Crime by Neighborhood
  
This scatter plot compares the number of parks to total crime across neighborhoods. There is a weak positive relationship, and some neighborhoods with many parks also show high crime, suggesting that park presence is not the only factor that has impact on crime levels.

### 3. Libraries vs. Crime by Neighborhood

This scatter plot shows the relationship between the number of public libraries and total crime in each neighborhood. While neighborhoods with more libraries tend to have higher crime totals, this is likely influenced by population density rather than indicating that libraries increase crime.

### 4. % Affordable Housing vs. Crime by Neighborhood

This scatter plot shows how the percentage of affordable housing relates to total crime across neighborhoods. The wide spread of points shows little relationship, indicating that percent affordability does not have a large correlation with crime.

### 5. Total Affordable Units vs. Crime by Neighborhood

This scatter plot compares the total number of affordable housing units to total crime across neighborhoods. There is a positive linear relationship, suggesting that neighborhoods with more affordable units often have higher crime totals.

# Workflow Automation and Provenance

To ensure reproducibility and automation, this project used a Snakemake workflow to manage the full data processing and visualization pipeline. The Snakefile was configured to track all raw input datasets and automatically execute the final_project.py script whenever inputs changed (although we don't predict input changes being necessary). It also defined the five output graphs as targets, allowing Snakemake to verify successful execution and prevent unnecessary reruns.

# References

City of Chicago/Chicago Data Portal. (n.d.). _Boundaries - Neighborhoods._ https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9

City of Chicago/Chicago Data Portal. (n.d.). _Citywide Affordable Rental Housing Analysis._ https://www.chicago.gov/city/en/depts/dcd/supp_info/citywide-affordable-rental-housing-aalysis.html

City of Chicago/Chicago Data Portal. (n.d.). _Crimes - 2001 to Present._ https://data.cityofchicago.org/stories/s/Crimes-2001-to-present-Dashboard/5cd6-ry5g

City of Chicago/Chicago Data Portal. (n.d.). _Parks - Chicago Park District Facilities (current)._ https://data.cityofchicago.org/Parks-Recreation/Parks-Chicago-Park-District-Facilities-current-/5yyk-qt9y

City of Chicago/Chicago Public Library. (n.d.). _Libraries - Locations, Contact Information, and Usual Hours of Operation._ https://data.cityofchicago.org/Education/Libraries-Locations-Contact-Information-and-Usual-/x8fc-8rcq

