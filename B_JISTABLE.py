import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Double Bytes"

#表头
for x in range(4096):
    sheet['A'+str(x+2)]='%03X'%x
for x in range(16):
    sheet[chr(66+x)+'1']='%01X'%x

for code in range(0x0000,0xffff):
    try:
        jisbyte=bytes(divmod(code,0x100))
        jischr=str(jisbyte,encoding='shift-jis')
        if len(jischr) > 1:
            continue
        a,b = divmod(code,0x10)
        sheet[chr(66+b)+str(a+2)] = jischr
    except:
        continue

sheet2 = workbook.create_sheet()
sheet2.title = 'Single Byte'

#表头
for x in range(16):
    sheet2['A'+str(x+2)]='%01X'%x
for x in range(16):
    sheet2[chr(66+x)+'1']='%01X'%x

for code in range(0x00,0xff):
    try:
        jisbyte=bytes([code])
        jischr=str(jisbyte,encoding='shift-jis')
        if len(jischr) > 1:
            continue
        a,b = divmod(code,0x10)
        sheet2[chr(66+b)+str(a+2)] = jischr
    except:
        continue
workbook.save('JISTable.xlsx')