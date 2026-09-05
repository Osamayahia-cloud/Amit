from config.config import file_path,COLS_DROP
from preprocessing import (
    read_file,
    Drop_unnecessary_features,
    Check_data_type,
    handle_Null,
    handle_data_type,
    handle_outliers,
    check_outliers
)
def main():

    # 1. Read data
    df = read_file(file_path)

    if df is None:
        return
    
    print("Original Data:")
    print(df.head())
    Drop_unnecessary_features(df,COLS_DROP)
    print(df.head())
        
    handle_data_type(df)
    print(df.dtypes)

    df.drop_duplicates(inplace=True)
    
    
    print("\nData Information:")
    print(Check_data_type(df))


    handle_Null(df)
    



    print("\nOutliers before handling:")
    check_outliers(df)


    handle_outliers(df)


    print("\nOutliers after handling:")
    check_outliers(df)


    print("\nCleaned Data:")
    print(df.head())

    print("\nFinal Shape:")
    print(df.shape)


if __name__ == "__main__":
    main()