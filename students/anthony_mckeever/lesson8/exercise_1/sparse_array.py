"""
Programming In Python - Lesson 8 Exercise 1: Sparse Array
Code Poet: Anthony McKeever
Start Date: 09/04/2019
End Date: 09/04/2019
"""

class SparseArray():

    def __init__(self, input):
        self._len = len(input)
        self.storage = {k: input[k] for k in range(self._len) if input[k] != 0 }


    def __len__(self):
        return self._len
    

    def __getitem__(self, index):
        if isinstance(index, int):
            index = self.validate_index(index)

            item = self.storage.get(index)
            return item if item is not None else 0
        elif isinstance(index, slice):
            get_range = self.get_range(index)
            print(get_range)
            return [self.__getitem__(x) for x in get_range ]
        else:
            raise TypeError(f"SparseArray indicies must be integers or slices, not {type(index).__name__}")

    
    def __setitem__(self, index, value):
        index = self.validate_index(index)
          
        if index in self.storage.keys():
            if value != 0:
                self.storage[index] = value
            else:
                self.storage.pop(index)
        else:
            if value != 0:
                self.storage.update({index: value})

    def append(self, value):
        if value != 0:
            item = {self._len: value}
            self.storage.update(item)
        self._len += 1

    def validate_index(self, index):
        index = index if index >= 0 else self._len + index 
        
        if index >= self._len or index < 0:
            raise IndexError("SparseArray index out of range.")

        return index


    def get_range(self, slice_index):
        step =  slice_index.step
        start = slice_index.start
        stop =  slice_index.stop

        if start is None:
            start = self._len - 1 if step < 0 else 0

        if stop is None:
            stop = 0 if step < 0 else self._len

        return range(start, stop, step)


class Sparse2DArray():

    def __init__(self, input):
        self._len = len(input)
        self.storage = {}

        for i, item in enumerate(input):
            storage = {k: item[k] for k in range(self._len) if item[k] != 0 }
            self.storage.update({i: storage})


    def __len__(self):
        return self._len
    

    def __getitem__(self, index):
        if isinstance(index, int):
            index = self.validate_index(index)

            item = self.storage.get(index)
            return item if item is not None else 0
        elif isinstance(index, slice):
            get_range = self.get_range(index)
            print(get_range)
            return [self.__getitem__(x) for x in get_range ]
        else:
            raise TypeError(f"SparseArray indicies must be integers or slices, not {type(index).__name__}")

    
    def __setitem__(self, index, value):
        index = self.validate_index(index)
          
        if index in self.storage.keys():
            if value != 0:
                self.storage[index] = value
            else:
                self.storage.pop(index)
        else:
            if value != 0:
                self.storage.update({index: value})

    def append(self, value):
        if value != 0:
            item = {self._len: value}
            self.storage.update(item)
        self._len += 1

    def validate_index(self, index):
        index = index if index >= 0 else self._len + index 
        
        if index >= self._len or index < 0:
            raise IndexError("SparseArray index out of range.")

        return index


    def get_range(self, slice_index):
        step =  slice_index.step
        start = slice_index.start
        stop =  slice_index.stop

        if start is None:
            start = self._len - 1 if step < 0 else 0

        if stop is None:
            stop = 0 if step < 0 else self._len

        return range(start, stop, step)
