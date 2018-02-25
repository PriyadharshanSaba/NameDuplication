import sys
import pandas as pd
global name_frame
global fname
global lname
global ufn
global fin
#sys.path.append("/usr/local/lib/python3.6/site-packages")


def fetch_unique_records(ufn,name_frame,record):
    oj=0
    for i in ufn:
        if oj==0:
            first_name_check = i
            fname_group=name_frame[name_frame['fn']==first_name_check]['ln']
            lname_group=(fname_group.to_frame()).ln
            decision_tree_split(i.split(' '),lname_group,name_frame,record)
            oj+=0
        else:
            break


#To check if the First name is unique or there are any initials that may map to a similar person already in records
def decision_tree_split(fname,lname,name_frame,record):
    if len(fname) == 1:
        io=0
        for lname_split in lname:
            io+=1
            current=name_frame.iloc[0].name                 #Current index
            if len(lname_split.split(' ')) >= 2:           #Takes Name and following initials as one entity
                if not existence_rules(lname_split):
                    db.append(current)
                    record = record.append(name_frame.iloc[0])
                    name_frame=name_frame.iloc[1:]
                    lnameleft.append(list(lname_split.split()))
                else:
                    #name_frame=name_frame.iloc[1:]
                    if not dob(lname_split.split(),current,name_frame,record):
                        dob(lname_split,current,name_frame,record)
                        name_frame=name_frame.iloc[1:]
            else:
                #print("\n\nREC\n",record)
                q=record[record['ln'] == lname_split].values
                if len(q)==0:
                    db.append(current)
                    record = record.append(name_frame.iloc[0])
                    name_frame=name_frame.iloc[1:]
                    lnameleft.append(lname_split)
                else:
                    lnameright.append(lname_split)
                    if not dob(lname_split,current,name_frame,record):
                        db.append(current)
                        record = record.append(name_frame.iloc[0])
                        name_frame=name_frame.iloc[1:]
                    else:
                        name_frame=name_frame.iloc[1:]
    with open('records.csv', 'a') as f:
        record.to_csv(f,header=False)




def existence_rules(xname):
    leng=len(xname.split())
    if leng==1:                                                     #length of the Last name
        dfx = pd.DataFrame({'ln':lnameleft})
        if not presence(xname):
            return True
        elif xname[:1] in df['ln'].astype(str).str[2]:
            return True
        else:
            return False
    else:
        dfx = pd.DataFrame({'ln':lnameleft})
        if not presence(xname):
            return False
        else:
            return True


#FUNCTION decides by classifying withrespect to gender and DOB
def dob(nam,indx,name_frame,record):
    current_c=dset.iloc[indx]
    try:
        rec= record.loc[record['ln'] == nam]
        x=rec['ln'].values[0]
        #    return current_c['dob'],rec['dob'].values[0]
        if current_c['dob']==rec['dob'].values[0] and current_c['gn']==rec['gn'].values[0]:
            return True
        else:
            return False

    except:
        return True

#print("\n>>>>>>>>>>>",x,current_c['dob'],"\n------------------------")



def presence(nam):
    exp=0
    if len(lnameleft)==0:
        return False
    else:
        for i in lnameleft:
            for j in nam.split():
                for k in i:
                    if k == j:                                      #splits the last name and follows the decision tree
                        exp+=1
                        continue
                    elif k[0] == j[0]:
                        return False
        if exp==len(nam.split()):
            return True
        else:
            return False
    return False


def remove_duplicates(db,dset):
    pdf = pd.DataFrame(columns=['ln','dob','gn','fn'])
    for i in db:
        pdf.append(dset.iloc[i])
    print(pdf)
    return 0



dset = pd.read_csv('dset.csv')
record = pd.DataFrame(columns=['ln','dob','gn','fn'])
pdf = pd.DataFrame(columns=['ln','dob','gn','fn'])
lnameleft, lnameright, db = list(), list(), list()
with open('records.csv', 'w') as f:
    record.to_csv(f,header=True)

ufn = dset.fn
ufn= ufn.drop_duplicates()
name_frame=dset.sort_values('fn')
fetch_unique_records(ufn,name_frame,record)
db=list(set(db))
print(ufn)
print(db)
for i in db:
    pdf=pdf.append(dset.iloc[i])
print(pdf)




