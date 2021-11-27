import locale
import pandas as pd
from preprocessor import refactoring_cleaner, selector, p_selector, summary
from connector import connection
import matplotlib.pyplot as plt
import json

# Establish connection with the DB and select table
# Selecting through following parameters: table name, column name and an optional specific query
con = connection.Connection()
query_content = con.select_column('text', 'old_text', 'WHERE old_id > 0 AND old_id < 500')
con.terminate_connection()


# Iterating the preprocessor functions over input_text and assigning the results to a new list.
# Parameters could be turned on/off e.g. text_cleaner.clean(x, newline=False)
input_text = refactoring_cleaner.unpack_tuple_into_list(query_content)
text_transformed = list(map(lambda x: refactoring_cleaner.clean(x), input_text))

ns_coordinates = list(map(lambda x: selector.find_ns_coordinates(x), input_text))
ew_coordinates = list(map(lambda x: selector.find_ew_coordinates(x), input_text))
coordinates = zip(ns_coordinates, ew_coordinates)
zipped_coordinates = list(coordinates)

article_title = list(map(lambda y: selector.find_title(y), text_transformed))
article_subheaders = list(map(lambda z: selector.find_subheader(z), text_transformed))
cleaned_subheaders = selector.clean_subheaders(article_subheaders)

article_summary = list(map(lambda x, y: summary.article_intro(x, y), text_transformed, article_title))


# Defining the dictionary that holds our two lists and that will form our new database with the preprocessed data
preprocessed_data = {
    'title': article_title,
    'article': text_transformed,
    'subheaders': cleaned_subheaders,
    'coordinates': zipped_coordinates,
    'intro': article_summary
}

# Creating a reprocessed_data_df DataFrame to hold our preprocessed data
preprocessed_data_df = pd.DataFrame.from_dict(preprocessed_data)
preprocessed_data_df['paragraphs'] = preprocessed_data_df.apply(
    lambda x: p_selector.paragrapher(x.subheaders, x.article), axis=1)
# nRow, nCol = preprocessed_data_df.shape
# print(f'There are {nRow} rows and {nCol} columns.')
#print(preprocessed_data_df['intro'].sample(n=5, random_state=1))


plt.xlabel("subheaders")
plt.ylabel("Counts")

preprocessed_data_df.subheaders.value_counts().plot(kind='bar')
#plt.show()

preprocessed_data_df.isnull().sum()

# title_df = preprocessed_data_df['title']
# title_df = title_df.to_frame()
# title_df.sample(10, random_state = 5)

titles = preprocessed_data_df[preprocessed_data_df.duplicated('title')]

print(titles['title'])
print(len(titles))

with open('output.txt', 'w') as opened_file:
    final = text_transformed[0]
    #opened_file.write("titel:" + article_title + "\n")
    opened_file.write(final)

# concatinate = [preprocessed_data_df['title'], preprocessed_data_df['article'], preprocessed_data_df['']]
# post_request_df = pd.concat()
# sample_df = preprocessed_data_df.sample(10, random_state = 5)

for_json = {
    'title': article_title,
    'latitude': ew_coordinates,
    'longitude': ns_coordinates,
    'introduction': article_summary
}

# for_json_df = pd.DataFrame.from_dict(for_json)

# #for_json_df = for_json_df[for_json_df.title != 'Unkown']

# to_json = for_json_df.to_json(orient='records')

# to_csv = for_json_df.to_csv('csv_sample.csv', encoding='utf-8')

# with open('json_sample.json', 'w', encoding='utf-8') as f:
#     json.dump(to_json, f, ensure_ascii=False, indent=4)



# print(sample_df)




# Reviewing the collation
loc = locale.getlocale()
print(loc)