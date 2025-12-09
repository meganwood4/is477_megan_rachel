rule all:
    input:
        "graphs/total_crimes_by_neighborhood.png",
        "graphs/parks_vs_crime_by_neighborhood.png",
        "graphs/libraries_vs_crime_by_neighborhood.png",
        "graphs/percent_affordable_vs_crime_by_neighborhood.png",
        "graphs/units_affordable_vs_crime_by_neighborhood.png"

rule run_final_project:
    input:
        crimes="data/crimes.csv",
        libraries="data/libraries.csv",
        parks="data/parks.csv",
        housing="data/affordable_housing.xlsx",
        neighborhoods="data/neighborhoods.csv",
        script="final_project.py"
    output:
        "graphs/total_crimes_by_neighborhood.png",
        "graphs/parks_vs_crime_by_neighborhood.png",
        "graphs/libraries_vs_crime_by_neighborhood.png",
        "graphs/percent_affordable_vs_crime_by_neighborhood.png",
        "graphs/units_affordable_vs_crime_by_neighborhood.png"
    shell:
        "python final_project.py"

