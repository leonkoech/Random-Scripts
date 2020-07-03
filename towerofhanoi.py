  
def TowerOfHanoi(n , source, destination, auxilliary): 
    if n==1: 
        print ("Move disk 1 from ",source,"to ",destination )
        return
    TowerOfHanoi(n-1, source, auxilliary, destination) 
    print ("Move disk ",n,"from ",source,"to ",destination )
    TowerOfHanoi(n-1, auxilliary, destination, source) 

# number of disks 
disk = 5
# left,center and right rod
TowerOfHanoi(disk,'leftRod','centerRod','rightRod')  
