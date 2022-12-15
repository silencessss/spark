"""
Computing number of objects
"""
import os
import sys

def counting_each_label(label_list):
    label_0=[]
    label_1=[]
    label_2=[]
    for one_data in range(len(label_list)):
        #print(label_list[one_data])
        for one_label in range(len(label_list[one_data])):
            x = label_list[one_data][one_label]
            #print(label_list[one_data][one_label])
            if x == 0:
                label_0.append(x)
            elif x == 1:
                label_1.append(x)
            elif x == 2:
                label_2.append(x)
            else:
                print('other label:',x)
    print(len(label_0))
    print(len(label_1))
    print(len(label_2))

def read_eachlabel(path_txt):
    '''
    Args: 
        input: txt file with yolo mark format
        output: label list in a txt file 
    '''
    labels = []
    with open(path_txt) as f:
        for line in f.readlines():
            print(line)
            s = line.split('  ')
            labels.append(int(s[0]))
    #print(labels)
    return labels


if __name__=='__main__':
    label_list = []# all labels
    path_src = r'C:\Users\PeterChan\Downloads\AIGO_data\data\val_set\labels'
    for root,_,basenames in os.walk(path_src):
        for basename in basenames:
            filepath = os.path.join(root,basename)
            #print(filepath)# check okay
            labels = read_eachlabel(filepath)
            #print(labels)
            label_list.append(labels)
    #print(label_list)
    #print(len(label_list))#391
    counting_each_label(label_list)

