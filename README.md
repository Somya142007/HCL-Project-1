# HCL-Project-1


Sales Performance Analysis Using python

Introduction



Originally when I looked at the sales data, there was just so many rows and columns and I could not really make head nor tail of it.

Therefore, my idea was to create an analysis on this data, so that it could be easily understood.



My project allows me to import in data from a CSV, and then analyse and clean it. Finally this data can be displayed on a dashboard including visualisations.



Rather than having to analyse every single row, you can now simply view the dashboard to obtain information such as overall sales, profit and which products and categories are selling well. Additionally, you can also view which region is performing better and even place filters around the data for further investigation.

Objectives

Whilst my objectives weren’t complex, I aimed to:



- Analyse real sales data – as this will teach you far more.

- Understand how to appropriately clean data (for example by deleting duplicates and managing missing data).



- Calculate key statistics such as sales, profit and orders, plus the number of items sold.

- Investigate which category is performing well.

- Investigate which regions are contributing sales and how these differ.

- Investigate sales per month so that trends can be analysed (for example whether sales are increasing or decreasing).

- Identify best selling products.

- Display all this within a single dashboard, so that it is easy to understand.

- Also include a function to allow people to download filtered data.

Software and Technology

The software and technology I used was all standard:

Technology Used For

Python Coding

Pandas Importing and cleaning data

NumPy Performing some calculations

Matplotlib Producing basic visualisations

Seaborn Enhancing visualisations

Plotly Producing interactive visualisations

Streamlit Producing a dashboard

CSV As my sales data was in CSV format.

VS Code Coding and executing code.

How It Works

I carried out my project in sections to ensure that I did not become disorganised.

1. Importing Data – Firstly I imported my CSV file using Pandas.

2. Cleaning Data – I investigated my data to identify missing data, duplicates and issues with dates. As the date column was not in standard format, I also converted it into the right format. Following this, I stored my cleaned data in a new file.

3. Analysing Data – I then analysed my data to obtain key statistics such as sales, profit and order information.

4. Visualising Data – I created visualisations to display sales per month, category and region. Plus I also produced visualisations to show best selling products. Visualisations are extremely useful as they allow data to be easily analysed.

5. Producing Dashboard – Having analysed my data, I then combined all my information onto a dashboard using Streamlit.

6. Investigating – Finally, users can investigate data further by placing filters on it. They can also analyse and compare information and even download filtered data.

Project Features

Sales Summary – Overall sales, profit, orders and quantity can all be viewed.

Category Analysis – This enables users to compare different categories and identify which is performing better.

Region Analysis – Users can investigate which regions are contributing the most sales.

Monthly Sales Trend – This shows how sales have evolved.

Best Selling Products – Best selling products can be viewed.

Filters and Download – Filters can be placed relating to category, region and date. Furthermore, if required, data can be downloaded.