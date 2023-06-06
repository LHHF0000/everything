import openpyxl
import shutil
from openpyxl import load_workbook
from openpyxl.styles import PatternFill


def deal(c):
    r = 2
    while r < rows + 1:
        for row_b in worksheet_b.iter_rows(min_row=2, values_only=True):
            table_name_b = row_b[0]
            column_name_b = row_b[1]
            data_type_b = row_b[2]

            table_name_a = sheet1.cell(row=r, column=c - 2).value  # 获取(row,col)单元格的值
            column_name_a = sheet1.cell(row=r, column=c - 1).value
            data_type_a = sheet1.cell(row=r, column=c).value

            # cell(r,c)中的行r和列c 是从1开始 而不是0 例如A11则是ws.cell(1,1),不是ws.cell(0,0)
            if table_name_a != table_name_b or column_name_a != column_name_b:
                continue
            if table_name_a == table_name_b and column_name_a == column_name_b and data_type_a != data_type_b:
                sheet1.cell(row=r, column=c, value=data_type_b).fill = filleN  # 更新的单元格设置为绿色
                break
            if table_name_a == table_name_b and column_name_a == column_name_b and data_type_a == data_type_b:
                sheet1.cell(row=r, column=c, value=data_type_b).fill = filleY  # 无需更新的单元格设置为黄绿色
                break

        r += 1


if __name__ == '__main__':
    excelA_path = r'D:\everything\python1\files\excelA.xlsx'
    excelB_path = r'D:\everything\python1\files\excelB.xlsx'
    excelA_updated_path = r'D:\everything\python1\files\excelA_updated.xlsx'

    # 复制excelA.xlsx为excelA_updated.xlsx
    shutil.copyfile(excelA_path, excelA_updated_path)

    workbook_b = load_workbook(excelB_path)
    worksheet_b = workbook_b.active

    wb = openpyxl.load_workbook(excelA_path)
    sheet1 = wb.worksheets[0]  # 获取第一页sheet

    cols = sheet1.max_column  # 获取有效的数据的最大列数
    rows = sheet1.max_row  # 最大行数

    filleY = PatternFill('solid', fgColor='a5b46a')  # 黄绿
    filleN = PatternFill('solid', fgColor='6ab479')  # 绿
    deal(7)
    deal(11)
    deal(15)

    wb.save(excelA_updated_path)  # 设置保存的路径 和保存的文件名：2.xlsx