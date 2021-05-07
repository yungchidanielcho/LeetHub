class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = {0:"Z", 1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"} 
        def ToExcel(num,string):
            if num > 26:
                quo, rem = divmod(num,26)
                string = d[rem] + string
                if rem == 0 and quo != 1:
                    quo -= 1
                string = ToExcel(quo,string)
            else:
                string = d[num] + string
            return string
        string = ToExcel(columnNumber,"")
        return string