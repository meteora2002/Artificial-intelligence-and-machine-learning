mport matplotlib.pyplot as plt
%matplotlib inline
def readDraw(f,j=0):
    with open(f) as f:
        i = 0
        steps = []
        globPpx = []
        bucket0 =[]
        bucket1 =[]
        bucket2 =[]
        bucket3 =[]
        bucketMean =[]

        for line in f:
            i = i+1
            l = line.split()
            #print l
            #if i%15 == 0:            
                #break
            if "global" in l:
                steps.append(l[2])
                globPpx.append(l[-1])
                  if "bucket" in l:
                exec('bucket'+l[2]+'.append('+l[-1]+")")
            if "mean" in l:
                bucketMean.append(l[-1])

        if (len(steps) == len(bucket0) & len(bucket3) == len(bucketMean)):
            print "complete"
        
    plt.xlabel("steps")
    plt.ylabel("perplexity")
    plt.plot(steps[j:], globPpx[j:],label='Train Perplexity')
    plt.plot(steps[j:], bucket0[j:],label='Validation: bucket 0')
    plt.plot(steps[j:], bucket1[j:],label='Validation: bucket 1')
    plt.plot(steps[j:], bucket2[j:],label='Validation: bucket 2')
    plt.plot(steps[j:], bucket3[j:],label='Validation: bucket 3')

    plt.legend(loc=1)

    plt.title(str(f))
    plt.show()
