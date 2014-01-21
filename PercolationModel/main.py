import numpy.random as nr
import matplotlib.pyplot as plt
from math import sqrt,pi,e
from matplotlib.patches import Circle


#----------------------------------------------------------------------
def check_lap(x1,y1,x2,y2,rad):
    """
    return if the two disk is overlap by calculate coordinate distance
    true for lap
    false for non lap
    """
    dis = sqrt((x1-x2)**2+(y1-y2)**2)
    return dis <= 2*rad


#----------------------------------------------------------------------
def whichcluster(cluster_list, disk_index):
    """
     find which cluster a disk belongs to. 
     function  take two arguments, the list of clusters 
     and the id of the disk (its index in the NumPy array). 
     The function should return the index of the cluster 
     that contains the disk.
    """
    for index,cluster in enumerate(cluster_list):
        if disk_index in cluster['disks']:
            return index

#----------------------------------------------------------------------
def is_touch_left(x1,rad):
    """
    check if disk is touch left side    
    """
    return x1-rad <= 0

#----------------------------------------------------------------------
def is_touch_right(x1,rad):
    """
    check if disk is touch right side    
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
    new_cluster['disks'] = c1['disks'] + c2['disks']
    new_cluster['left'] = c1['left'] or c2['left']
    new_cluster['right'] = c1['right'] or c2['right']
    return new_cluster


#----------------------------------------------------------------------
def clust_disk_touch(cluster,disk_x,rad):
    """
    check if cluster touch state will change when add a new disk  
    and  check if a cluster is touch both side  retrun True
    """
    cluster['left'] = cluster['left'] or is_touch_left(disk_x,rad)
    cluster['right'] = cluster['right'] or is_touch_right(disk_x,rad)
    return cluster['left'] and cluster['right']

#----------------------------------------------------------------------
def findclusters(r,rad):
    """
     function findclusters() that 
     takes as arguments your array of disk coordinates 
     and a radius and returns a list containing the clusters.
    """

    #a empty cluster list
    cluster_list=[]

    #add disks
    for i in range(len(r)):
        disk_x=r[i][0]
        disk_y=r[i][1]
        lapped_clust = set()

        #check all disks which already in clusters, range(i)=[0,1,..,i-1]
        for j in range(i):
            #check if lapped and find which cluster lapped
            if check_lap(r[i][0],r[i][1],r[j][0],r[j][1],rad):
                lapped_clust.add(whichcluster(cluster_list,j))

        #finish all above disk before i th disk and check lapped num
        #If the new disk does not overlap with any existing cluster, 
        #you will need to create a new cluster for it.
        lapped_num = len(lapped_clust)
        if lapped_num == 0:
            new_cluster={'disks':[i],'left':False,'right':False}
            if clust_disk_touch(new_cluster,disk_x,rad):
                return new_cluster,i
            cluster_list.append(new_cluster)


        #If it overlaps disks from only one cluster, then add the disk to that cluster
        elif lapped_num == 1:
            k=lapped_clust.pop()
            cluster_list[k]['disks'].append(i)
            if clust_disk_touch(cluster_list[k],disk_x,rad):
                return cluster_list[k],i

        #If the disk overlaps disks from more than one cluster, 
        #then the new disk has connected the two clusters, 
        #so you will need to amalgamate those clusters and add the new disk.   
        elif lapped_num >= 2:
            joined_c = {'disks':[],'left':False,'right':False}
            for k in lapped_clust:
                joined_c = joincluster(joined_c,cluster_list[k])
            lp_s=list(lapped_clust)
            lp_s.sort(reverse=True)
            for k in lp_s:    
                cluster_list.pop(k)
            joined_c['disks'].append(i)
            if clust_disk_touch(joined_c,disk_x,rad):
                return joined_c,i
            cluster_list.append(joined_c)

    return cluster_list,len(r)

#----------------------------------------------------------------------
def example():
    """
     run four simulation and show in graph 
     """    
    fig = plt.figure(figsize=(12,8))
    rad=0.05
    n=[20,50,100,150]
    
    for i in range(len(n)):
        ax = plt.subplot(221+i)
        run_show(ax,n[i],rad)

    
    plt.show()     

#----------------------------------------------------------------------
def run_show(ax,n,rad):
    """
    run one simulation with two argumnets n and radius
    """
    r = nr.uniform(size=(n,2))

    clusters,dn = findclusters(r,rad)

    for i in range(n):
       x1=r[i][0]
       y1=r[i][1]
       circle = Circle((x1, y1), rad , facecolor=(0,0,1),
           edgecolor=(0,0,0), linewidth=1, alpha=0.4)
       #print("%.6f  %.6f " % (x1,y1))
       ax.add_patch(circle)
       plt.xlabel('Simulation of cluster with N = %d' % n)
       #plt.text(x1,y1,i)        

   #get a connected cluster
    if type(clusters) == dict:
       for i in clusters['disks']:
           x1=r[i][0]
           y1=r[i][1]
           circle = Circle((x1, y1), rad , facecolor=(1,0,0),
               edgecolor=(0,0,0), linewidth=1, alpha=0.4)
           ax.add_patch(circle)   
   
   #for cluster in clusters:
        #print("disks: %20s left: %6s right: %6s" % (cluster['disks'],cluster['left'],cluster['right']))    
    
    return dn


#----------------------------------------------------------------------
def run(n,rad):
    """
    run one simulation with two argumnets n and radius
    """
    r = nr.uniform(size=(n,2))

    clusters,dn = findclusters(r,rad)

    return dn


def test():
    #simulation run times
    rt=5

    #max random disk num
    max_random=2000

    eta_list=[]
    area_frac_list=[]
    rad_variation=[i/1000 for i in range(30,100,3)]
    for rad in rad_variation:
        dn=[]
        print("simulating... rad= %.3f" % rad)
        for i in range(rt):  
            dn.append(run(max_random,rad))
        aver_n=sum(dn)/rt

        #calculate the  critical total area for disks
        eta=aver_n*pi*rad**2

        #calculate the critical area fraction
        area_frac = 1 - e**(-eta)

        eta_list.append(eta)
        area_frac_list.append(area_frac)
        print("rad=%.3f,aver_n=%d,eat=%.3f,area fraction=%.3f" %(rad,aver_n,eta,area_frac))

    estimate_val = sum(area_frac_list)/len(area_frac_list)   
    print("The estimate of percolation threshold is %.6f" %  estimate_val)    

    estimate_line=[]    
    for i in range(len(rad_variation)):
        estimate_line.append(estimate_val)

    fig = plt.figure(figsize=(10,6))
    ax = plt.subplot(111)    
    plt.plot(rad_variation,area_frac_list)
    plt.plot(rad_variation,estimate_line)
    plt.xlabel('radius')
    plt.ylabel('Percolation threshold')
    plt.ylim([0.2,1])
    plt.title('Simulation of Percolation Threshold with radius variable')
    plt.show()        

if __name__ == '__main__':
    test()
    #example()

    

