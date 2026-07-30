
import pandas
data=pandas.read_csv("squirrel_data.csv")
gray_squ=len(data[data["Primary Fur Color"]=="Gray"])
red_squ=len(data[data["Primary Fur Color"]=="Cinnamon"])
blk_squ=len(data[data["Primary Fur Color"]=="Black"])
print("Grey Squirrel:",gray_squ)
print("red Squirrel:",red_squ)
print("black Squirrel:",blk_squ)
data_dict={
    "Primary Fur Color":["Gray","Cinnamon","Black"],
    "count":[gray_squ,red_squ,blk_squ]
}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

