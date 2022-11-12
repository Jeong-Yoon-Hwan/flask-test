import mariadb
import sys

try:
  conn = mariadb.connect(
    user="root",
    password="stock5861!",
    host="127.0.0.1",
    port=3316,
    database="stock586"
  )
except mariadb.Error as e:
  print(f"Error connecting to MariaDB platform:{e}")
  sys.exit(1)


cur = conn.cursor()

cur.execute(
  "select name,code,market from companylist limit 10"
)

arr = []
for (name,code,market) in cur:
  #print(f"name:{name},code:{code}") 
  #arr.append(f"name:{name},code:{code}")
  #print({'name':name,'code':code,'market':market})
  arr.append({'name':name,'code':code,'market':market})
conn.close()

print(arr)