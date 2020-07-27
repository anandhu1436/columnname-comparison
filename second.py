import os
import sys
import pandas as pd
from pandas.io.parsers import ParserError

def readdf(arr0):    
    ar1=arr0#if you want enter custompath for file1 here instead of arr[0]
    if ar1.endswith('.xlsx') or ar1.endswith('.xls'):
        df1=pd.read_excel(ar1)
    elif ar1.endswith('.txt'):
            try:
                    df1=pd.read_csv(ar1,sep="|")	#change delimeter here
            except ParserError:
                    df1=pd.read_csv(ar1,sep="|",nrows=5) #change delimeter here
    else:
        df1=pd.read_csv(ar1)
        
    c1=df1.columns
    c2=df2.columns
    e1=[]
    e2=[]
    for i in c1 :
        if i not in c2:
            e1.append(i)
          
    for i in c2 :
        if i not in c1:
            e2.append(i)
    if len(e1)!=0:
            df1=df1[[k for k in e1]]
            df1['file name']=ar1
    if len(e2)!=0:
            df2=df2[[k for k in e2]]
            df2['file name']=ar2

    return e1,e2


#reading input from config.txt 
config_path = "config.txt"#path of config.txt
dff=pd.read_csv(config_path,sep='-')
data=dff[dff.columns[1]]
data=list(data)

out=[]
val=[]

val2=[]
lis2=[]
mon=data[1].split(",")
for m in mon:
    
    path1=data[0]+"\\"+m
    file1 = os.listdir(path1)
    
    for f1 in file1:
        val.append(f1)
        lis=[]
        
        for k in mon:
            
            countf=0
            
            if k!=m:
                
                path2=data[0]+"\\"+k
                file2=os.listdir(path2)
                fil1 = ''.join([i for i in f1.split('.')[0] if not i.isdigit()])
                
                for f2 in file2:
                    fil2 = ''.join([i for i in f2.split('.')[0] if not i.isdigit()])
                    if fil1==fil2:
                        lis.append([f1,m,f2,k])
                lis2.append(lis)
                    
                
                
                       
        
                      
        
    
    

'''        
    f=open("out.txt","w")
    for k in e1:
            f.write(k+",")
    f.write("--"+ar1+"\n")
    for k in e2:
            f.write(k+",")
    f.write("--"+ar2)
    f.close()
    writer=pd.ExcelWriter('out.xlsx',engine='xlsxwriter') 
    if len(e1)!=0:
            df1.to_excel(writer,sheet_name='sheet1')
    if len(e2)!=0:
            df2.to_excel(writer,sheet_name='sheet2')
    writer.save()	
'''	
    



