import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time


df=pd.read_excel("Ecommerce_Sales_Modified.xlsx")




while True:
    A = input("Enter the month you want to analyse the sales data (or 'Exit' to quit): ")

    if A == "Exit":
        print("Exiting program...")
        time.sleep(2)
        print("----Exit Completed----")
        break

    match A:
        case "January":
            jan_df = df.query("Month == 'January'")
            print(jan_df)
            while True:
                b = input(
                    "\nChoose an option:\n"
                    "1. Total_Orders\n"
                    "2. Total_Revenue\n"
                    "3. Total_Quantity\n"
                    "4. Average_orders\n"
                    "5. Monthly_Revenue_Chart\n"
                    "6. Category_wise_sales\n"
                    "7. Top_Products\n"
                    "8. Order_Volume_Trend\n"
                    "9. Unique_customers\n"
                   "10. High_value_customers\n"
                   "11. Regional_revenue\n"
                   "12. Best_performing_regions\n"
                   "13. Region_wise_product_trends\n"
                   "14. Back_to_Month_Selection\n"
                    "\nEnter your choice: "
                )
                match b:
                    case "1" | "Total_Orders":
                        print("Total Orders in January:", jan_df["OrderID"].nunique())
                    case "2" | "Total_Revenue":
                        print("Total Revenue in January:", jan_df["Revenue"].sum())
                    case "3" | "Total_Quantity":
                        print("Total Quantity in January:", jan_df["Quantity"].sum())
                    case "4" | "Average_orders":
                        print("Average Order Value in January:", jan_df["Revenue"].mean())
                    case "5" | "Monthly_Revenue_Chart":
                        monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=monthly_revenue, x="Month", y="Revenue")
                        plt.title("Monthly Revenue Analysis")
                        plt.xlabel("Month")
                        plt.ylabel("Total Revenue")
                        plt.tight_layout()
                        plt.show()
                    case "6" | "Category_wise_sales":
                        category_wise_sales = df.groupby("Category")["Price"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=category_wise_sales, x="Category", y="Price")
                        plt.title("Category wise sales analysis")
                        plt.xlabel("Category")
                        plt.ylabel("Total")
                        plt.tight_layout()
                        plt.show()
                    case "7" | "Top_Products":
                        top_products = jan_df.groupby("Product")[["Quantity", "Revenue"]].sum().sort_values("Revenue", ascending=False).head(10).reset_index()
                        sns.barplot(x="Product", y="Revenue", data=top_products)
                        plt.title("Top 10 Best-Selling Products (by Revenue) - January")
                        plt.xlabel("Products")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "8" | "Order_Volume_Trend":
                        order_volume = jan_df.groupby("Order_Day")["OrderID"].count().reset_index()
                        sns.lineplot(x="Order_Day", y="OrderID", data=order_volume)
                        plt.title("Daily order volume trend in January")
                        plt.xlabel("Order Day")
                        plt.ylabel("Orders")
                        plt.show()
                    case "9" | "Unique_customers":
                        unique_customers = jan_df["OrderID"].nunique()
                        repeat_buyers = (jan_df["OrderID"].value_counts() > 1).sum()
                        print(f"Total Unique Customers in January: {unique_customers}")
                        print(f"Repeat Buyers in January: {repeat_buyers}")
                    case "10" | "High_value_customers":
                        high_value_customers = jan_df.groupby("OrderID")["Price"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="OrderID", y="Price", data=high_value_customers)
                        plt.title("Top 5 High value customers in January")
                        plt.xlabel("OrderID")
                        plt.ylabel("Price")
                        plt.show()
                    case "11" | "Regional_revenue":
                        regional_revenue=jan_df.groupby("Region")["Revenue"].sum().reset_index()
                        sns.barplot(x="Region", y="Revenue", data=regional_revenue)
                        plt.title("Regional revenue in january")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "12" | "Best_performing_regions":
                        best_performing_regions=jan_df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="Region", y="Revenue", data=best_performing_regions)
                        plt.title("Top 5 best regions based on revenue")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "13" | "Region_wise_product_trends":
                        region_wise_product_trends=jan_df.groupby(["Region","Product"])["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False).head(10)
                        heatmap_data=region_wise_product_trends.pivot(index="Region", columns="Product", values="Quantity")
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(heatmap_data,annot=True,fmt=".0f",cmap="YlGnBu")
                        plt.title("Top 10 product trends in all regions")
                        plt.tight_layout()
                        plt.show()
                    case "14" | "Back_to_Month_Selection":
                        print("Returning to month selection...")
                        time.sleep(4)
                        break
                    case _:
                        print("Invalid input")

        case "February":
            feb_df = df.query("Month == 'February'")
            print(feb_df)
            while True:
                b = input(
                    "\nChoose an option:\n"
                    "1. Total_Orders\n"
                    "2. Total_Revenue\n"
                    "3. Total_Quantity\n"
                    "4. Average_orders\n"
                    "5. Monthly_Revenue_Chart\n"
                    "6. Category_wise_sales\n"
                    "7. Top_Products\n"
                    "8. Order_Volume_Trend\n"
                    "9. Unique_customers\n"
                    "10. High_value_customers\n"
                    "11. Regional_revenue\n"
                    "12. Best_performing_regions\n"
                    "13. Region_wise_product_trends\n"
                    "14. Back_to_Month_Selection\n"
                    "\nEnter your choice: "
                )
                match b:
                    case "1" | "Total_Orders":
                        print("Total Orders in February:", feb_df["OrderID"].nunique())
                    case "2" | "Total_Revenue":
                        print("Total Revenue in February:", feb_df["Revenue"].sum())
                    case "3" | "Total_Quantity":
                        print("Total Quantity in February:", feb_df["Quantity"].sum())
                    case "4" | "Average_orders":
                        print("Average Order Value in February:", feb_df["Revenue"].mean())
                    case "5" | "Monthly_Revenue_Chart":
                        monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=monthly_revenue, x="Month", y="Revenue")
                        plt.title("Monthly Revenue Analysis")
                        plt.xlabel("Month")
                        plt.ylabel("Total Revenue")
                        plt.tight_layout()
                        plt.show()
                    case "6" | "Category_wise_sales":
                        category_wise_sales = df.groupby("Category")["Price"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=category_wise_sales, x="Category", y="Price")
                        plt.title("Category wise sales analysis")
                        plt.xlabel("Category")
                        plt.ylabel("Total")
                        plt.tight_layout()
                        plt.show()
                    case "7" | "Top_Products":
                        top_products = feb_df.groupby("Product")[["Quantity", "Revenue"]].sum().sort_values("Revenue", ascending=False).head(10).reset_index()
                        sns.barplot(x="Product", y="Revenue", data=top_products)
                        plt.title("Top 10 Best-Selling Products (by Revenue) - February")
                        plt.xlabel("Products")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "8" | "Order_Volume_Trend":
                        order_volume = feb_df.groupby("Order_Day")["OrderID"].count().reset_index()
                        sns.lineplot(x="Order_Day", y="OrderID", data=order_volume)
                        plt.title("Daily order volume trend in February")
                        plt.xlabel("Order Day")
                        plt.ylabel("Orders")
                        plt.show()
                    case "9" | "Unique_customers":
                        unique_customers = feb_df["OrderID"].nunique()
                        repeat_buyers = (feb_df["OrderID"].value_counts() > 1).sum()
                        print(f"Total Unique Customers in February: {unique_customers}")
                        print(f"Repeat Buyers in February: {repeat_buyers}")
                    case "10" | "High_value_customers":
                        high_value_customers = feb_df.groupby("OrderID")["Price"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="OrderID", y="Price", data=high_value_customers)
                        plt.title("Top 5 High value customers in February")
                        plt.xlabel("OrderID")
                        plt.ylabel("Price")
                        plt.show()
                    case "11" | "Regional_revenue":
                        regional_revenue=feb_df.groupby("Region")["Revenue"].sum().reset_index()
                        sns.barplot(x="Region", y="Revenue", data=regional_revenue)
                        plt.title("Regional revenue in February")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "12" | "Best_performing_regions":
                        best_performing_regions=feb_df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="Region", y="Revenue", data=best_performing_regions)
                        plt.title("Top 5 best regions based on revenue")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "13" | "Region_wise_product_trends":
                        region_wise_product_trends=feb_df.groupby(["Region","Product"])["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False).head(10)
                        heatmap_data=region_wise_product_trends.pivot(index="Region", columns="Product", values="Quantity")
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(heatmap_data,annot=True,fmt=".0f",cmap="YlGnBu")
                        plt.title("Top 10 product trends in all regions")
                        plt.tight_layout()
                        plt.show()
                    case "14" | "Back_to_Month_Selection":
                        print("Returning to month selection...")
                        time.sleep(4)
                        break
                    case _:
                        print("Invalid input")

        case "March":
            mar_df = df.query("Month == 'March'")
            print(mar_df)
            while True:
                b = input(
                    "\nChoose an option:\n"
                    "1. Total_Orders\n"
                    "2. Total_Revenue\n"
                    "3. Total_Quantity\n"
                    "4. Average_orders\n"
                    "5. Monthly_Revenue_Chart\n"
                    "6. Category_wise_sales\n"
                    "7. Top_Products\n"
                    "8. Order_Volume_Trend\n"
                    "9. Unique_customers\n"
                    "10. High_value_customers\n"
                    "11. Regional_revenue\n"
                    "12. Best_performing_regions\n"
                    "13. Region_wise_product_trends\n"
                    "14. Back_to_Month_Selection\n"
                    "\nEnter your choice: "
                )
                match b:
                    case "1" | "Total_Orders":
                        print("Total Orders in March:", mar_df["OrderID"].nunique())
                    case "2" | "Total_Revenue":
                        print("Total Revenue in March:", mar_df["Revenue"].sum())
                    case "3" | "Total_Quantity":
                        print("Total Quantity in March:", mar_df["Quantity"].sum())
                    case "4" | "Average_orders":
                        print("Average Order Value in March:", mar_df["Revenue"].mean())
                    case "5" | "Monthly_Revenue_Chart":
                        monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=monthly_revenue, x="Month", y="Revenue")
                        plt.title("Monthly Revenue Analysis")
                        plt.xlabel("Month")
                        plt.ylabel("Total Revenue")
                        plt.tight_layout()
                        plt.show()
                    case "6" | "Category_wise_sales":
                        category_wise_sales = df.groupby("Category")["Price"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=category_wise_sales, x="Category", y="Price")
                        plt.title("Category wise sales analysis")
                        plt.xlabel("Category")
                        plt.ylabel("Total")
                        plt.tight_layout()
                        plt.show()
                    case "7" | "Top_Products":
                        top_products = mar_df.groupby("Product")[["Quantity", "Revenue"]].sum().sort_values("Revenue", ascending=False).head(10).reset_index()
                        sns.barplot(x="Product", y="Revenue", data=top_products)
                        plt.title("Top 10 Best-Selling Products (by Revenue) - March")
                        plt.xlabel("Products")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "8" | "Order_Volume_Trend":
                        order_volume = mar_df.groupby("Order_Day")["OrderID"].count().reset_index()
                        sns.lineplot(x="Order_Day", y="OrderID", data=order_volume)
                        plt.title("Daily order volume trend in March")
                        plt.xlabel("Order Day")
                        plt.ylabel("Orders")
                        plt.show()
                    case "9" | "Unique_customers":
                        unique_customers = mar_df["OrderID"].nunique()
                        repeat_buyers = (mar_df["OrderID"].value_counts() > 1).sum()
                        print(f"Total Unique Customers in March: {unique_customers}")
                        print(f"Repeat Buyers in March: {repeat_buyers}")
                    case "10" | "High_value_customers":
                        high_value_customers = mar_df.groupby("OrderID")["Price"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="OrderID", y="Price", data=high_value_customers)
                        plt.title("Top 5 High value customers in March")
                        plt.xlabel("OrderID")
                        plt.ylabel("Price")
                        plt.show()
                    case "11" | "Regional_revenue":
                        regional_revenue=mar_df.groupby("Region")["Revenue"].sum().reset_index()
                        sns.barplot(x="Region", y="Revenue", data=regional_revenue)
                        plt.title("Regional revenue in March")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "12" | "Best_performing_regions":
                        best_performing_regions=mar_df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="Region", y="Revenue", data=best_performing_regions)
                        plt.title("Top 5 best regions based on revenue")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "13" | "Region_wise_product_trends":
                        region_wise_product_trends=mar_df.groupby(["Region","Product"])["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False).head(10)
                        heatmap_data=region_wise_product_trends.pivot(index="Region", columns="Product", values="Quantity")
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(heatmap_data,annot=True,fmt=".0f",cmap="YlGnBu")
                        plt.title("Top 10 product trends in all regions")
                        plt.tight_layout()
                        plt.show()
                    case "14" | "Back_to_Month_Selection":
                        print("Returning to month selection...")
                        time.sleep(4)
                        break
                    case _:
                        print("Invalid input")

        case "April":
            apr_df = df.query("Month == 'April'")
            print(apr_df)
            while True:
                b = input(
                    "\nChoose an option:\n"
                    "1. Total_Orders\n"
                    "2. Total_Revenue\n"
                    "3. Total_Quantity\n"
                    "4. Average_orders\n"
                    "5. Monthly_Revenue_Chart\n"
                    "6. Category_wise_sales\n"
                    "7. Top_Products\n"
                    "8. Order_Volume_Trend\n"
                    "9. Unique_customers\n"
                    "10. High_value_customers\n"
                    "11. Regional_revenue\n"
                    "12. Best_performing_regions\n"
                    "13. Region_wise_product_trends\n"
                    "14. Back_to_Month_Selection\n"
                    "\nEnter your choice: "
                )
                match b:
                    case "1" | "Total_Orders":
                        print("Total Orders in April:", apr_df["OrderID"].nunique())
                    case "2" | "Total_Revenue":
                        print("Total Revenue in April:", apr_df["Revenue"].sum())
                    case "3" | "Total_Quantity":
                        print("Total Quantity in April:", apr_df["Quantity"].sum())
                    case "4" | "Average_orders":
                        print("Average Order Value in April:", apr_df["Revenue"].mean())
                    case "5" | "Monthly_Revenue_Chart":
                        monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=monthly_revenue, x="Month", y="Revenue")
                        plt.title("Monthly Revenue Analysis")
                        plt.xlabel("Month")
                        plt.ylabel("Total Revenue")
                        plt.tight_layout()
                        plt.show()
                    case "6" | "Category_wise_sales":
                        category_wise_sales = df.groupby("Category")["Price"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=category_wise_sales, x="Category", y="Price")
                        plt.title("Category wise sales analysis")
                        plt.xlabel("Category")
                        plt.ylabel("Total")
                        plt.tight_layout()
                        plt.show()
                    case "7" | "Top_Products":
                        top_products = apr_df.groupby("Product")[["Quantity", "Revenue"]].sum().sort_values("Revenue", ascending=False).head(10).reset_index()
                        sns.barplot(x="Product", y="Revenue", data=top_products)
                        plt.title("Top 10 Best-Selling Products (by Revenue) - April")
                        plt.xlabel("Products")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "8" | "Order_Volume_Trend":
                        order_volume = apr_df.groupby("Order_Day")["OrderID"].count().reset_index()
                        sns.lineplot(x="Order_Day", y="OrderID", data=order_volume)
                        plt.title("Daily order volume trend in April")
                        plt.xlabel("Order Day")
                        plt.ylabel("Orders")
                        plt.show()
                    case "9" | "Unique_customers":
                        unique_customers = apr_df["OrderID"].nunique()
                        repeat_buyers = (apr_df["OrderID"].value_counts() > 1).sum()
                        print(f"Total Unique Customers in April: {unique_customers}")
                        print(f"Repeat Buyers in April: {repeat_buyers}")
                    case "10" | "High_value_customers":
                        high_value_customers = apr_df.groupby("OrderID")["Price"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="OrderID", y="Price", data=high_value_customers)
                        plt.title("Top 5 High value customers in April")
                        plt.xlabel("OrderID")
                        plt.ylabel("Price")
                        plt.show()
                    case "11" | "Regional_revenue":
                        regional_revenue=apr_df.groupby("Region")["Revenue"].sum().reset_index()
                        sns.barplot(x="Region", y="Revenue", data=regional_revenue)
                        plt.title("Regional revenue in April")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "12" | "Best_performing_regions":
                        best_performing_regions=apr_df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="Region", y="Revenue", data=best_performing_regions)
                        plt.title("Top 5 best regions based on revenue")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "13" | "Region_wise_product_trends":
                        region_wise_product_trends=apr_df.groupby(["Region","Product"])["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False).head(10)
                        heatmap_data=region_wise_product_trends.pivot(index="Region", columns="Product", values="Quantity")
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(heatmap_data,annot=True,fmt=".0f",cmap="YlGnBu")
                        plt.title("Top 10 product trends in all regions")
                        plt.tight_layout()
                        plt.show()
                    case "14" | "Back_to_Month_Selection":
                        print("Returning to month selection...")
                        time.sleep(4)
                        break
                    case _:
                        print("Invalid input")

        case "May":
            may_df = df.query("Month == 'May'")
            print(may_df)
            while True:
                b = input(
                    "\nChoose an option:\n"
                    "1. Total_Orders\n"
                    "2. Total_Revenue\n"
                    "3. Total_Quantity\n"
                    "4. Average_orders\n"
                    "5. Monthly_Revenue_Chart\n"
                    "6. Category_wise_sales\n"
                    "7. Top_Products\n"
                    "8. Order_Volume_Trend\n"
                    "9. Unique_customers\n"
                    "10. High_value_customers\n"
                    "11. Regional_revenue\n"
                    "12. Best_performing_regions\n"
                    "13. Region_wise_product_trends\n"
                    "14. Back_to_Month_Selection\n"
                    "\nEnter your choice: "
                )
                match b:
                    case "1" | "Total_Orders":
                        print("Total Orders in May:", may_df["OrderID"].nunique())
                    case "2" | "Total_Revenue":
                        print("Total Revenue in May:", may_df["Revenue"].sum())
                    case "3" | "Total_Quantity":
                        print("Total Quantity in May:", may_df["Quantity"].sum())
                    case "4" | "Average_orders":
                        print("Average Order Value in May:", may_df["Revenue"].mean())
                    case "5" | "Monthly_Revenue_Chart":
                        monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=monthly_revenue, x="Month", y="Revenue")
                        plt.title("Monthly Revenue Analysis")
                        plt.xlabel("Month")
                        plt.ylabel("Total Revenue")
                        plt.tight_layout()
                        plt.show()
                    case "6" | "Category_wise_sales":
                        category_wise_sales = df.groupby("Category")["Price"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=category_wise_sales, x="Category", y="Price")
                        plt.title("Category wise sales analysis")
                        plt.xlabel("Category")
                        plt.ylabel("Total")
                        plt.tight_layout()
                        plt.show()
                    case "7" | "Top_Products":
                        top_products = may_df.groupby("Product")[["Quantity", "Revenue"]].sum().sort_values("Revenue", ascending=False).head(10).reset_index()
                        sns.barplot(x="Product", y="Revenue", data=top_products)
                        plt.title("Top 10 Best-Selling Products (by Revenue) - May")
                        plt.xlabel("Products")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "8" | "Order_Volume_Trend":
                        order_volume = may_df.groupby("Order_Day")["OrderID"].count().reset_index()
                        sns.lineplot(x="Order_Day", y="OrderID", data=order_volume)
                        plt.title("Daily order volume trend in May")
                        plt.xlabel("Order Day")
                        plt.ylabel("Orders")
                        plt.show()
                    case "9" | "Unique_customers":
                        unique_customers = may_df["OrderID"].nunique()
                        repeat_buyers = (may_df["OrderID"].value_counts() > 1).sum()
                        print(f"Total Unique Customers in May: {unique_customers}")
                        print(f"Repeat Buyers in May: {repeat_buyers}")
                    case "10" | "High_value_customers":
                        high_value_customers = may_df.groupby("OrderID")["Price"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="OrderID", y="Price", data=high_value_customers)
                        plt.title("Top 5 High value customers in May")
                        plt.xlabel("OrderID")
                        plt.ylabel("Price")
                        plt.show()
                    case "11" | "Regional_revenue":
                        regional_revenue=may_df.groupby("Region")["Revenue"].sum().reset_index()
                        sns.barplot(x="Region", y="Revenue", data=regional_revenue)
                        plt.title("Regional revenue in May")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "12" | "Best_performing_regions":
                        best_performing_regions=may_df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="Region", y="Revenue", data=best_performing_regions)
                        plt.title("Top 5 best regions based on revenue")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "13" | "Region_wise_product_trends":
                        region_wise_product_trends=may_df.groupby(["Region","Product"])["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False).head(10)
                        heatmap_data=region_wise_product_trends.pivot(index="Region", columns="Product", values="Quantity")
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(heatmap_data,annot=True,fmt=".0f",cmap="YlGnBu")
                        plt.title("Top 10 product trends in all regions")
                        plt.tight_layout()
                        plt.show()
                    case "14" | "Back_to_Month_Selection":
                        print("Returning to month selection...")
                        time.sleep(4)
                        break
                    case _:
                        print("Invalid input")

        case "June":
            jun_df = df.query("Month == 'June'")
            print(jun_df)
            while True:
                b = input(
                    "\nChoose an option:\n"
                    "1. Total_Orders\n"
                    "2. Total_Revenue\n"
                    "3. Total_Quantity\n"
                    "4. Average_orders\n"
                    "5. Monthly_Revenue_Chart\n"
                    "6. Category_wise_sales\n"
                    "7. Top_Products\n"
                    "8. Order_Volume_Trend\n"
                    "9. Unique_customers\n"
                    "10. High_value_customers\n"
                    "11. Regional_revenue\n"
                    "12. Best_performing_regions\n"
                    "13. Region_wise_product_trends\n"
                    "14. Back_to_Month_Selection\n"
                    "\nEnter your choice: "
                )
                match b:
                    case "1" | "Total_Orders":
                        print("Total Orders in June:", jun_df["OrderID"].nunique())
                    case "2" | "Total_Revenue":
                        print("Total Revenue in June:", jun_df["Revenue"].sum())
                    case "3" | "Total_Quantity":
                        print("Total Quantity in June:", jun_df["Quantity"].sum())
                    case "4" | "Average_orders":
                        print("Average Order Value in June:", jun_df["Revenue"].mean())
                    case "5" | "Monthly_Revenue_Chart":
                        monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=monthly_revenue, x="Month", y="Revenue")
                        plt.title("Monthly Revenue Analysis")
                        plt.xlabel("Month")
                        plt.ylabel("Total Revenue")
                        plt.tight_layout()
                        plt.show()
                    case "6" | "Category_wise_sales":
                        category_wise_sales = df.groupby("Category")["Price"].sum().reset_index()
                        plt.figure(figsize=(8, 5))
                        sns.barplot(data=category_wise_sales, x="Category", y="Price")
                        plt.title("Category wise sales analysis")
                        plt.xlabel("Category")
                        plt.ylabel("Total")
                        plt.tight_layout()
                        plt.show()
                    case "7" | "Top_Products":
                        top_products = jun_df.groupby("Product")[["Quantity", "Revenue"]].sum().sort_values("Revenue", ascending=False).head(10).reset_index()
                        sns.barplot(x="Product", y="Revenue", data=top_products)
                        plt.title("Top 10 Best-Selling Products (by Revenue) - June")
                        plt.xlabel("Products")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "8" | "Order_Volume_Trend":
                        order_volume = jun_df.groupby("Order_Day")["OrderID"].count().reset_index()
                        sns.lineplot(x="Order_Day", y="OrderID", data=order_volume)
                        plt.title("Daily order volume trend in June")
                        plt.xlabel("Order Day")
                        plt.ylabel("Orders")
                        plt.show()
                    case "9" | "Unique_customers":
                        unique_customers = jun_df["OrderID"].nunique()
                        repeat_buyers = (jun_df["OrderID"].value_counts() > 1).sum()
                        print(f"Total Unique Customers in June: {unique_customers}")
                        print(f"Repeat Buyers in June: {repeat_buyers}")
                    case "10" | "High_value_customers":
                        high_value_customers = jun_df.groupby("OrderID")["Price"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="OrderID", y="Price", data=high_value_customers)
                        plt.title("Top 5 High value customers in June")
                        plt.xlabel("OrderID")
                        plt.ylabel("Price")
                        plt.show()
                    case "11" | "Regional_revenue":
                        regional_revenue=jun_df.groupby("Region")["Revenue"].sum().reset_index()
                        sns.barplot(x="Region", y="Revenue", data=regional_revenue)
                        plt.title("Regional revenue in June")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "12" | "Best_performing_regions":
                        best_performing_regions=jun_df.groupby("Region")["Revenue"].sum().sort_values(ascending=False).head(5).reset_index()
                        sns.barplot(x="Region", y="Revenue", data=best_performing_regions)
                        plt.title("Top 5 best regions based on revenue")
                        plt.xlabel("Region")
                        plt.ylabel("Revenue")
                        plt.show()
                    case "13" | "Region_wise_product_trends":
                        region_wise_product_trends=jun_df.groupby(["Region","Product"])["Quantity"].sum().reset_index().sort_values("Quantity",ascending=False).head(10)
                        heatmap_data=region_wise_product_trends.pivot(index="Region", columns="Product", values="Quantity")
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(heatmap_data,annot=True,fmt=".0f",cmap="YlGnBu")
                        plt.title("Top 10 product trends in all regions")
                        plt.tight_layout()
                        plt.show()
                    case "14" | "Back_to_Month_Selection":
                        
                        print("Returning to month selection...")
                        time.sleep(4)
                        break
                    case _:
                        print("Invalid input")

        case _:
            print("This month is not in the sales data")
