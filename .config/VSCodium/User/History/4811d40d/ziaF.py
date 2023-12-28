import pandas as pd 
import matplotlib.pyplot as plt

data_f=pd.read_csv('/Users/apple/Desktop/vscode_intro/laba 13/student-mat.csv')
# print(data_f)


correlation_weekend = data_f['traveltime'].corr(data_f['Walc'])
correlation_weekdays = data_f['traveltime'].corr(data_f['Dalc'])
correlation_total = data_f['traveltime'].corr(data_f['Walc'] + data_f['Dalc'])


print(f"Correlation between distance to school and weekend alcohol consumption: {correlation_weekend}")
print(f"Correlation between distance to school and weekday alcohol consumption: {correlation_weekdays}")
print(f"Correlation between distance to school and total alcohol consumption: {correlation_total}")




plt.figure(figsize=(12, 8))

plt.scatter(data_f['traveltime'], data_f['Walc'], color='blue', label='Weekends')
plt.scatter(data_f['traveltime'], data_f['Dalc'], color='red', label='Weekdays')
plt.scatter(data_f['traveltime'], (data_f['Walc'] + data_f['Dalc']), color='green', label='total consumption')

plt.title('Correlation between distance to school and alcohol consumption')
plt.xlabel('Distance to school')
plt.ylabel('Level of alcohol consumption')
plt.legend()

plt.show()




correlation_payment = data_f['paid'].apply(lambda x: 1 if x == 'yes' else 0).corr(data_f['Dalc']+data_f['Walc'])
print(f"Correlation between paid and alcohol consumption: {correlation_payment}")

plt.figure(figsize=(12, 8))
plt.scatter(data_f['paid'], (data_f['Dalc'] + data_f['Walc']), color='purple', label='Total alcohol consumption')
plt.title('Correlation between paid and alcohol consumption')
plt.xlabel('Paid (Yes/No)')
plt.ylabel('Level of alcohol consumption')
plt.legend()
plt.show()



avg_alcohol_consumption = data_f.groupby('Fjob')[['Dalc', 'Walc']].mean()
avg_alcohol_consumption['Total'] = avg_alcohol_consumption['Dalc'] + avg_alcohol_consumption['Walc']

top_5_professions = avg_alcohol_consumption.sort_values(by='Total', ascending=False).head(5)

print(f"Top 5 job with the most alcoholic children: {top_5_professions}")


plt.figure(figsize=(12, 8))
top_5_professions['Total'].plot(kind='bar', color='teal')
plt.title('Top 5 job with the most alcoholic children')
plt.xlabel('Job')
plt.ylabel('Average alcohol consumption')
plt.show()

