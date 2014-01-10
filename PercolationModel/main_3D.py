import numpy.random as nr
import matplotlib.pyplot as plt
from math import sqrt,pi
import math
from matplotlib.patches import Circle


#----------------------------------------------------------------------
def check_lap(x1,y1,z1,x2,y2,z2,rad):
    """
    return if the two spheres is overlap by calculate coordinate distance
    true for lap
    false for non lap
    """
    dis = sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    return dis <= 2*rad
    

#----------------------------------------------------------------------
def whichcluster(cluster_list, spheres_index):
    """
     find which cluster a spheres belongs to. 
     function  take two arguments, the list of clusters 
     and the id of the spheres (its index in the NumPy array). 
     The function should return the index of the cluster 
     that contains the spheres.
    """
    for index,cluster in enumerate(cluster_list):
        if spheres_index in cluster['spheres']:
            return index
    
#----------------------------------------------------------------------
def is_touch_left(x1,rad):
    """
    check if spheres is touch left side    
    """
    return x1-rad <= 0
    
#----------------------------------------------------------------------
def is_touch_right(x1,rad):
    """
    check if spheres is touch right side    
    """
    return x1+rad >= 1
    

#----------------------------------------------------------------------
def joincluster(c1,c2):
    """
     function joincluster() that takes two clusters c1 and c2 as arguments. 
     The function should amalgamate c2 into c1. Create some examples of 
     clusters to test your function. if either of the clusters 
     represented by c1 or c2 touches a boundary, then the resulting 
     amalgamated cluster should too.
    """
    new_cluster = {}
    new_cluster['spheres'] = c1['spheres'] + c2['spheres']
    new_cluster['left'] = c1['left'] or c2['left']
    new_cluster['right'] = c1['right'] or c2['right']
    return new_cluster


#----------------------------------------------------------------------
def clust_spheres_touch(cluster,spheres_x,rad):
    """
    check if cluster touch state will change when add a new spheres  
    and  check if a cluster is touch both side  retrun True
    """
    cluster['left'] = cluster['left'] or is_touch_left(spheres_x,rad)
    cluster['right'] = cluster['right'] or is_touch_right(spheres_x,rad)
    return cluster['left'] and cluster['right']

#----------------------------------------------------------------------
def findclusters(r,rad):
    """
     function findclusters() that 
     takes as arguments your array of spheres coordinates 
     and a radius and returns a list containing the clusters.
    """
    
    #a empty cluster list
    cluster_list=[]

    #add spheres
    for i in range(len(r)):
        spheres_x=r[i][0]
        spheres_y=r[i][1]
        spheres_z=r[i][2]
        lapped_clust = set()
        
        #check all spheres which already in clusters, range(i)=[0,1,..,i-1]
        for j in range(i):
            #check if lapped and find which cluster lapped
            if check_lap(r[i][0],r[i][1],r[i][2],r[j][0],r[j][1],r[j][2],rad):
                lapped_clust.add(whichcluster(cluster_list,j))
        
        #finish all above spheres before i th spheres and check lapped num
        #If the new spheres does not overlap with any existing cluster, 
        #you will need to create a new cluster for it.
        lapped_num = len(lapped_clust)
        if lapped_num == 0:
            new_cluster={'spheres':[i],'left':False,'right':False}
            if clust_spheres_touch(new_cluster,spheres_x,rad):
                return new_cluster,i
            cluster_list.append(new_cluster)
            
            
        #If it overlaps spheres from only one cluster, then add the spheres to that cluster
        elif lapped_num == 1:
            k=lapped_clust.pop()
            cluster_list[k]['spheres'].append(i)
            if clust_spheres_touch(cluster_list[k],spheres_x,rad):
                return cluster_list[k],i
            
        #If the spheres overlaps spheres from more than one cluster, 
        #then the new spheres has connected the two clusters, 
        #so you will need to amalgamate those clusters and add the new spheres.   
        elif lapped_num >= 2:
            joined_c = {'spheres':[],'left':False,'right':False}
            for k in lapped_clust:
                joined_c = joincluster(joined_c,cluster_list[k])
            lp_s=list(lapped_clust)
            lp_s.sort(reverse=True)
            for k in lp_s:    
                cluster_list.pop(k)
            joined_c['spheres'].append(i)
            if clust_spheres_touch(joined_c,spheres_x,rad):
                return joined_c,i
            cluster_list.append(joined_c)
            
    return cluster_list,len(r)



#----------------------------------------------------------------------
def run(n,rad):
    """
    run one simulation with two argumnets n and radius
    """
    

    r = nr.uniform(size=(n,3))
    
    clusters,dn = findclusters(r,rad)
    
    return dn
    
    
    #for i in range(n):
        #x1=r[i][0]
        #y1=r[i][1]
        #circle = Circle((x1, y1), rad , facecolor=(0,0,1),
            #edgecolor=(0,0,0), linewidth=1, alpha=0.4)
        ##print("%.6f  %.6f " % (x1,y1))
        #ax.add_patch(circle)
        ##plt.text(x1,y1,i)        
    
    ##get a connected cluster
    #if type(clusters) == dict:
        #for i in clusters['spheres']:
            #x1=r[i][0]
            #y1=r[i][1]
            #circle = Circle((x1, y1), rad , facecolor=(1,0,0),
                #edgecolor=(0,0,0), linewidth=1, alpha=0.4)
            #ax.add_patch(circle)   
    
    #   for cluster in clusters:
    #       print("spheres: %20s left: %6s right: %6s" % (cluster['spheres'],cluster['left'],cluster['right']))    

if __name__ == '__main__':
    
    #simulation run times
    rt=5
    
    #max random spheres num
    max_random=2000


    
    eta_list=[]
    crit_vol_list=[]
    rad_variation=[i/1000 for i in range(50,150,5)]
    for rad in rad_variation:
        dn=[]
        #print("simulating... rad= %.3f" % rad)
        for i in range(rt):  
            dn.append(run(max_random,rad))
        aver_n=sum(dn)/rt
        
        #calculate the total volume
        eta=aver_n*(4/3.0)*pi*rad**3
        
        #calculate critical volume fraction        
        crit_vol = 1 - math.e ** (-eta)
        
        print("rad=%.3f,n=%d,eat=%.3f,crit_vol=%.3f" %(rad,aver_n,eta,crit_vol))
        
        eta_list.append(eta)
        crit_vol_list.append(crit_vol)
    
    estimate_val = sum(crit_vol_list)/len(crit_vol_list)   
    print("The estimate of percolation threshold is %.6f" %  estimate_val)    
    
    estimate_line=[]    
    for i in range(len(rad_variation)):
        estimate_line.append(estimate_val)
    
    fig = plt.figure(figsize=(10,6))
    ax = plt.subplot(111)    
    plt.plot(rad_variation,crit_vol_list)
    plt.plot(rad_variation,estimate_line)
    plt.xlabel('radius')
    plt.ylim([0,0.6])
    plt.ylabel('Percolation threshold')
    plt.title('Simulation of Percolation Threshold with radius variable')
    plt.show()    

    