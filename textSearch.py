from pyspark import SparkConf, SparkContext #imports the functionality of the session, text
from pyspark.sql import SparkSession #imports the functionality of the session for sql
from pyspark.sql import Row #imports the ability to do pre-defined rows in sql
from pyspark.sql.functions import col #imports the ability to do pre-defined columns in sql
spark = SparkSession \ #defining spark with SparkSession / .builder / .appName / .getOrCreate()
    .builder \
    .appName("Spark Example") \
    .getOrCreate()
conf = SparkConf().setMaster("local").setAppName("textSearch") #defining conf, setting the name of the application file
sc = SparkContext.getOrCreate() #creating object SparkContext.getOrCreate()
textFile = sc.textFile("FacebookAds.csv") #placing the contents of the file to be searched in the textFile object
df = textFile.map(lambda r: Row(r)).toDF(["line"]) #Creating the df object which holds the dataFrame
searched = df.filter(col("line").like("%Patriot%")) #Creating the searched object which holds column name and also the word to be searched for.

#parameters established and dataframe complete at this point just need to search for the text we want now.
searched.count() #Count searched, not printing this out for this project.
#Counts searched mentioning phrase in .like().
searched.filter(col("line").like("%Patriot%")).count()


#print this out
#Fetches the MySQL searched as an array of strings
print(searched.filter(col("line").like("%Patriot%")).collect())


