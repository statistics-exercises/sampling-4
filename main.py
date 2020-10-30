# Uncomment these two lines if you get an error saying pandas is not available
from os import system
system('pip install pandas')
import numpy as np 
import pandas as pd

# This reads in the data from the movie_data.txt file
movies_df = pd.read_csv("movie_data.txt", index_col="Title")

# This is the command that generates the box plot 
movies_df['revenue_millions'].plot(kind="box").get_figure().savefig("boxplot.png")
