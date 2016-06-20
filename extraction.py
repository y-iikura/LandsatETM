#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Extraction of Landsat Image 
	Original data : Landsat 7 ETM+ : geotif format
		Specified Region from DEM Geotif Image region 	
"""
# cd /Volumes/Transcend/LandsatETM+
# extraction.py ELP108R032_7T20020630 template.txt NEW2 0.0 0.0

import sys
import os
import numpy as np
import cv2
import convert_util as ut
import proj_util as pr

param=sys.argv
if len(param)!=4 and len(param)!=6:
    print 'Usage: extraction.py scene_name area_file(dem.tif) new_folder (dx=0.0 dy=0.0)'
    exit()

fscene=param[1]
fname=param[2]
fnew=param[3]
if len(param)!=6:
  dx=float(param[4])
  dy=float(param[5])
else:
  dx=0.0
  dy=0.0


if os.path.isdir(fnew) == False: os.mkdir(fnew)  

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

xmax=int((pr.xe-pr.xs)/pr.dx)
ymax=int((pr.ye-pr.ys)/pr.dy)
print xmax,ymax

#fold='ELP108R032_7T20020630'
os.chdir(fscene)

list=os.listdir('.')
for name in list:
  if name.find('.met')!=-1:
    fname=name[:-4]

flag=1
sat=ut.original(fname)
if flag:
  print sat.jmax,sat.imax
  print sat.xs,sat.dx
  print sat.ye,sat.dy
  print sat.offset
  print sat.gain

sat.chokka()
if flag:
  print sat.pv
  print sat.qv

for band in [10,20,30,40,50,70]:
  sat.read_band(band)
  conv=ut.convert(sat,xmax,ymax)
  new=conv.convert(dx,dy)
  pr.write_tif('../'+fnew+'/band'+str(band/10)+'.tif',new,1)

ut.gwrite(sat,fnew)
exit()
