# # create the merge() function and merge the one or more dataframes.
# import pandas as pd
# #used the merge() function.
# print(pd.merge(df1,df2, on='index'))
# print(pd.merge(df2,df1, on='index', how='left'))
# print(pd.merge(df2,df1, on='index', how='right'))
# print(pd.merge(df2,df1, on='index', how='outer', indicator=True))

# df3=pd.DataFrame({'index':[6,7,8,9],
#      'names':['appu','appi','appy','alpesh']
# })
# # used the left_index and right_index.
# print(pd.merge(df2,df3, left_index=True, right_index=True))

# # used the suffix and merge() function on the parameters.
# print(pd.merge(df2,df3, on='index', suffixes=('my_indxe', 'my_names')))

# create the concat() function on the parameters and used the various parameters inside the function.
import pandas as pd
# df=pd.Series([1,2,3,4])
# print(df)
# df1=pd.Series([1,2,3,4,5])
# print(df1)
# # used the concat() function.
# df2=pd.concat([df1,df])
# df3=pd.DataFrame({'index':[1,2,3,4],
#      'boys':['appu','appi','appy','ap']
# })
# df4=pd.DataFrame({'index':[1,2,3,4],
#      'boys':['appu','appi','appy','ap']
# })
# # df4=pd.concat([df4,df3], axis=1)
# # print(df4)
# df5=pd.concat([df3,df4], axis=0, ignore_index=True)
# print(df5)
# create the concat() function and using the axis, no_axis and sort parameters.
# print(pd.concat([df3,df4], axis=1))
# # df5=pd.concat([df3, df4],axis=1, join_axes=[df4.index])
# # print(df5)
# # used the key parameter.
# print(pd.concat([df3, df4], axis=0, keys=['appu', 'appi']))
# # used the sort parameters.
# print(pd.concat([df3, df4], sort=False))

#join() function.
# the join function is the combining the the two dataframes in different indexes.
import pandas as pd
df3=pd.DataFrame({'name':[1,2,3,4],
     'boys':['appu','appi','appy','ap']
},index=[12,13,14,15])
df4=pd.DataFrame({'name':[1,2,3,4],
     'girls':['appu','appi','appy','ap']
}, index=[12,13,14,15])
print(df3, df4)
# used the join function.
# print(df3.join(df4,how='outer'))
# # print(pd.display(df3,df4))
# # print(df3.display(df4))

# print(df3.join(df4, lsuffix='_1'))
# print(df3.join(df4, rsuffix='_my'))
# used the append() function.
print(df3, df4)
print(df3.append(df4))
# pandas append() function used to append the row of dataframe to other dataframe rows, returning the dataframe object.
print(df4.append(df3, ignore_index=False, sort=False))