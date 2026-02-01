import datetime
def get_date():
    return int(input("Enter date (DD) : "))
# d=date()    
def get_year():
    return int(input("Enter year (YYYY) : "))
# year=y()   
def get_month():
    return int(input("Enter month (1-12) : "))
def month_code(m,year): 
        if year%400==0 or (year%4==0 and year%100!=0):
            m_code=[0,3,4,0,2,5,0,3,6,1,4,6]
        else:
            m_code=[1,4,4,0,2,5,0,3,6,1,4,6]  
        
        mo=m_code[m-1]
        return mo
# print(mo)
# mo=month_code()
 
def l_2digit(year):         
    rem=year%100   
    return rem
# print(rem)
# rem=l_2digit()
def century_code(rem,year):
    x=year-rem
    y=x%400
    if y==0:
        c=0
    elif y==100:    
        c=5
    elif y==200:
        c=3
    elif y==300:
        c=1
    return c    
# c=century_code()
def div_last2(rem):
    n=rem/4
    a=int(n)
    return a
# print(a)         
   


# a=div_last2()
def day(d,mo,rem,c,a):
    da=d+mo+rem+c+a+5
    dayn=da%7
    return dayn
# print(day)

# day_name=day()
def match_day(day_name):
    if day_name==0:
        return "Sunday"
    elif day_name==1:
        return "Monday"
    elif day_name==2:
        return "Tuesday"
    elif day_name==3:
        return "Wednesday"
    elif day_name==4:
        return "Thursday"
    elif day_name==5:
        return "Friday"
    elif day_name==6:
        return "Saturday"                      
    else:
        return "Something Went Wrong"   
def gen_time():
    it=datetime.datetime.now()
    t=str(it)
    return t     
def make_file(d,m,year,md,t):
    d1=str(d)
    m1=str(m)   
    year1=str(year)
    file=str(d1+"."+m1+"."+year1)
    f=open(file+".txt","w")
    f.write("WEEKDAY DETERMINATION REPORT \n----------------------------- \nGiven Date : "+file+"\nDay : "+md+"\nGenerated on : "+t)

def insert_into_sql(d,m,year,md,t):
    import mysql.connector

    # MySQL se connection
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jaat@2010",
        database="da"
    )
    cursor=con.cursor()    
    d2=str(d)
    m2=str(m)
    y=str(year)
    x=d2+"."+m2+"."+y
    md1=str(md)
    t1=str(t)
    sql='''insert into date_day 
    values(%s,%s,%s)'''
    values=(x,md1,t1)
    cursor.execute(sql,values)
    con.commit()
    con.close()    
#Execution
d=get_date()
m=get_month()
if m>12: 
       print("Invalid input of month")
       exit()
year=get_year()

mo=month_code(m,year)
rem=l_2digit(year)
c=century_code(rem,year)
a=div_last2(rem)
day_name=day(d,mo,rem,c,a)
md=match_day(day_name)
t=gen_time()
make_file(d,m,year,md,t)
print("File Generated successfully✅")
insert_into_sql(d,m,year,md,t)
print("Data inserted successfully✅")
