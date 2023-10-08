###Imports
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



###---------------------------------------------------------------------------------------------
###Functions

###Standard Operations

def mean_value(lst):
    mean = 0
    for value in lst:
        mean += (float(value) / len(lst))
    return mean
        

###Extracting Data
def nth_element_of_lst(lst, index):
    return [sub_lst[index] for sub_lst in lst]

def csv_to_dictionary(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = list(reader)
        output = {}
        
        for index in range(len(header)):
            output[header[index]] = nth_element_of_lst(data, index)
        
    return output
        
def lst_str_to_float(lst):
    for index in range(0, len(lst)):
        lst[index] = float(lst[index])
    return lst
    

###Sorting Data

def sort_by_condition(dict, key, value):
    output = {}
    for key1 in dict:
        output[key1] = []
    lst = dict[key]
    for index in range(len(lst)):
        if lst[index] == value:
            for key2 in dict:
                output[key2].append(dict[key2][index])
    return output

###Plotting Functions

def scatter_func_x_of_y(x, y, x_name, y_name, domain, range):
    plt.rcParams['figure.dpi'] = 100
    plt.figure(figsize=(10, 10))
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.xticks(rotation=90)
    plt.xlim(domain[0], domain[1])
    plt.ylim(range[0], range[1])
    plt.grid()
    plt.scatter(x, y)

def scatter_2_func_x_of_y(data_1, data_2, x_key, y_key, domain, range):
    plt.rcParams['figure.dpi'] = 100
    plt.figure(figsize=(10, 10))
    plt.xlabel(x_key)
    plt.ylabel(y_key)
    plt.xticks(rotation=90)
    plt.xlim(domain[0], domain[1])
    plt.ylim(range[0], range[1])
    plt.grid()
    plt.scatter(data_1[x_key], data_1[y_key], color=colors[0])
    plt.scatter(data_2[x_key], data_2[y_key], color=colors[1])
    plt.show()

def plot_func_x_of_y(x, y, x_name, y_name, domain, range):
    plt.rcParams['figure.dpi'] = 100
    plt.figure(figsize=(10, 10))
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.xticks(rotation=90)
    plt.xlim(domain[0], domain[1])
    plt.ylim(range[0], range[1])
    plt.grid()
    plt.plot(x, y)

def scatter_func(dataset, x_key, y_key, domain, range):
    scatter_func_x_of_y(dataset[x_key], dataset[y_key], x_key, y_key, domain, range)

def plot_func(dataset, x_key, y_key, domain, range):
    plot_func_x_of_y(dataset[x_key], dataset[y_key], x_key, y_key, domain, range)

###Curve Fitting Functions

def linear_fit(x, a, b):
    return x*a+b

###---------------------------------------------------------------------------------------------
###Variables

###All Data combined
data = csv_to_dictionary('insurance.csv')
data['age'] = lst_str_to_float(data['age'])
data['bmi'] = lst_str_to_float(data['bmi'])
data['children'] = lst_str_to_float(data['children'])
data['charges'] = lst_str_to_float(data['charges'])

###Children
data_0_child = sort_by_condition(data, 'children', 0)
data_1_child = sort_by_condition(data, 'children', 1)
data_2_child = sort_by_condition(data, 'children', 2)
data_3_child = sort_by_condition(data, 'children', 3)
data_per_child = [data_0_child, data_1_child, data_2_child, data_3_child]

###Sex
data_male = sort_by_condition(data, 'sex', 'male')
data_female = sort_by_condition(data, 'sex', 'female')
data_per_sex = [data_male, data_female]

###Smoker
data_smoker_true = sort_by_condition(data, 'smoker', 'yes')
data_smoker_false = sort_by_condition(data, 'smoker', 'no')
data_smoker = [data_smoker_false, data_smoker_true]

###Region
data_region_southwest = sort_by_condition(data, 'region', 'southwest')
data_region_northwest = sort_by_condition(data, 'region', 'northwest')
data_region_southeast = sort_by_condition(data, 'region', 'southeast')
data_region_northeast = sort_by_condition(data, 'region', 'northeast')
data_region = [data_region_northeast, data_region_southeast, data_region_southwest, data_region_northwest]

mean_charges_per_child = []
for data_lst in data_per_child:
    mean_charges_per_child.append(mean_value(data_lst['charges']))


### Found Variables

### linear aproximation of connection between number of children and the mean charges
values, covariance = curve_fit(linear_fit, [0, 1, 2, 3], mean_charges_per_child)
a_mean_charges_per_child, b_mean_charges_per_child = values
approximation_values_of_charges_per_child = []
for num in [0, 1, 2, 3]:
    approximation_values_of_charges_per_child.append(linear_fit(num, a_mean_charges_per_child, b_mean_charges_per_child))

###Standard Values
colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
charges_domain = [0, 65000]
age_domain = [20,65]
bmi_domain = [20, 50]


###---------------------------------------------------------------------------------------------
###Execution


###scatter_func(data_0_child, 'age', 'charges', age_domain, charges_domain)

###There appaers to be a connection between the number of children and the mean charges
###The second plot shows the y=ax+b approximation graph made using the curve_fit function from scipy

###plot_func_x_of_y([0, 1, 2, 3], mean_charges_per_child, 'number of children', 'mean charges', [0, 3], [12000, 16000])
###plot_func_x_of_y([0, 1, 2, 3], approximation_values_of_charges_per_child, 'number of children', 'mean charges', [0, 3], [12000, 16000])


###The 2 graphs below show really well that there is a big connections between smoking and charges

###scatter_2_func_x_of_y(data_smoker[0], data_smoker[1], 'age', 'charges', age_domain, charges_domain)
###scatter_2_func_x_of_y(data_smoker[0], data_smoker[1], 'bmi', 'charges', bmi_domain, charges_domain)
