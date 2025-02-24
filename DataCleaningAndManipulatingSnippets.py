#Useful pieces of Python code: 

## Lookup table preparation
### Remove white spaces
#### whitespace_remover is a function to remove leading and trailing white space. This is particularly useful to run on lookup tables before trying to merge with administrative datasets of interest 
#### Found at GeeksForGeeks.org (https://www.geeksforgeeks.org/pandas-strip-whitespace-from-entire-dataframe/)

####Takes a DataFrame as a parameter and strips the leading and trailing white spaces
def whitespace_remover(dataframe):
  # loop through columns
   for i in dataframe.columns: 
      # If the column is of type object (i.e., not numeric), use the str.strip function to remove leading and trailing spaces, else ignore
      if dataframe[i].dtype == 'object':
        dataframe[i] = dataframe[i].map(str.strip)
      else:
        pass
