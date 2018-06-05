import pandas as pd
import re
# import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

def logg_import(fail_update,file_name):
    pass
    # videofile=f'chart_video_log/v'+str(file_name)+'.log'
    # # videofile=file_name
    # data2=pd.read_fwf(videofile)
    # data2.tail()
    # data=(data2.iloc[:,:2])
    # data.columns=["time","comment"]
    # video_num=int(re.findall(r'\d+',videofile)[0])
    # new_time=data.time.str.replace(']'  ,"")
    # new_time2=new_time.str.replace('[' ,"")
    # new_time_col=pd.to_timedelta(new_time2)
    # working_df=pd.concat([data,new_time_col],axis=1)
    # working_df_v2=working_df.iloc[:,1:]
    # working_df_v2['seconds']=working_df_v2.time.apply(lambda row:  (row.total_seconds()))
    # working_df_v3=(working_df_v2)
    # working_df_v3.head()
    # group_seconds=pd.DataFrame(working_df_v3.groupby(['seconds']).agg(['count']))
    # group_seconds_v2=group_seconds.reset_index()
    # group_seconds_v3=group_seconds_v2.iloc[:,:2]
    # group_seconds_v3.columns=['seconds','counts']
    # group_seconds_v3.head()
    # df4 = pd.DataFrame(working_df_v3.comment.str.split('>',1).tolist(),
    #                                    columns = ['user','comment'])
    # df5=working_df_v3.iloc[:,1:]
    # df6=pd.concat([df4,df5], axis=1)
    # df7 = pd.DataFrame(df6.groupby(['time'])['comment'].apply(list)).reset_index()
    # df8=df7.set_index('time')
    # df8.head()
    # df9=df8.resample('30s', how=sum)
    # df9['str_comments']=df9.comment.apply(lambda row:  str(row))
    # df10= df9.drop(["comment"], axis=1)
    # df11=pd.DataFrame(df10.str_comments.str.lower())
    # df12=pd.DataFrame(df11.str_comments.str.replace(r'ninja', ''))
    # df12.str_comments.replace(r'crinja','', regex=True,inplace=True )
    # df12.str_comments.replace(r'creep','', regex=True,inplace=True )
    #
    # df12.str_comments.replace(r'[^a-zA-Z\s]','', regex=True,inplace=True )
    # (df12)
    # plot_video_comments=working_df_v3.copy()
    # plot_video_comments['number']=1
    # plot_video_comments_v2=plot_video_comments.set_index('time')
    # plot_video_comments_v3=plot_video_comments_v2.resample('30s', how=sum)
    # plot_video_comments_v3['interval']=[i for i in range(len(plot_video_comments_v3))]
    # plot_video_comments_v3.head()
    #
    # fail_1=fail_update
    # fail_2= fail_1*30
    # # plt.figure(figsize=(30,7))
    # # plt.fill(plot_video_comments_v3.interval,plot_video_comments_v3.number)
    # # plt.axvline(x=fail_1 , color='red')
    # # print('chart output')
    # # plt.show()
    # return group_seconds_v3



def logg_import2(fail_update,file_name):
    videofile='chart_video_log/v'+str(file_name)+'.log'
    # videofile=file_name
    data2=pd.read_fwf(videofile)
    data2.tail()
    data=(data2.iloc[:,:2])
    data.columns=["time","comment"]
    video_num=int(re.findall(r'\d+',videofile)[0])
    new_time=data.time.str.replace(']'  ,"")
    new_time2=new_time.str.replace('[' ,"")
    new_time_col=pd.to_timedelta(new_time2)
    working_df=pd.concat([data,new_time_col],axis=1)
    working_df_v2=working_df.iloc[:,1:]
    working_df_v2['seconds']=working_df_v2.time.apply(lambda row:  (row.total_seconds()))
    working_df_v3=(working_df_v2)
    working_df_v3.head()
    group_seconds=pd.DataFrame(working_df_v3.groupby(['seconds']).agg(['count']))
    group_seconds_v2=group_seconds.reset_index()
    group_seconds_v3=group_seconds_v2.iloc[:,:2]
    group_seconds_v3.columns=['seconds','counts']
    group_seconds_v3.head()
    df4 = pd.DataFrame(working_df_v3.comment.str.split('>',1).tolist(),
                                       columns = ['user','comment'])
    df5=working_df_v3.iloc[:,1:]
    df6=pd.concat([df4,df5], axis=1)
    df7 = pd.DataFrame(df6.groupby(['time'])['comment'].apply(list)).reset_index()
    df8=df7.set_index('time')
    df8.head()
    df9=df8.resample('30s', how=sum)
    df9['str_comments']=df9.comment.apply(lambda row:  str(row))
    df10= df9.drop(["comment"], axis=1)
    df11=pd.DataFrame(df10.str_comments.str.lower())
    df12=pd.DataFrame(df11.str_comments.str.replace(r'ninja', ''))
    df12.str_comments.replace(r'crinja','', regex=True,inplace=True )
    df12.str_comments.replace(r'creep','', regex=True,inplace=True )
    df12.str_comments.replace(r'[^a-zA-Z\s]','', regex=True,inplace=True )
    (df12)
    df12.str_comments[1]
    plot_video_comments=working_df_v3.copy()
    plot_video_comments['number']=1
    plot_video_comments_v2=plot_video_comments.set_index('time')
    plot_video_comments_v3=plot_video_comments_v2.resample('30s', how=sum)
    plot_video_comments_v3['interval']=[i for i in range(len(plot_video_comments_v3))]
    plot_video_comments_v3.head()

    fail_1=fail_update
    fail_2= fail_1*30
    # tfidf_vectorizer = TfidfVectorizer(min_df=.1, max_df=.9, stop_words='english', token_pattern="\\b[a-z][a-z]+\\b")

    with open("vect.pkl",'rb') as picklefile:
        tfidf_vectorizer=pickle.load(picklefile)


    # tfidf_matrix = tfidf_vectorizer.fit_transform(df12.str_comments)
    tfidf_matrix = tfidf_vectorizer.transform(df12.str_comments)

    tfidf_feature_names = tfidf_vectorizer.get_feature_names()


    with open("nmf.pkl",'rb') as picklefile:
        nmf=pickle.load(picklefile)
    # nmf = NMF(n_components=32, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf_matrix)
    tfidf_matrix.toarray()
    tfidf_matrix.shape
    matrix_topics_nmf=nmf.transform(tfidf_matrix)
    topics_outcome_nmf=[np.argmax(row) for row in matrix_topics_nmf]

    #cosmetic
    topics_outcome_df_nmf=pd.DataFrame(topics_outcome_nmf)
    topics_outcome_df_nmf=topics_outcome_df_nmf.rename(columns={0:'outcome'})

    #join them more cosmeticv

    matrix_topics_nmf_df=pd.DataFrame(matrix_topics_nmf)
    final_nmf=matrix_topics_nmf_df.join(topics_outcome_df_nmf, lsuffix='index',rsuffix='index')
    final_nmf.head()
    # final_nmf['index2']=final_nmf.index  # for the plot
    final_nmf.outcome
    #Validation of created groups.
    plot_video_comments_v4 = plot_video_comments_v3.number.reset_index()
    #Join both Comment frequency in time with  created groups!! Final DF ready to analyze.
    validate_groups = plot_video_comments_v4.join(final_nmf.outcome)
    validate_groups.outcome[(validate_groups.outcome!=8) & (validate_groups.outcome!=0) & (validate_groups.outcome!=10)]=np.nan

    # test to see if chosen categories have higher values then rest of the categories.

    # categories filtered for selected features.
    validate_groups_v1 = validate_groups[(validate_groups.outcome == 0)
                                         | (validate_groups.outcome == 8)
                                         | (validate_groups.outcome == 10)]

    #Remove Selected features from Initial groups.
    validate_groups_v2 = validate_groups[(validate_groups.outcome != 0)]
    validate_groups_v3 = validate_groups_v2[(validate_groups.outcome != 8)]
    validate_groups_v4 = validate_groups_v3[(validate_groups.outcome != 10)]

    #Compare Groups ratios based on comments mean!!

    # return validate_groups_v1,df12.str_comments[1]
    return validate_groups,[i for i in df12.str_comments],plot_video_comments_v3
# logg_import(100,262826551)
# 263708483
# # 262826551
# print(logg_import2(199,263708483))
