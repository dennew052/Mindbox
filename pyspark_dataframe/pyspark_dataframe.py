from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('PySpark_Tutorial')\
        .getOrCreate()

csv_my_products = r'csv_files\myProducts.csv'
csv_my_categories = r'csv_files\myCategories.csv'
csv_my_products_and_categories = r'csv_files\myProductsAndCategories.csv'

# data_products = spark.read.csv(csv_my_products, sep=',', header=True).createOrReplaceTempView("products")
# data_categories = spark.read.csv(csv_my_categories, sep=',', header=True).createOrReplaceTempView("categories")
# data_products_and_categories = spark.read.csv(csv_my_products_and_categories, sep=',', header=True).createOrReplaceTempView("products_and_categories")
# df = spark.sql("SELECT products.product_name, categories.category_name FROM products \
#                 LEFT JOIN products_and_categories ON products.product_id = products_and_categories.product_id \
#                 LEFT JOIN categories ON products_and_categories.category_id = categories.category_id") \
#                 .show()

data_products = spark.read.csv(csv_my_products, sep=',', header=True)
data_categories = spark.read.csv(csv_my_categories, sep=',', header=True)
data_products_and_categories = spark.read.csv(csv_my_products_and_categories, sep=',', header=True)

df = data_products.join(data_products_and_categories, data_products.product_id == data_products_and_categories.product_id, "left") \
    .join(data_categories, data_categories.category_id == data_products_and_categories.category_id, "left") \
    .select(['product_name', 'category_name']) \
    .show()