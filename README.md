# Urban Planning and Crime

### Contributors: 
- Megan Wood
- Rachel Li

### Summary
In this project, we sought to understand how different aspects of urban infrastructures and housing demographics correlate with crime patterns across the city of Chicago. Our central goal was to examine measurable relationships between environmental factors such as access to public park facilities and libraries, the distribution of affordable housing units, and neighborhood boundary characteristics in relation to both the amount and types of crime committed in those areas. By studying these structural and social patterns, we aimed to uncover data-driven insight that can encourage safer, more equitable urban design and development. Cities are built on complex social and physical systems, and our research focuses on how particular features of the built environment may unintentionally encourage, reduce, or redistribute criminal activity.

Urban planners, community developers, and policymakers often make decisions that indirectly influence public safety indirectly through zoning laws, public infrastructure funding, and patterns of community investment. However, many of these decisions are not rooted in quantitative assessments of how people interact with public spaces or how neighborhood design may shape levels of risk. For example, accessible green spaces and well-maintained public libraries can function as community anchors that foster shared norms of social responsibility that can reduce crimes. On the other hand, zoning decisions that create sharp socioeconomic boundaries or disproportionately concentrate affordable housing in certain districts may contribute to an uneven distribution of opportunities, policing, and social tension. Our project seeks to address this by applying data science techniques to evaluate how specific characteristics of Chicago’s infrastructure relate to where and when crimes occur. Ultimately our research asks whether the physical and demographic landscape of Chicago helps protect residents or inadvertently puts certain communities at greater risk.

Our personal motivation for studying this topic is rooted in our experience growing up in Chicago. As residents, we have witnessed how conversations about public safety often overshadow discussions about structural inequality, resource allocation, and long-term urban development. Crime can feel like a result of individual actions, yet it is deeply connected to environmental conditions shaped by decades of policy decisions. As crime continues to be discussed as an urgent issue in neighborhoods across Chicago, we are curious about more than just the statistics. We would like to investigate underlying factors that shape these patterns and explore how proactive design can alleviate them. Our shared familiarity with Chicago’s diverse communities, from its complex history of urban development to socioeconomic disparities, makes this research personally meaningful.

Chicago is also an ideal setting for this kind of analysis due to its rich and publicly available data resources, and its distinct neighborhood histories. The city showcases clear patterns of socioeconomic segregation and public facility access– conditions that are crucial in studying how infrastructure affects crime. Chicago's unique combination of dense urban planning, community assets, and historical zoning practices offers a rich context for identifying statistically significant patterns. Although our analysis focuses on Chicago, the methods we employ could be replicated in other metropolitan areas. Insights from this study may serve as a model for understanding how urban design influences crime in other cities facing similar challenges.

Our overarching research question is: How is urban infrastructure related to crime rates and types in the city of Chicago? Within this central question, we aim to understand how the physical layout of Chicago and its housing demographics shape where, when, and how crime occurs. To develop a clearer picture, we break this into several more specific questions. These include: Are areas with higher concentrations of affordable housing associated with higher or lower rates specific types of crimes? Affordable housing can act as a stabilizing force by providing long-term residence, as well as be correlated with higher policing presence and inequality, depending on surrounding conditions. We also wonder: Are areas with higher access to public facilities more or less susceptible to crimes? These facilities can increase foot traffic and create a sense of community, but they may also attract crime depending on how facilities are utilized, maintained, and monitored.

Our overall finding is that the physical infrastructures we examined do not show a meaningful correlation with either higher or lower crime rates. Moreover, none of these infrastructures appear to cause crime. When we analyzed the number of libraries, number of parks, the percentage of affordable housing, and number of affordable housing units in relation to crime rates, we generally did not observe strong or consistent correlations. The only visualization that displayed a noticeable positive linear relationship was between the number of affordable housing units to crime. This pattern likely reflects the fact that neighborhoods with more housing units tend to be larger and therefore have more total crime because they contain more residents. Similarly, although we observed higher crime counts in areas with more public facilities, this does not indicate that these facilities contribute to crime. Instead, when considering all the variables together, our findings suggest that underlying factors such as population density, higher foot traffic, and differences in maintenance or surveillance across neighborhoods are more plausible explanations for the observed patterns.

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

