#Step 1. Import the necessary libraries
import pandas as pd
import csv

#Step 2. Import the dataset Euro_2012_stats_TEAM

#Step 3. Assign it to a variable called euro12.
euro_12= pd.read_csv('Euro_2012_stats_TEAM.csv')

#Step 4. Select only the Goal column.
print(euro_12.Goals)

#Step 5. How many team participated in the Euro2012?
cld = euro_12.dropna()
print(cld.Team.index)

#Step 6. What is the number of columns in the dataset?
print(euro_12.shape)

#Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = pd.DataFrame(cld, columns=['Team', 'Yellow Cards', 'Red Cards'])
print(discipline)

#Step 8. Sort the teams by Red Cards, then to Yellow Cards
sort_red = discipline.sort_values(['Red Cards'], ascending=False)
sort_yellow = discipline.sort_values(['Yellow Cards'], ascending=False)
print(sort_red,'\n')
print(sort_yellow)

#Step 9. Calculate the mean Yellow Cards given per Team
discipline['Yellow Cards'].mean()

#Step 10. Filter teams that scored more than 6 goals
cld[cld.Goals > 6]

#Step 11. Select the teams that start with G
cld[cld.Team.str[0] == 'G']

#Step 12. Select the first 7 columns
cld.iloc[:, :7]


#Step 13. Select all columns except the last 3.
cld.iloc[:, :32]

#Step 14. Present only the Shooting Accuracy from England, Italy and Russia
s_a = cld.iloc[[2,6,11], [0,4]]
print(s_a)


#Step 15. Use apply method on Goal Column to make a new column called Performance, using following conditions
#1. If Goals are less than or equal to 2, peformance is Below Avg
#2. If Goals are more than 2 and less than or equal to 5, peformance is Average
#3. If Goals are more than 5 and less than or equal to 10, peformance is Above Average
#4. If Goals are more than 10 then peformance is Excellent

pf_labels = ['Below Average', 'Average', 'Above Average', 'Excellent']
categories = [0, 2, 5, 10, 15]
cld['Performance'] = pd.cut(cld['Goals'], labels = pf_labels, bins = categories)
print(cld[['Team', 'Goals', 'Performance']])