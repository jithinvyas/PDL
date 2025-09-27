import pandas as pd
        
    def clean(filename):
        df = pd.read_csv(filename)
        df1 = df.fillna(0)
        return df1
        
    if __name__ == "__main__":
        filename = sys.args[1]