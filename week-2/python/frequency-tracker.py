# class FrequencyTracker:

#     def __init__(self):
#         self.dict = {}
#         self.dict2 = {}

#     def add(self, number: int) -> None:
#         if number in self.dict:
#             self.dict2[self.dict[number]]-=1
#             self.dict[number]+=1
#             if self.dict[number] in self.dict2:
#                 self.dict2[self.dict[number]]+=1
#             else:
#                 self.dict2[self.dict[number]] = 1
#         else:
#             self.dict[number] = 1
#             self.dict2[self.dict[number]] = 1
#         # print(self.dict2)

#     def deleteOne(self, number: int) -> None:
#         if self.dict[number] and self.dict[number] >= 1:
#             self.dict2[self.dict[number]]-=1
#             self.dict[number]-=1
#             if self.dict[number] in self.dict2:
#                 self.dict2[self.dict[number]]+=1
#             else:
#                 self.dict2[self.dict[number]] = 1
            
#         # print(self.dict2)
            

#     def hasFrequency(self, frequency: int) -> bool:
#         print(self.dict2)
#         return frequency in self.dict2 and self.dict2[frequency]>0

        


# # Your FrequencyTracker object will be instantiated and called as such:
# # obj = FrequencyTracker()
# # obj.add(number)
# # obj.deleteOne(number)
# # param_3 = obj.hasFrequency(frequency)
class FrequencyTracker(object):

    def __init__(self):
        self.frequency=defaultdict(int)
        self.f=defaultdict(int)

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.frequency[number]:
            if self.f[self.frequency[number]] > 0:
                self.f[self.frequency[number]]-=1
        self.frequency[number] += 1
        self.f[self.frequency[number]]+=1
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.frequency[number]>0:
            self.f[self.frequency[number]]-=1
            self.frequency[number]-=1
            self.f[self.frequency[number]]+=1

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        
        if self.f[frequency]:
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
