import pandas as pd

#_ READING & CONVERTING TO LIST

df = pd.read_csv("weatherdata.csv")
# print(df['temp'])

# df.to_dict()

# temp_list = df['temp'].to_list()

# # MEAN

# avg = sum(temp_list)/len(temp_list)
# print(avg)

# print(df.mean(numeric_only=True))


# print(df['temp'].max())

# print(df.temp)
monday = df[df.day =="Monday"]
print(monday['temp'][0])

data_dict = {
    
    "students" :["Ammy","James","angela"],
    "scores":[76,56,15]
}