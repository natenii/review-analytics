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
for d in data:
    if len(d) < 100:
        new.append(d)
print(len(new))
print(new[0])
print('留言少於100字的有', len(new), '筆資料')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('留言裡有good的有', len(good), '筆資料')
print(good[0])