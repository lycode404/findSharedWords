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
        gbkbyte=bytes(divmod(code,0x100))
        gbkchr=str(gbkbyte,encoding='GB2312')
        if len(gbkchr) > 1:
            continue
        a,b = divmod(code,0x10)
        sheet[chr(66+b)+str(a+2)] = gbkchr
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
        gbkbyte=bytes([code])
        gbkchr=str(gbkbyte,encoding='GB2312')
        if len(gbkchr) > 1:
            continue
        a,b = divmod(code,0x10)
        sheet2[chr(66+b)+str(a+2)] = gbkchr
    except:
        continue

workbook.save('GB2312Table.xlsx')