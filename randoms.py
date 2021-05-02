class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):  # Called for index or slice 
        print('getitem:', index, self.data[index])
        return self.data[index]  # Perform index or slice
    
    def __contains__(self, item):
        return item in self.data
print(7 in Indexer())

a=(range(0, 10))
print(a)
b, c = iter(a), list(iter(a))
print(b, a, c)
