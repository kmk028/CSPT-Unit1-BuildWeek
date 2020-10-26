import numpy as np

def MyDBSCAN(D, eps, min_pts):
    # D is data blob 
    # eps is the epsilon or the radius of circle around the point in question
    # min_pts is number of points inside the circle which is needed for it to be considered Corepoint 
    labels = len(D)*[0] # Create an array of 0 equal to length of data 

    cluster =0  # Cluster ID initialization

    for point in range(0,len(D)): # execute the cluster extension if Cluster ID is not assigned. 
        if not (labels[point]== 0):
            continue

        neighbor_pts = Neighbors(D, point, eps) # Get all the points within the eps radius 

        if len(neighbor_pts) < min_pts: # If < min points required its a noise point. 
            labels[point] = -1
        else:
            cluster = cluster+1  # If > min points assign cluster ID and grow the cluster 
            GrowCluster(D,labels,point,neighbor_pts,cluster,eps,min_pts)

    return labels

def Neighbors(D, point, eps): 
    # Given the eps and data point, function returns all points inside the eps radius as an array 
    neighbors = []

    for neigh_point in range(0,len(D)):
         if np.linalg.norm(D[point]-D[neigh_point]) < eps:
             neighbors.append(neigh_point)
    return neighbors

def GrowCluster(D,labels,point,neighbor_pts,cluster,eps,min_pts):
    # Grow a cluster from seed point 'point' with cluster ID 'Cluster' 
    # D is data (list of vectors)
    # Labels is array to store cluster ID of each point in dataset 
    # cluster : cluster ID
    # min pts: Minimum required number of neighbors
    # eps: Threshold radius 
    # point: seed point from which this cluster grows


    labels[point] = cluster # assign Cluster ID to seed point 

    i =0
    while i < len(neighbor_pts):
        neigh_point = neighbor_pts[i]

        if labels[neigh_point] == -1:
            labels[neigh_point] = cluster
        
        elif labels[neigh_point] == 0:
            labels[neigh_point] = cluster

            neigh_point_neighbors = Neighbors(D,neigh_point,eps)

            if len(neigh_point_neighbors) >= min_pts:
                neighbor_pts += neigh_point_neighbors

        i+=1










    