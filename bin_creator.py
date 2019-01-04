import os
from collections import defaultdict
start = 0
steps = 1024*50
end = steps*100
for i in range(start,end,steps):
	with open(str(i)+".txt", 'w+') as f:
		content = list(map(lambda x: bin(x)[2:],list(range(i,i+steps))))
		f.write(str(",".join(content)))



# import os
# import csv
# from collections import defaultdict

# FILE_DIR = os.path.dirname(os.path.abspath("./"))


# def get_file_path(filename):
#     return os.path.join(FILE_DIR, filename)


# file_path = get_file_path('uk/query_result.csv')
# with open(file_path, 'rU') as csvfile:
#     reader = csv.reader(csvfile)
#     header = next(reader)
#     data = defaultdict(lambda:[""])
#     _ = data[header[0]]
#     for row in reader: 
#         data[row[0]].append(row[1])
#     for file_name, rows in data.items():
#         with open(file_name+".txt", 'w+') as f:
#             for row in rows:
#                 f.write(str(row) + '\n')