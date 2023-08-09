import pandas as pd

df = pd.read_csv('data.csv')
print(df)

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)

print()

df = pd.read_csv('data.csv')
print(df)

print()

df = pd.read_json('data.json')
print(df.to_string())

print()

data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}
df = pd.DataFrame(data)
print(df)

# Viewing data
df = pd.read_csv('data.csv')
print(df.head(10))  # The head() method returns the headers and a specified number of rows, starting from the top

df = pd.read_csv('data.csv')  # If no number of rows is specified, the head() will return the first five rows
print(df.head())

print(df.tail())  # The tail() method returns the headers and a specified number of rows, starting from the bottom

print()

# Cleaning data
df = pd.read_csv('dat.csv')
new_df = df.dropna()  # Remove rows that contain empty cells
print(new_df.to_string())  # By default, the dropna() method returns a new DataFrame, and will not change the original

print()

df = pd.read_csv('dat.csv')
df.dropna(inplace=True)  # inplace = True argument changes the original dataFrame
print(df.to_string())

# Replace empty cells with values
df = pd.read_csv('dat.csv')
df.fillna(130, inplace=True)
print(df.to_string())

df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace=True)  # Replace only a specific column
print(df.to_string())  # his operation inserts 130 in empty cells in the "Calories" column

# Replace using the mean, median or mode value of the column
df = pd.read_csv('data.csv')
x = df["Calories"].mean()  # Replacing using the mean of the column, Calories
df["Calories"].fillna(x, inplace=True)
print(df.to_string())

df = pd.read_csv('data.csv')
x = df["Calories"].median()  # Replacing using the median of the column, Calories
df["Calories"].fillna(x, inplace=True)
print(df.to_string())

df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]  # Replacing using the mode of the column, Calories
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
