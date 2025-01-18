# A construction company is launching a housing scheme in latifabad , Hyderabad , and before launching a scheme the CEO wants to know what is the market of houses in latifabad , and for that purpose , the CEO of company comes to Arham who is Data analyst to collect the data of houses in latifabad and perform analysis and give me insights so I can develop a scheme according to the market,
# now Arham collect the houses data and store it in a dictionary and the data look something like this

'''
MinimumPricePerSqftThreshold: 1500 , MaximumPricePerSqftThreshold : 4000
create another key value pair of pricepersqft: [values]
remove all the houses data which are not in range of pricepersqftthreshold
Extract data of most expensive house
Extract data of most cheap house
If certain house has 2 rooms so it is mandadtory that it contain 2 washrooms not less not more , remove all the data which did not meet that requirement
'''
MinimumPricePerSqftThreshold=1500 
MaximumPricePerSqftThreshold = 4000

data={
    "AreaSqft":[1200,900.4500,2000,3500,4500,4000,600,700,100,1850,900,1000,1500,1400],
    "PriceInLac": [45,35,80,22,35,65,80,70,20,30,100,65,35,58,55],
    "Bedrooms": [2,3,2,3,2,3,2,3,2,3,2,3,2,4,2],
    "Bathrooms":[2,3,5,2,2,3,4,2,3,2,3,2,3,4,2]
}
print("Data Analysis ----> Start\n")

print("New columns Absolute price is added\n")
data["absolute_price"]=[i*100000 for i in data["PriceInLac"]]
print(data)

print("\nNew column Price Per sqft added\n")
data["PricePerSqrtFt"]=[(round(data["absolute_price"][i]/data['AreaSqft'][i],2)) for i in range(len(data["AreaSqft"]))]
print(data)

h=[data['PricePerSqrtFt'].index(i) for i in data["PricePerSqrtFt"] if i< MinimumPricePerSqftThreshold or i> MaximumPricePerSqftThreshold]
    
print(data)
print("\nData Analysis ----> Completed\n")