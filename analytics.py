import sys
import pandas as pd

#sys.path.append("/usr/local/lib/python3.6/site-packages")


def fetch_unique_records():
    fname = dset.iloc[:,3:4]
    lname = dset.iloc[:,:1]
    ufn = dset.fn.unique()
    name_frame=pd.concat([fname,lname], axis=1) #concating the dataframe columns
    j=0
    for i in ufn:
        if j==0:
            first_name_check = i
            fname_group=dset[dset['fn']==first_name_check]['ln']
            #fname_group=dset[dset['fn']=='WILLIAM']['ln']
            lname_group=(fname_group.to_frame()).ln
    #        print (fname_group)
            decision_tree_split(j,i.split(' '),lname_group)
            j+=1
        else:
            break


def decision_tree_split(index,fname,lname):
    temp_list = list()
    if len(fname) == 1:
        for lname_split in lname:
            if len(lname_split.split(' ')) >= 2:
                #                if not lname_split in lnameleft :
                if not existence_rules(lname_split):
                    lnameleft.append(list(lname_split.split()))
                else:
                    lnameright.append(lname_split)
            else:
                continue


def existence_rules(xname):
    #df['lname'] = df['First'].astype(str).str[0]
    #print(df['ln'].astype(str).str[2])

    leng=len(xname.split())
    if leng==1: #length of the Last name
        dfx = pd.DataFrame({'ln':lnameleft})
        if xname in lnameleft:
            return True
        elif xname[:1] in df['ln'].astype(str).str[2]:
            return True
        else:
            return False

    else:
        #print(">>>>>>>>>>>>\t\t",xname)
        dfx = pd.DataFrame({'ln':lnameleft})
        print(dfx)
        for i in xname.split():
            if i in lnameleft:
                return True
            elif i[:1] in dfx['ln'].astype(str).str[2]:
                return True
            else:
                return False

def dob():


dset = pd.read_csv('dset.csv')
record = pd.DataFrame(columns=['ln','dob','gn','fn'])
lnameleft, lnameright = list(), list()

fetch_unique_records()
print("Left List:\n",lnameleft)
print("\nRight List:\n",lnameright)




#first_name = input("First Name").upper()
#last_name = input("Last Name").upper()
#dob = name = input("DOB").upper()
#gender = input("Gender ( F | M )").upper()




#p.iterrows()
#len(df.index)
#names_dset= dset.values
#    y=dset.query("fn == 'WILLIAM'")['ln']
