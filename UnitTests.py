import unittest

def partition(array, low, high):

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

class TestSorts(unittest.TestCase):
        
    def test_pos(self):
        
        self.assertEqual(testedData, [-2,1,1,4,7,9,10])
    
    def test_neg(self):
        
        self.assertNotEquals(testedData, [1, -2, 4, 10, 1, 9, 7])

    def test_pef(self):
        
        self.assertEqual(testedData, [-2, 1, 1, 4, 7, 9, 10])
        self.assertEqual(testedSmall, [1,1,2,3])
        self.assertEqual(testedLarge, [1,1,2,2,3,4,4,5,6,7,8])
    
    def test_bounds(self):
        
        self.assertEqual(cleanSorted, [1,2,3,4,5])
        self.assertEqual(cleanEmp, [])
    
    def test_idem(self):
        
        self.assertEqual(newIdem, [1,1,2,3])


if __name__ == "__main__":

    #raw unsorted arrays
    data = [1, 7, 4, 1, 10, 9, -2]
    smallData = [1,2,3,1]
    largeData = [1,2,3,4,4,5,6,7,8,1,2]


    #quicksort is ran and copied into a new array to be tested against cleanDatas
    quickSort(data, 0, 6)
    quickSort(smallData,0,3)
    quickSort(largeData,0,10)
    testedSmall = smallData.copy()
    testedLarge = largeData.copy()
    testedData = data.copy()

    #Already sorted and empty array

    empArr = []
    alreadySorted = [1,2,3,4,5]
    quickSort(alreadySorted,0,4)
    quickSort(empArr,0,0)
    cleanSorted = alreadySorted.copy()
    cleanEmp = empArr.copy()

    #idempotency cases

    idemArr = [1,3,2,1]
    quickSort(idemArr,0,3)
    quickSort(idemArr,0,3)
    quickSort(idemArr,0,3)
    newIdem = idemArr.copy()

   
    unittest.main()
    
