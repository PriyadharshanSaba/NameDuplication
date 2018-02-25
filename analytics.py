import sys
import pandas as pd
global name_frame
global fname
global lname
global ufn
global record
#sys.path.append("/usr/local/lib/python3.6/site-packages")


def fetch_unique_records(ufn,name_frame,record):
    oj=0
    for i in ufn:
        if oj==0:
            first_name_check = i
            fname_group=dset[dset['fn']==first_name_check]['ln']
            lname_group=(fname_group.to_frame()).ln
            decision_tree_split(i.split(' '),lname_group,name_frame,record)
            oj+=1
        else:
            break


def decision_tree_split(fname,lname,name_frame,record):
    if len(fname) == 1:
                                                        #To check if the First name is unique or there are any initials that may map to a similar person already in records
        io=0
        for lname_split in lname:
            io+=1
            if len(lname_split.split(' ')) >= 2:           #Takes Name and following initials as one entity
                if not existence_rules(lname_split):
                    #record = record.append(name_frame.iloc[0])
                    db.append(name_frame.iloc[0].name)
                    name_frame=name_frame.iloc[1:]
                    lnameleft.append(list(lname_split.split()))
                    print(name_frame.iloc[0].name)
                else:
                    lnameright.append(list(lname_split.split()))
            else:
                if not lname_split in lnameleft:
                    db.append(name_frame.iloc[0].name)
                    name_frame=name_frame.iloc[1:]
                    lnameleft.append(lname_split)
                    print("\n\nrec\n",record)
                else:
                    lnameright.append(lname_split)



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


def dob(nam):
    name=""
    for i in nam:
        name=name+nam
    return True


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
                        if not dob(nam):
                            return False
        if exp==len(nam.split()):
            return True
        else:
            return False
    return False




dset = pd.read_csv('dset.csv')
record = pd.DataFrame(columns=['ln','dob','gn','fn'])
lnameleft, lnameright, db = list(), list(), list()
ufn = dset.fn.unique()
name_frame=dset.sort_values('fn')
ufn.sort()

print(name_frame)
fetch_unique_records(ufn,name_frame,record)



print("Left List:\n",lnameleft)
print("\nRight List:\n",lnameright)
print("\n\nrec\n",db)






#print("\n\nrec\n",record)

#first_name = input("First Name").upper()
#last_name = input("Last Name").upper()
#dob = name = input("DOB").upper()
#gender = input("Gender ( F | M )").upper()




#p.iterrows()
#len(df.index)
#names_dset= dset.values
#    y=dset.query("fn == 'WILLIAM'")['ln']
