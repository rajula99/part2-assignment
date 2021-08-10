import csv
f = input('Enter filename: ')
with open(f, newline='') as csvfile:
    freader = csv.reader(csvfile, delimiter=' ')
    lin = 0
    marks = list()
    subj = list()
    stud = list()
    d = dict()
    for row in freader:
        r =  row[0].split(',')
        #print(r)
        if lin == 0:
            for i in r[1:]:
                marks.append(0)
                subj.append(i)
                stud.append(None)
            lin += 1
            #print(subj)
            continue
     
        m = list(map(int, r[1:]))
        total = 0
        for i in range(len(m)):
            if m[i] > marks[i]:
                marks[i] = m[i]
                stud[i] = r[0]
            total += m[i]
        avg = total/len(m)
        name = r[0]
        d[name] = avg
    #print(marks, stud)

    for i in range(len(subj)):
        print('Topper in {} is {}'.format(subj[i],stud[i]))

    sorted_d = sorted(d.items(), key = lambda kv:(kv[1], kv[0]))
    #print(sorted_d)

    print('Best students in the class are ',sorted_d[-1][0], sorted_d[-2][0], sorted_d[-3][0])