# Save dataframe
def save_finalDf(df):
    # current working directory
    current_path = os.getcwd()
    print(current_path)
    filepath = os.path.abspath(os.path.join(current_path, '..', 'Data'))
    filename = "Private.csv"

    # print(filename)
    saved_file = df.to_csv(os.path.join(filepath, filename),
                           index=False,
                           # mode='x',
                          )
    return saved_file

# Read data
def readSavedData(filename):
    currentDirectory = os.getcwd()
    print(currentDirectory)
    filepath = os.path.abspath(os.path.join(currentDirectory, '..', 'Data', filename))
    df = pd.read_csv(filepath)
    return df