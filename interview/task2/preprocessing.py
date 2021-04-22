import numpy as np # linear algebra
import xml.etree.ElementTree as ET # for parsing XML
import matplotlib.pyplot as plt # to show images
from PIL import Image # to read images
import os
import glob
import csv

def bounding_box(image_name):

    label_file = 'dataset/annotations.xml'
    tree = ET.parse(label_file)
    root = tree.getroot()
    image_id = image_name.rsplit(".", 1)[0]
    bbox_all = []
    labels = []

    for image in root.findall('image'):

        if image.attrib['id'] == image_id:

            bbox = []
            mask = -1
            helmet = -1

            for allBboxes in image.findall('box'):

              if allBboxes.attrib['label'] == 'head':

                  xmin = int(float(allBboxes.attrib['xtl']))
                  ymin = int(float(allBboxes.attrib['ytl']))
                  xmax = int(float(allBboxes.attrib['xbr']))
                  ymax = int(float(allBboxes.attrib['ybr']))

                  bbox = [xmin, ymin, xmax, ymax]
                  bbox_all.append(bbox)

                  for attributes in allBboxes.findall('attribute'):

                    if attributes.attrib['name'] == 'mask':
                        
                        if attributes.text == 'yes':
                          mask = 1
                        if attributes.text == 'invisible':
                          mask = 0
                        if attributes.text == 'no':
                          mask = 0
                        if attributes.text == 'wrong':
                          mask = 0

                    if attributes.attrib['name'] == 'has_safety_helmet':
                        
                        if attributes.text == 'yes':
                          helmet = 1
                        if attributes.text == 'no':
                          helmet = 0
                    
                  labels.append([helmet, mask])

    return bbox_all, labels


all_images=os.listdir("dataset/images/")
root_images = "dataset/images/"
new_dataset = "dataset/images_new/"

with open('dataset.csv', mode='w') as csv_file:
        fieldnames = ['image', 'helmet', 'mask']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i,image in enumerate(all_images):
            box, labels = bounding_box(image)

            

            j = 0

            for i, bbox in enumerate(box):

                if len(bbox) != 0:
            
                    j = j+1
                    print(bbox)
                    print(labels[i])
                    im=Image.open(os.path.join(root_images,image))
                    im=im.crop(bbox)
                    im = im.save(new_dataset+image.rsplit(".", 1)[0]+"_"+str(j)+".jpg")

                    writer.writerow({'image': new_dataset+image.rsplit(".", 1)[0]+"_"+str(j)+".jpg", 'helmet': labels[i][0], 'mask': labels[i][1]})