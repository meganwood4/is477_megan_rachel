import pandas as pd
import geopandas as gpd
from shapely import wkt
import matplotlib.pyplot as plt
import os

df_crimes = pd.read_csv("data/crimes.csv")
df_crimes = df_crimes.drop(["Case Number", "Block", "IUCR", "Domestic", "Beat", "District", "Ward", "Community Area", "FBI Code", "X Coordinate", "Y Coordinate"], axis=1)
df_crimes = df_crimes[(df_crimes["Latitude"].isna() == False) & (df_crimes["Longitude"].isna() == False)]

df_libraries = pd.read_csv("data/libraries.csv")
df_libraries = df_libraries.drop(["PHONE", "WEBSITE", "BRANCH EMAIL"], axis=1)
df_libraries[['LATITUDE', 'LONGITUDE']] = (df_libraries['LOCATION'].str.replace('[()]', '', regex=True).str.split(',', expand=True))
df_libraries = df_libraries.assign(LATITUDE=df_libraries['LATITUDE'].astype(float),LONGITUDE=df_libraries['LONGITUDE'].astype(float))

df_parks = pd.read_csv("data/parks.csv")
df_parks = df_parks.drop(["the_geom","GISOBJID"], axis=1)
df_parks.rename(columns={"X_COORD":"LONGITUDE","Y_COORD":"LATITUDE"}, inplace=True)

df_affordable_housing = pd.read_excel("data/affordable_housing.xlsx", nrows=79, header=3)

df_neighborhoods = pd.read_csv("data/neighborhoods.csv")

df_affordable_housing["Area_clean"] = df_affordable_housing["Area"].str.strip().str.upper()
df_neighborhoods["PRI_NEIGH_clean"] = df_neighborhoods["PRI_NEIGH"].str.strip().str.upper()
overlap = set(df_affordable_housing["Area_clean"]) & set(df_neighborhoods["PRI_NEIGH_clean"])
df_affordable_housing = df_affordable_housing[df_affordable_housing["Area_clean"].isin(overlap)].copy()
df_neighborhoods = df_neighborhoods[df_neighborhoods["PRI_NEIGH_clean"].isin(overlap)].copy()

df_neighborhoods["geometry"] = df_neighborhoods["the_geom"].apply(wkt.loads)
gdf_neighborhoods = gpd.GeoDataFrame(df_neighborhoods, geometry="geometry", crs="EPSG:4326")
gdf_crimes = gpd.GeoDataFrame(df_crimes, geometry=gpd.points_from_xy(df_crimes.Longitude, df_crimes.Latitude), crs="EPSG:4326")
gdf_libraries = gpd.GeoDataFrame(df_libraries, geometry=gpd.points_from_xy(df_libraries.LONGITUDE, df_libraries.LATITUDE), crs="EPSG:4326")
gdf_parks = gpd.GeoDataFrame(df_parks, geometry=gpd.points_from_xy(df_parks.LONGITUDE, df_parks.LATITUDE), crs="EPSG:4326")

gdf_crimes = gpd.sjoin(gdf_crimes, gdf_neighborhoods[["PRI_NEIGH", "geometry"]], how="left", predicate="within")
gdf_crimes = gdf_crimes[gdf_crimes["PRI_NEIGH"].isna() == False]

gdf_libraries = gpd.sjoin(gdf_libraries, gdf_neighborhoods[["PRI_NEIGH", "geometry"]], how="left", predicate="within")
gdf_libraries = gdf_libraries[gdf_libraries["PRI_NEIGH"].isna() == False]

gdf_parks = gpd.sjoin(gdf_parks, gdf_neighborhoods[["PRI_NEIGH", "geometry"]], how="left", predicate="within")
gdf_parks = gdf_parks[gdf_parks["PRI_NEIGH"].isna() == False]

unique_parks = gdf_parks[['PARK', 'PRI_NEIGH']].drop_duplicates()
parks_per_neighborhood = unique_parks.groupby("PRI_NEIGH").size().reset_index(name="num_parks")

unique_libraries = gdf_libraries[['BRANCH', 'PRI_NEIGH']].drop_duplicates()
libraries_per_neighborhood = unique_libraries.groupby("PRI_NEIGH").size().reset_index(name="num_libraries")

crime_counts = (gdf_crimes.groupby(['PRI_NEIGH', 'Primary Type']).size().reset_index(name='count'))
crime_totals = (crime_counts.groupby("PRI_NEIGH")["count"].sum().reset_index(name="total_crimes"))
crime_types = (crime_counts.pivot(index="PRI_NEIGH", columns="Primary Type", values="count").fillna(0).reset_index())
df_affordable_housing = df_affordable_housing[(df_affordable_housing["Area"].notna()) & (df_affordable_housing["Area"] != "CITY OF CHICAGO")]
df_affordable_housing["PRI_NEIGH"] = df_affordable_housing["Area"].str.strip().str.title()
df_affordable_housing = df_affordable_housing[[
    "PRI_NEIGH",
    "Total Units",
    "Total Affordable",
    "% Affordable"
]].copy()

gdf_neighborhood_final = (
    gdf_neighborhoods[["PRI_NEIGH", "geometry"]]
    .merge(parks_per_neighborhood, on="PRI_NEIGH", how="left")
    .merge(libraries_per_neighborhood, on="PRI_NEIGH", how="left")
    .merge(df_affordable_housing, on="PRI_NEIGH", how="left")
    .merge(crime_totals, on="PRI_NEIGH", how="left")
    .merge(crime_types, on="PRI_NEIGH", how="left")
)

df_neighborhood_final = gdf_neighborhood_final.drop(columns="geometry")

df_neighborhood_final = df_neighborhood_final.fillna(0)
gdf_neighborhood_final = gdf_neighborhood_final.fillna(0)

os.makedirs("graphs", exist_ok=True)

gdf_neighborhood_final.plot(
    column="total_crimes",
    legend=True,
    figsize=(10,10),
    edgecolor="black"
)
plt.title("Total Crimes by Chicago Neighborhood")
plt.savefig("graphs/total_crimes_by_neighborhood.png")
plt.close()

plt.scatter(df_neighborhood_final["num_parks"],df_neighborhood_final["total_crimes"])
plt.xlabel("Number of Parks")
plt.ylabel("Total Crimes")
plt.title("Parks vs. Crime by Neighborhood")
plt.grid(True)
plt.savefig("graphs/parks_vs_crime_by_neighborhood.png")
plt.close()

plt.scatter(df_neighborhood_final["num_libraries"], df_neighborhood_final["total_crimes"])
plt.xlabel("Number of Libraries")
plt.ylabel("Total Crimes")
plt.title("Libraries vs. Crime by Neighborhood")
plt.grid(True)
plt.savefig("graphs/libraries_vs_crime_by_neighborhood.png")
plt.close()

plt.scatter(df_neighborhood_final["% Affordable"], df_neighborhood_final["total_crimes"])
plt.xlabel("Percent of Affordable Housing")
plt.ylabel("Total Crimes")
plt.title("% Affordable Housing vs. Crime by Neighborhood")
plt.grid(True)
plt.savefig("graphs/percent_affordable_vs_crime_by_neighborhood.png")
plt.close()

plt.scatter(df_neighborhood_final["Total Affordable"], df_neighborhood_final["total_crimes"])
plt.xlabel("Total Affordable Housing Units")
plt.ylabel("Total Crimes")
plt.title("Total Affordable Units vs. Crime by Neighborhood")
plt.grid(True)
plt.savefig("graphs/units_affordable_vs_crime_by_neighborhood.png")
plt.close()