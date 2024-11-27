import os
import pandas as pd

# Directory where your CSV files are located
csv_folder = r'C:/Users/asus/Desktop/Law data/Data/province data'
output="C:/Users/asus/Desktop/Law data/Data/transformed data/immigration firms by province.csv"

def Concatenate_province_DataFrames(csv_folder=csv_folder,output_path=output):
    # List to hold DataFrames
    all_data = []

    # Loop through each file in the directory
    for file_name in os.listdir(csv_folder):
        if file_name.endswith(".csv"):  # Check if the file is a CSV
            file_path = os.path.join(csv_folder, file_name)
        
        # Read the CSV file
            df = pd.read_csv(file_path)
        
        # Add a new column for the file name (without extension)
            csv_name = os.path.splitext(file_name)[0]
            df['Province'] =csv_name.split('-')[1]
        
        
        # Append the DataFrame to the list
            all_data.append(df)

    # Concatenate all DataFrames into one
    combined_df = pd.concat(all_data, ignore_index=True)

    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(output_path, index=False)

    print(f"CSV Province files combined successfully! in {output_path}")


#add province column to lawyers
output="C:/Users/asus/Desktop/Law data/Data/transformed data/immigration_lawyers.csv"
def add_province_to_lawyers(Lawyers,output_path=output):
    province=[]
    for Location2 in Lawyers["Location"]:
        province.append(Location2.split(', ')[1])

    Lawyers["Province"]=province
    Lawyers.to_csv(output_path)
    #Lawyers.head()


def Transform_data():
    Lawyers=pd.read_csv("C:/Users/asus/Desktop/Law data/Data/immigration_lawyers.csv")
    immigration_firms_without_province= pd.read_csv("C:/Users/asus/Desktop/Law data/Data/law_firms_canada.csv")
    #immigration_firms_with_province=pd.read_csv("C:/Users/asus/Desktop/Law data/Data/immigration firms by province.csv")
    #linkedin_data=pd.read_csv("C:/Users/asus/Desktop/Law data/Data/linkedIn data collected manual.csv")
    Concatenate_province_DataFrames()
    add_province_to_lawyers(Lawyers=Lawyers)
    immigration_firms_without_province.to_csv("C:/Users/asus/Desktop/Law data/Data/transformed data/law_firms_canada.csv")
    #linkedin_data.to_csv("C:/Users/asus/Desktop/Law data/Data/transformed data/linkedIn data collected manual.csv")
    print("Data Transformed successfully!")


