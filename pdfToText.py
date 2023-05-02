import pdftotext

with open("amazon.web.services.testkings.scs-c01.brain.dumps.2022-nov-28.by.dwight.344q.vce.pdf", "rb") as file:
    pdf = pdftotext.PDF(file)

with open("amazon.web.services.testkings.scs-c01.brain.dumps.2022-nov-28.by.dwight.344q.vce.txt", "w") as f:
    # 將轉換後的文字寫入檔案
    f.write("\n\n".join(pdf))