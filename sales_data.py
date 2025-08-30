import pandas as pd
data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Region': ['North', 'South', 'East', 'West', 'South', 'North'],
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'Sales': [200, 150, 300, 400, 250, 500]
}

class Sales:
    def __init__(self):
        self.data=pd.DataFrame(data)
    
    def Total_sale(self):
        if self.data.empty:
            return 'No found any record..'
        total_sale = self.data.groupby('Product')['Sales'].sum()
        return total_sale
    
    def Region_sale_max(self):
        if self.data.empty:
            return 'No found any record..'
        total_region= self.data.groupby('Region')['Sales'].max()
        return total_region
    
    def Monthly_sales(self):
        if self.data.empty:
            return 'No found any record..'
        total_monthly=self.data.groupby('Month')['Sales'].mean()
        return total_monthly

if __name__=="__main__":
    system = Sales()
    print(system.Total_sale())
    print(system.Region_sale_max())
    print(system.Monthly_sales())