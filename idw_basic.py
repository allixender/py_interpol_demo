# -*- coding: utf-8 -*-

import numpy as np


#DISTANCE FUNCTION
def distance(x1,y1,x2,y2):
    d=np.sqrt((x1-x2)**2+(y1-y2)**2)
    return d


# fixed radius and power
def run_rblock(x, y, z, xz, yz, r, p):
    x_block=[]
    y_block=[]
    z_block=[]
    xr_min=xz-r
    xr_max=xz+r
    yr_min=yz-r
    yr_max=yz+r
    for i in range(len(x)):
        # condition to test if a point is within the block
        if ((x[i]>=xr_min and x[i]<=xr_max) and (y[i]>=yr_min and y[i]<=yr_max)):
            x_block.append(x[i])
            y_block.append(y[i])
            z_block.append(z[i])
            
    #calculate weight based on distance and p value
    w_list=[]
    for j in range(len(x_block)):
        d=distance(xz,yz,x_block[j],y_block[j]) #distance function is created outside this function
        if d>0:
            w=1/(d**p)
            w_list.append(w)
            z0=0
        else:
            w_list.append(0) #if meet this condition, it means d<=0, weight is set to 0
    
    #check if there is 0 in weight list
    w_check=0 in w_list
    if w_check==True:
        idx=w_list.index(0) # find index for weight=0
        z_idw=z_block[idx] # set the value to the current sample value
    else:
        wt=np.transpose(w_list)
        z_idw=np.dot(z_block,wt)/sum(w_list) # idw calculation using dot product
    return z_idw


def idw_rblock(x, y, z, grid_side_length, search_radius, p):
    # n=100
    n = grid_side_length
    # setup frame of reference
    
    # left,right,lower,upper coordinate boundaries
    x_min=min(x)
    x_max=max(x)
    y_min=min(y)
    y_max=max(y)
    
    #width
    w=x_max-x_min
    #length
    h=y_max-y_min
    #x interval
    wn=w/n
    #y interval
    hn=h/n
    
    # target data lists to store interpolated points and values
    x_idw_list=[]
    y_idw_list=[]
    z_head=[]
    
    # initialisation
    y_init=y_min
    x_init=x_min
    
    for i in range(n):
        xz=x_init+wn*i
        yz=y_init+hn*i
        y_idw_list.append(yz)
        x_idw_list.append(xz)
        z_idw_list=[]
        for j in range(n):
            xz=x_init+wn*j
            # search_radius=100, inv. power value p=1.5
            z_idw=run_rblock(x, y, z, xz, yz, search_radius, p)
            z_idw_list.append(z_idw)
        z_head.append(z_idw_list)
    
    return (x_idw_list, y_idw_list, z_head)


def run_npoint(x, y, z, xz, yz, n_point, p, rblock_iter_distance=10):
    # block radius iteration distance
    # r=10
    r = rblock_iter_distance
    nf=0
    while nf<=n_point: #will stop when np reaching at least n_point
        x_block=[]
        y_block=[]
        z_block=[]
        r +=10 # add 10 unit each iteration
        xr_min=xz-r
        xr_max=xz+r
        yr_min=yz-r
        yr_max=yz+r
        for i in range(len(x)):
            # condition to test if a point is within the block
            if ((x[i]>=xr_min and x[i]<=xr_max) and (y[i]>=yr_min and y[i]<=yr_max)):
                x_block.append(x[i])
                y_block.append(y[i])
                z_block.append(z[i])
        nf=len(x_block) #calculate number of point in the block
    
    #calculate weight based on distance and p value
    w_list=[]
    for j in range(len(x_block)):
        d=distance(xz,yz,x_block[j],y_block[j])
        if d>0:
            w=1/(d**p)
            w_list.append(w)
            z0=0
        else:
            w_list.append(0) #if meet this condition, it means d<=0, weight is set to 0
    
    #check if there is 0 in weight list
    w_check=0 in w_list
    if w_check==True:
        idx=w_list.index(0) # find index for weight=0
        z_idw=z_block[idx] # set the value to the current sample value
    else:
        wt=np.transpose(w_list)
        z_idw=np.dot(z_block,wt)/sum(w_list) # idw calculation using dot product
    return z_idw


# min. number of search points=5, inv. power value p=1.5
def idw_npoint(x, y, z, grid_side_length, n_points, p, rblock_iter_distance=10):
    # n=100
    n = grid_side_length
    # setup frame of reference
    
    # left,right,lower,upper coordinate boundaries
    x_min=min(x)
    x_max=max(x)
    y_min=min(y)
    y_max=max(y)
    
    #width
    w=x_max-x_min
    #length
    h=y_max-y_min
    #x interval
    wn=w/n
    #y interval
    hn=h/n
    
    # target data lists to store interpolated points and values
    x_idw_list=[]
    y_idw_list=[]
    z_head=[]
    
    # initialisation
    y_init=y_min
    x_init=x_min
    
    for i in range(n):
        xz=x_init+wn*i
        yz=y_init+hn*i
        y_idw_list.append(yz)
        x_idw_list.append(xz)
        z_idw_list=[]
        for j in range(n):
            xz=x_init+wn*j
            # min. number of search points=5, inv. power value p=1.5
            z_idw=run_npoint(x, y, z, xz, yz, n_points, p)
            z_idw_list.append(z_idw)
        z_head.append(z_idw_list)
    
    return (x_idw_list, y_idw_list, z_head)
