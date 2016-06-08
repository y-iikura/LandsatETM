#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Satellie Image Class for Geometric Correction
	Original data : Landsat 7 ETM+ : geotif format
	New data : converted image with specified region 	
 12/27/2015 executable file
"""
import numpy as np
import cv2
#from osgeo import gdal
#from osgeo import osr
import proj_util as pr


#sun_el = 0.0
#sun_az = 0.0

#xs=0.0
#ye=0.0
#dx=0.0
#dy=0.0

class original:
  def __init__(self,fname):
    gt,wkt,image=pr.read_tif(fname)
    self.image=image
    self.xs=gt[0]
    self.ye=gt[3]
    self.dx=gt[1]
    self.dy=-gt[5]
  def display(self,name,xmax,ymax):
    old=self.image
    min=np.min(old) ; max=np.max(old)
    oldx=np.uint8(255.0*(old-min)/(max-min))
    oldy=cv2.resize(oldx,(xmax,ymax))
    cv2.imshow(name,oldy)

class convert:
  def __init__(self,old,xmax,ymax):
    self.old=old
    self.xs=pr.xs
    self.ye=pr.ye
    self.dx=pr.dx
    self.dy=pr.dy
    self.xmax=xmax
    self.ymax=ymax
  def convert(self,tx,ty):
    x=self.xs+np.arange(self.xmax)*self.dx
    y=self.ye-np.arange(self.ymax)*self.dy
    xso=self.old.xs+tx
    yeo=self.old.ye+ty
    xc=(x-xso)/self.old.dx
    yc=(yeo-y)/self.old.dy
    xx,yy=np.meshgrid(xc,yc)
    xx=np.float32(xx)
    yy=np.float32(yy)
    return cv2.remap(self.old.image,xx,yy,cv2.INTER_LINEAR)
  def hyouka(self,parm):
    new=self.convert(parm[0],parm[1])
    res=np.corrcoef(inc[100:500,100:500].flat,new[100:500,100:500].flat)
    return -res[0,1]


