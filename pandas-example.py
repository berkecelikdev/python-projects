import pandas as pd

ad_clicks = pd.read_csv("ad_clicks.csv")
print(ad_clicks.head())
print("----------------------------")

print(ad_clicks.groupby(["utm_source"]).user_id.count().reset_index()) # How many IDs clicked on each source
print("----------------------------")

ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index() # Click control and count for source.
print(clicks_by_source)
print("----------------------------")

clicks_pivot = clicks_by_source.pivot( # pivot table
    columns = "is_click",
    index = "utm_source",
    values = "user_id").reset_index()
print(clicks_pivot)
print("----------------------------")

clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) # click rate pivot table
print(clicks_pivot)
print("----------------------------")

print(ad_clicks.groupby("experimental_group").user_id.count().reset_index()) # Number of IDs in groups
print("----------------------------")

print(ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index().pivot(  # Click control in groups
    index = "experimental_group",
    columns = "is_click",
    values = "user_id").reset_index())
print("----------------------------")

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"] # Only group A is listed
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"] # Only group B is listed

a_clicks_pivot = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot( # Group A clicklist
    index = "day",
    columns = "is_click",
    values = "user_id").reset_index()

a_clicks_pivot["percent_clicked"] = a_clicks_pivot[True] / a_clicks_pivot[True] + a_clicks_pivot[False] # click rate table
print(a_clicks_pivot)
print("----------------------------")

b_clicks_pivot = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot( # Group B clicklist
    index = "day",
    columns = "is_click",
    values = "user_id").reset_index()

b_clicks_pivot["percent_clicked"] = b_clicks_pivot[True] / b_clicks_pivot[True] + b_clicks_pivot[False] # click rate table
print(b_clicks_pivot)

