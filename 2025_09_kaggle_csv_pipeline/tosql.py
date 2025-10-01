# import pymysql
# import pandas as pd

# # DB 연결을 위한 정보 입력
# conn = pymysql.connect(host='localhost', user='root', db='titanicDB', password='1234')

# # DB 연결
# cur = conn.cursor()

# # 읽을 파일 불러오기
# data = pd.read_csv('train_new.csv')

# # 엑셀 데이터가 파이썬으로 넘어왔는지 확인
# print(data)

# # DB에 들어갈 sql문 작성
# data = data.where(pd.notnull(data), None)
# sql = 'INSERT INTO titanictbl (PassengerId,Survived,Pclass,`Name`,Sex,Age,SibSp,Parch,Ticket,Fare,Embarked,Name_length) VALUES (%d, %d, %d, %s, %s, %d, %d, %d, %s, %f, %s, %d)'

# # 엑셀에 많은 양을 반복문을 돌려서 전부 꺼내기
# for idx in range(len(data)):
#     cur.execute(sql, tuple(data.values[idx]))

# # DB에 저장
# conn.commit()

# # 완료되었으면 닫기
# cur.close()
# conn.close()

import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', db='titanicDB', password='1234', charset='utf8mb4')
cur = conn.cursor()

data = pd.read_csv('train_new.csv')

# NaN -> None (MySQL NULL)
data = data.where(pd.notnull(data), None)

# 모두 %s로 (숫자/문자 구분 안 함)
sql = '''INSERT INTO titanictbl
    (PassengerId, Survived, Pclass, FullName, Sex, Age, SibSp, Parch, Ticket, Fare, Embarked, Name_length)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

# 빠르고 안전한 반복 (튜플을 직접 넘김)
for row in data.itertuples(index=False, name=None):
    cur.execute(sql, row)

conn.commit()
cur.close()
conn.close()