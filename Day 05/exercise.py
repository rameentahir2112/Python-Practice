# Exercise

# Level 1

# Task 1: Declare an empty list
empty_list = []

# Task 2: Declare a list with more than 5 items
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby', 'Go', 'SQL']

# Task 3: Find the length of your list
print('Length of languages list:', len(languages))

# Task 4: Get the first item, the middle item and the last item of the list
first_language = languages[0]
print('First language:', first_language)
middle_index = len(languages) // 2
middle_language = languages[middle_index]
print('Middle Language:', middle_language)
last_index = len(languages) - 1
last_language = languages[last_index]
print('Last Language:', last_language)

# Task 5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Rameen', 21, 5.4, False, 'xyz, Pakistan']

# Task 6: Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Task 7: Print the list using print()
print('IT Companies:', it_companies)

# Task 8: Print the number of companies in the list
print('Number of IT Companies:', len(it_companies))

# Task 9: Print the first, middle and last company
first_company = it_companies[0]
print('First company:', first_company)
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index]
print('Middle company:', middle_company)
last_index = len(it_companies) - 1
last_company = it_companies[last_index]
print('Last company:', last_company)
last_language = languages[last_index]
print('Last Language:', last_language)

# Task 10: Print the list after modifying one of the companies
it_companies[0] = 'Github'
print('Modified IT Companies List:', it_companies)

# Task 11: Add an IT company to it_companies
it_companies.append('Netsol')

# Task 12: Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Devsinc')

# Task 13: Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print('IT COMPANIES:', it_companies)

# Task 14: Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

# Task 15: Check if a certain company exists in the it_companies list.
does_exist = 'Google' in it_companies
print('Does Google exist in the list?', does_exist)

# Task 16: Sort the list using sort() method
it_companies.sort()
print('Sorted List:', it_companies)

# Task 17: Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print('Descending Order of List:', it_companies)

# Task 18: Slice out the first 3 companies from the list
first_three = it_companies[0:3]
print('First three companies:', first_three)

# Task 19: Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print('Last three companies:', last_three)

# Task 20: Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print('Middle Companies:', it_companies[middle_index - 1], 'and', it_companies[middle_index])
else:
    print('Middle Company:', it_companies[middle_index])

# Task 21: Remove the first IT company from the list
it_companies.remove(it_companies[0])

# Task 22: Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
it_companies.remove(it_companies[middle_index])

# Task 23: Remove the last IT company from the list
last_index = len(it_companies) - 1
it_companies.remove(it_companies[last_index])

# Task 24: Remove all IT companies from the list
it_companies.clear()

# Task 25: Destroy the IT companies list
del it_companies

# Task 26: Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# Task 27: After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
print('Full Stack:', full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

# Level 2:

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
max_age = max(ages)
min_age = min(ages)
# Add the min age and the max age again to the list
ages.append(max_age)
ages.append(min_age)
# Find the median age (one middle item or two middle items divided by two)
middle_index = len(ages) // 2
middle_age1 = ages[middle_index - 1]
middle_age2 = ages[middle_index]
# Find the average age (sum of all items divided by their number ) 
avg_age = sum(ages) / len(ages)
# Find the range of the ages (max minus min)
range = max_age - min_age
# Compare the value of (min - average) and (max - average), use abs() method
difference1 = abs(min_age - avg_age)
difference2 = abs(max_age - avg_age)
if difference1 > difference2:
    print('Difference 1 is greater')
elif difference1 < difference2:
    print('Difference 2 is greater')
else:
    print('Difference 1 and difference 2 are equal')

# 1. Find the middle country(ies) in the
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    print('Middle Countries:', countries[middle_index - 1], 'and', countries[middle_index])
else:
    print('Middle Country:', countries[middle_index])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
    print('First Half:', countries[0:middle_index])
    print('Second Half:', countries[middle_index::])
else:
    print('First Half:', countries[0:middle_index + 1])
    print('Second Half:', countries[middle_index + 1::])