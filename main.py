import locale
import pandas as pd
from preprocessor import cleaner, paragraph_selector, selector, summary, title_transformation_for_mediawiki_api
from connector import connection, db_creation
from api import wiki_versioning
from api import mediawiki_api
import matplotlib.pyplot as plt
import json
import uuid
import pprint
import sqlalchemy



                                                                        ###     Connection     ###

# Establish connection with the DB and select table
# Selecting through following parameters: table name, column name and an optional specific query
con = connection.Connection()
query_content = con.select_column('text', 'old_text', 'WHERE old_id > 4000 AND old_id < 4005')
#con.terminate_connection()



                                                                        ###     Preprocessing     ###

# Iterating the preprocessor functions over input_text and assigning the results to a new list.
# Parameters could be turned on/off e.g. text_cleaner.clean(x, newline=False)
input_text = cleaner.unpack_tuple_into_list(query_content)
text_transformed = list(map(lambda x: cleaner.clean(x), input_text))

ns_coordinates = list(map(lambda x: selector.find_ns_coordinates(x), input_text))
ew_coordinates = list(map(lambda x: selector.find_ew_coordinates(x), input_text))
coordinates = zip(ns_coordinates, ew_coordinates)
zipped_coordinates = list(coordinates)

article_title = list(map(lambda y: selector.find_title(y), text_transformed))
wiki_url_title = list(map(lambda y: title_transformation_for_mediawiki_api.wiki_appropriate_title(y), article_title))

article_subheaders = list(map(lambda z: selector.find_subheader(z), text_transformed))
cleaned_subheaders = selector.clean_subheaders(article_subheaders)

categories = list(map(lambda x, y: selector.category_finder(x, y), text_transformed, article_title))

article_summary = list(map(lambda x, y: summary.article_intro(x, y), text_transformed, article_title))

change_is_minor = list(map(lambda x: wiki_versioning.find_if_minor(x), wiki_url_title))



                    ###     Defining the dictionary that holds our two lists and that will form our new database with the preprocessed data     ###

preprocessed_data = {
    'title': article_title,
    'wiki_title': wiki_url_title,
    'article': text_transformed,
    'categories': categories,
    'subheaders': cleaned_subheaders,
    'coordinates': zipped_coordinates,
    'intro': article_summary,
    'latest update is minor': change_is_minor
}

print(type(preprocessed_data['coordinates']))
# for_excel = {
#     'title': article_title,
#     'wiki_title': wiki_url_title,
#     'categories': categories,
#     'coordinates': zipped_coordinates,
#     'article': text_transformed
# }

# to_excel = pd.DataFrame.from_dict(for_excel)
# to_excel.to_excel('4000_4559.xlsx', sheet_name='categories')



                                        ###     Creating a preprocessed_data_df DataFrame to hold our preprocessed data     ###

preprocessed_data_df = pd.DataFrame.from_dict(preprocessed_data)
preprocessed_data_df['paragraphs'] = preprocessed_data_df.apply(
    lambda x: paragraph_selector.paragrapher(x.subheaders, x.article), axis=1)

# preprocessed_data_df['category'] = preprocessed_data_df.apply(
#     lambda x: selector.category_finder(x.article), axis=1)
# nRow, nCol = preprocessed_data_df.shape
# print(f'There are {nRow} rows and {nCol} columns.')
#print(preprocessed_data_df['category'].sample(n=5, random_state=1))

#print(preprocessed_data_df)



                                                                         ###     Setting IDs     ###

# preprocessed_data_df['wiki_id'] = preprocessed_data_df.apply(
#     lambda x: mediawiki_api.get_id(x.title), axis=1)
# id_dict = dict(zip(preprocessed_data_df.title, preprocessed_data_df.wiki_id))


# #print(id_dict)
# # print(preprocessed_data_df['wiki_id'])
# titles = preprocessed_data_df['title'].unique()
# for title in titles:
#     preprocessed_data_df.loc[preprocessed_data_df['title'] == title, 'UUID'] = uuid.uuid4()

# #print(preprocessed_data_df['title'], preprocessed_data_df['categories'])
# dict_ready_for_db = preprocessed_data_df.to_dict(orient='dict')
# #print(dict_ready_for_db)



#                                                                  ###     inserting into middle DB     ###

print(type(preprocessed_data_df['title']))

# convert = preprocessed_data_df['coordinates']

# engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/test?charset=utf8mb4")

# convert.to_sql('overview', engine, index=False)

# out_connection = db_creation.OutgoingConnection()
# insert_into_outdb = out_connection.insert(dict_ready_for_db.values())



#                                                                           ###     Plotting    ###

# plt.xlabel("subheaders")
# plt.ylabel("Counts")
# preprocessed_data_df.subheaders.value_counts().plot(kind='bar')
# # plt.show()
# preprocessed_data_df.isnull().sum()
# # title_df = preprocessed_data_df['title']
# # title_df = title_df.to_frame()
# # title_df.sample(10, random_state = 5)
# # titles = preprocessed_data_df[preprocessed_data_df.duplicated('title')]
# # print(titles['title'])
# # print(len(titles))
# # print(preprocessed_data_df)



#                                                                   ###     Saving into external files     ###

# with open('output.txt', 'w') as opened_file:
#     final = text_transformed[0]
#     #opened_file.write("titel:" + article_title + "\n")
#     opened_file.write(final)
# # concatinate = [preprocessed_data_df['title'], preprocessed_data_df['article'], preprocessed_data_df['']]
# # post_request_df = pd.concat()
# # sample_df = preprocessed_data_df.sample(10, random_state = 5)



#                                                                   ###     Dict for Json (for Nisnab)     ###

# for_json = {
#     'title': article_title,
#     'latitude': ew_coordinates,
#     'longitude': ns_coordinates,
#     'introduction': article_summary
# }

# # for_json_df = pd.DataFrame.from_dict(for_json)
# # #for_json_df = for_json_df[for_json_df.title != 'Unkown']
# # to_json = for_json_df.to_json(orient='records')
# # to_csv = for_json_df.to_csv('csv_sample.csv', encoding='utf-8')
# # with open('json_sample.json', 'w', encoding='utf-8') as f:
# #     json.dump(to_json, f, ensure_ascii=False, indent=4)




#                                                                   ###     Reviewing the collation     ###

# loc = locale.getlocale()
# print(loc)