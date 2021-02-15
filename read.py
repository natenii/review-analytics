data = []
# count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        # count += 1
        # if count % 1000 == 0:
        #     print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆資料')

new = []
#num = 0
for d in data:
    if len(d) < 100:
        #num += 1
        new.append(d)
print(len(new))
print(new[0])
#print('留言少於100字的有', num, '筆資料')