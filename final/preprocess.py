import csv
import os
import re

data_dir = '/Users/michaelspector/projects/data/expertise-modeling/arxiv_data'

# Overwrite the data files
with open('./corpus-labels.csv','wb') as y, open('./corpus-abstracts.csv','wb') as z:
    pass

with open('./corpus-abstracts.csv','ab') as x, open('./corpus-labels.csv','ab') as y:
    for path in ['%s/papers_%s.csv' % (data_dir, year) for year in ['2012','2013','2014','2015','2016']]:
        with open(path) as f:
            reader = csv.reader(f)
            abstracts_writer = csv.writer(x,delimiter='\n')
            labels_writer = csv.writer(y,delimiter='\n')

            for paper in reader:
                abstract = paper[2]
                abstract = re.sub('[^a-z]+', ' ', abstract.lower())

                if not 'has been withdrawn' in abstract:
                    label = paper[3]
                    label = label.replace('[','')
                    label = label.replace(']','')
                    label = label.replace(' ','')
                    labels_writer.writerow([label])
                    abstracts_writer.writerow([abstract])

