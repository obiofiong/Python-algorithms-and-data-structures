
def mergeIntervals(arr):
     list_ = []
        
        intervals.sort()        
        
        min_ = intervals[0][0]
        max_ = intervals[0][1]
        list_.append([min_,max_])
        print(list_)
        a = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] <= list_[a][1]:
                list_[a][1] = max(list_[a][1], intervals[i][1])
                print("merged lis ",list_)
            else:
                list_.append(intervals[i])
                print("new inter ",list_)
                a +=1

        return list_



test1 =  [[1,3],[2,6],[8,10],[15,18]]
test2 = [[1,4],[0,4]]

mergeIntervals(test1)