import pandas as pd
import numpy as np


Data=pd.read_excel("review_extraction.xlsx", sheet_name='Sheet1')

# print(Data)

review=[]
orgid="850a8b8f-a6fe-49e4-88fc-874843279d66"
pname="demo_holler_prod"
eventtype="review"
sku="demo_sku"
max_rating=5
doc_id="demo_holler_prod_"
count=0

for index, row in Data.iterrows():
    name=str(row[0])
    name=name.rstrip("\n").replace('\n','')
    date=str(row[1]).strip()
    rat=float(row[2])
    if np.isnan(rat):
        rating=3
    else:
        rating=rat
    detitle=str(row[3]).rstrip("\n").replace('\n',' ')
    dereview=str(row[4]).rstrip("\n").replace('\n',' ')
    entitle=str(row[5]).rstrip("\n").replace('\n',' ')
    enreview=str(row[6]).rstrip("\n").replace('\n',' ')
    recommend=str(row[7]).rstrip("\n")
    pdetails=str(row[8]).rstrip("\n")
    doc_id_s=doc_id+str(count)
    finaljs={"userid_s":name,
             "date_s":date,
             "rating_d":rating,
             "detitle_s":detitle,
             "dereview_s":dereview,
             "entitle_s":entitle,
             "review_txt":enreview,
             "recommend_s":recommend,
             "pdetails_s":pdetails,
             "orgId_s":orgid,
             "productname_s":pname,
             "event_type_s":eventtype,
             "sku_s":sku,
             "max_rating_d":max_rating,
             "doc_id_s":doc_id_s}
    # print(finaljs)
    review.append(finaljs)
    count+=1
    
print(review)
    