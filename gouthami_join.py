import pprint

t1_attributes = ('Student_ID', 'Year_Of_Birth', 'Depatment','Mother_tongue')
t2_attributes = ('Grade', 'Student_name', 'Student_ID','Gender')

t1_tuples = [
    [200555, '2002', 'Computer Science','Telugu'],
    [200558, '2003', 'Physics',         'Telugu'],
    [200567, '2002', 'Mathematics',     'Gujarati'],
    [200245, '2002', 'EVS',             'Malayalam'],
    [200198, '2002', 'Mathematics',     'Tamil']]

t2_tuples = [
     ['A', 'Vijayasree', 200555, 'Female'],
     ['O', 'Gouthami',   200558, 'Female'],
     ['B', 'Avval',      200567, 'Male'],
     ['A', 'Sridivya',   200245, 'Female'],
     ['O', 'Prem',       200198, 'Male']]


t1_columns = set(t1_attributes)
t2_columns = set(t2_attributes)
t1_map = {k: i for i, k in enumerate(t1_attributes)}
t2_map = {k: i for i, k in enumerate(t2_attributes)}

join_on = t1_columns & t2_columns
diff = t2_columns - join_on

def match(row1, row2):
   return all(row1[t1_map[rn]] == row2[t2_map[rn]] for rn in join_on)
results = []
for t1_row in t1_tuples:
    for t2_row in t2_tuples:
        if match(t1_row, t2_row):
            row = t1_row[:]
            for rn in diff:
                row.append(t2_row[t2_map[rn]])
            results.append(row)

pprint.pprint(results)