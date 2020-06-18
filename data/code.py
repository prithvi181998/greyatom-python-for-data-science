# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#print(data.shape)

#Code starts here
census = np.concatenate((new_record, data))
print(census.shape)
age = np.asarray(census[:,0])
max_age = age.max()
print(max_age)
age_min = age.min()
print(age_min)
age_mean = np.mean(age)
age_mean = str(round(age_mean,2))
print(age_mean)
age_std = np.std(age)
age_std = str(round(age_std,2))
print(age_std)

race_0 = np.asarray(census[census[:,2] == 0])
len_0 = len(race_0)

race_1 = np.asarray(census[census[:,2] == 1])
len_1 = len(race_1)

race_2 = np.asarray(census[census[:,2] == 2])
len_2 = len(race_2)

race_3 = np.asarray(census[census[:,2] == 3])
len_3 = len(race_3)

race_4 = np.asarray(census[census[:,2] == 4])
len_4 = len(race_4)

minority = [len_0, len_1, len_2, len_3, len_4]
minority_race = minority.index(min(minority))
print(minority_race)


senior_citizens = census[census[:,0] > 60]
senior_citizens_len = len(senior_citizens)

working_hours_sum = senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
avg_working_hours = working_hours_sum/senior_citizens_len
avg_working_hours = str(round(avg_working_hours,2))
print(avg_working_hours)


high = census[census[:,1] > 10]
avg_pay_high = high[:,7].mean()
#avg_pay_high = str(round(avg_pay_high,2))
print(avg_pay_high)

low = census[census[:,1] <= 10]
avg_pay_low = low[:,7].mean()
#avg_pay_low = str(round(avg_pay_low,2))
print(avg_pay_low)





