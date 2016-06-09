#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Extraction of Landsat Image 
	Original data : Landsat 7 ETM+ : geotif format
		Specified Region from DEM Geotif Image region 	
"""
# extraction.py ELP108R032_7T20020630 template.txt

import sys
import os
import numpy as np
import cv2
import convert_util as ut
import proj_util as pr

param=sys.argv
if len(param)!=3:
    print 'Usage: extraction.py scene_name area_file'


fscene=param[1]

fname=param[2]
f=open(fname)
lines=f.readlines()
f.close()

for line in lines:
  if line.find('xs')!=-1: pr.xs=float(line.split()[1])
  if line.find('xe')!=-1: pr.xe=float(line.split()[1])
  if line.find('ys')!=-1: pr.ys=float(line.split()[1])
  if line.find('ye')!=-1: pr.ye=float(line.split()[1])
  if line.find('dx')!=-1: pr.dx=float(line.split()[1])
  if line.find('dy')!=-1: pr.dy=float(line.split()[1])
  print line,

#pr.xs= 406200.0
#pr.xe= 442200.0
#pr.dx= 30.0
#pr.ys= 4460750.0
#pr.ye= 4496750.0
#pr.dy= 30.0

xmax=int((pr.xe-pr.xs)/pr.dx)
ymax=int((pr.ye-pr.ys)/pr.dy)
print xmax,ymax

#fold='ELP108R032_7T20020630'
os.chdir(fscene)

list=os.listdir('.')

for name in list:
  if name.find('.met')!=-1:
    fname=name[:-4]

#fname='p108r032_7t20020630'

for band in [10,20,30,40,50,70]:
  sat=ut.original(fname+'_z54_nn'+str(band)+'.tif')
  sat.image.shape
  #sat.display('sat',600,600)
  #cv2.destroyWindow('sat')
  conv=ut.convert(sat,xmax,ymax)
  new=conv.convert(0.0,0.0)
  #cv2.imshow('new',cv2.resize(new,(600,600)))
  #cv2.destroyWindow('new')
  pr.write_tif('../band'+str(band/10)+'.tif',new,1)

exit()