import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

## 1. train.csv 파일 읽기
train = pd.read_csv('train.csv')

## 2. 데이터 기본 구조 확인
#train.head()
#train.tail()
#train.info()
#train.describe()

## 3. 결측치 확인 및 처리
# print(train.isnull().sum()) # Age와 Cabin에 결측치 확인됨.

# 결측치 처리 방법 결정 (`dropna`, `fillna`)
# Cabin은 결측치의 비율이 매우 크기 때문에 drop
train = train.drop(columns=['Cabin'])
# Age는 평균 값으로 채우기
train['Age'] = train['Age'].fillna(train['Age'].mean())
# Embarked는 최빈값으로 채우기
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])
# 처리 전/후 row 수 비교
print(train.isnull().sum())

## 4. 데이터 타입 확인 및 변환
print("📌 데이터 타입")
print(train.dtypes, "\n")
# Pclass 범주형으로 변환
train['Pclass'] = train['Pclass'].astype('category')

## 5. 중복 데이터 확인 및 제거
# - df.duplicated().sum()
# - drop_duplicates()
print("📌 중복 데이터 개수:", train.duplicated().sum(), "\n") # 중복 없음

## 6. 기초 통계/분포 확인
# - describe()
# - hist()
# - boxplot()
# - value_counts()
# - 이상치 여부 메모
# =====================================================
# # Age 분포
# train['Age'].hist(bins=20)
# plt.title("Age Distribution")
# plt.show()
# # Pclass별 Age 분포 (박스플롯)
# sns.boxplot(x='Pclass', y='Age', data=train)
# plt.title("Age by Pclass")
# plt.show()
# # Embarked 값 개수
# print("📌 Embarked Value Counts")
# print(train['Embarked'].value_counts(), "\n")

## 7. 변수 간 관계 분석
# - groupby()
# - corr()
# - heatmap()
# =====================================================
# # 성별 생존률
# print("📌 성별 생존률")
# print(train.groupby('Sex')['Survived'], "\n")
# # Pclass별 생존률
# print("📌 Pclass별 생존률")
# print(train.groupby('Pclass')['Survived'], "\n")
# # 상관관계 & 히트맵
# corr = train.corr(numeric_only=True)
# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()

## 8. 데이터 변환 및 가공
# - apply, map
# - merge, concat
# - sort_values
# =====================================================
# 이름 길이 컬럼 추가
train['Name_length'] = train['Name'].apply(len)
print(train[['Name', 'Name_length']].head(), "\n")
# # 데이터 정렬 (Age 기준 내림차순)
# df_sorted = train.sort_values(by='Age', ascending=False)
# print("📌 나이 많은 순")
# print(df_sorted[['Name', 'Age']].head(), "\n")
# # concat 예시 (앞 3행 + 뒤 3행)
# df_concat = pd.concat([train.head(3), train.tail(3)])
# print("📌 concat 예시")
# print(df_concat, "\n")

# ## 9. 고급 인덱싱
# # - set_index()
# # - reset_index()
# # =====================================================
# # PassengerId를 인덱스로 설정
# df = train.set_index('PassengerId')
# print("📌 인덱스 설정 후")
# print(df.head(), "\n")
# # 다시 reset_index
# df = df.reset_index()

## 10. 시각화 & 인사이트 기록
# - Matplotlib + Seaborn 활용
# - 각 시각화 결과 해석 메모
# =====================================================
# # 성별/등급별 생존률 시각화
# sns.barplot(x='Sex', y='Survived', hue='Pclass', data=train)
# plt.title("Survival Rate by Sex and Pclass")
# plt.show()

# 👉 인사이트 메모 예시:
# - 여성 생존률이 남성보다 확연히 높음
# - 1등석 승객의 생존률이 높음

## 11. to_csv(새롭게 저장)
train.to_csv("train_new.csv", index = False)