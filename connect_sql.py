__author__ = 'Administrator'
import pymysql
def abc(abc):
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='yuzhixiang')
    cursor=conn.cursor()
    sql='insert into `ceshi`(company,position,salary,region,address,experience,education,number,time,Job_highlights,job_requirements) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    cursor.execute(sql,abc)
    conn.commit()
    print('插入成功')
    conn.close()
    cursor.close()
