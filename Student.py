import pandas as pd
data = {
    'Student': ['Ram', 'Shyam', 'Geeta', 'Sita'],
    'Math': [80, 40, 90, 70],
    'Science': [75, 55, 95, 60],
    'English': [85, 60, 88, 72]
}

class Stdudent_Performance:
    def __init__(self):
        self.data=pd.DataFrame(data)
    
    def Total_marks(self):
        if self.data.empty:
            return 'No data found..'
        total_marks=self.data[['Math','Science','English']].sum(axis=1)
        self.data['Total Mark']=total_marks
        return self.data
    
    def Average_marks(self):
        if self.data.empty:
            return 'No data found..'
        avg_marks= self.data[['Math','Science','English']].mean(axis=1)
        self.data['Avg Mark']=avg_marks
        return avg_marks
    
    def Student_filter(self):
        if self.data.empty:
            return 'No data found..'
        mark = self.data[self.data['Avg Mark']<60]
        return mark
    
    def Highest_mark(self):
        return self.data.loc[self.data['Total Mark'].idxmax()]

if __name__=="__main__":
    system=Stdudent_Performance()

    print(system.Total_marks())
    print(system.Average_marks())
    print(system.Student_filter())
    print(system.Highest_mark())
    