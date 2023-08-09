# 引入xlrd库
import xlrd

# 读取excel文件
workbook = xlrd.open_workbook("C:\\Users\\75690\\Desktop\\我的文件\\我的自学\\demo.xls")
# 获取第一个sheet表
table = workbook.sheets()[0]
# 便利该表，使用nrows，和ncols代表当前表的有效行列数。
for i in range(table.nrows):
    for j in range(table.ncols):
        # 利用cell_value获得指定行列单元格的值
        print(table.cell_value(i, j))
