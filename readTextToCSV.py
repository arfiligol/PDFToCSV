with open("amazon.web.services.testkings.scs-c01.brain.dumps.2022-nov-28.by.dwight.344q.vce.txt", "r") as f:
    lines = [r for r in f.readlines()]

paragraphs = []
current_paragraph = r""

time = 0
for line in lines:
    if line.strip() == "":
        time += 1
        if time == 3:
            paragraphs.append(current_paragraph.strip())
            current_paragraph = r""
            time = 0
    else:
        time = 0
        current_paragraph += line

if current_paragraph != "":
    paragraphs.append(current_paragraph.strip())


##############################################################
# Write to CSV part
import re
import csv

with open("amazon.web.services.testkings.scs-c01.brain.dumps.2022-nov-28.by.dwight.344q.vce.csv", "a+", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["QuestionID", "QuestionContent", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "Answer", "Explain"])


    # 假設你已經有了問題的文本內容
    for question in paragraphs:
        # 使用正則表達式從文本中提取問題編號、問題和答案
        pattern = r"NEW QUESTION\s+(\d+)\n" + r"(.*(?=A\.))" + r".?\n?\s*(A\..*?(?=B\.|\n))" + r".?\n?(B\..*?(?=C\.|\n))" + r".?\n?(C\..*?(?=D\.|\n))" + r".?\n?(D\..*?(?=E\.|\n))" + r".?\n?(?:(?P<E>E\..*?(?=\n|F\.)))?" + r".?\n?(?:(?P<F>F\..*?(?=G\.|\n)))?" + r".?\n?(?:(?P<G>G\..*?(?=H\.|\n)))?" + r".?\n?(?:(?P<H>H\..*?(?=I\.|\n)))?" + r".?\n?(?:(?P<I>I\..*?(?=J\.|\n)))?" + r".?\n?(?:(?P<J>J\..*?(?=K\.|\n)))?" + r".?\n?(?:(?P<K>K\..*?(?=L\.|\n)))?" + r".?\n?(?:(?P<L>L\..*?(?=M\.|\n)))?" + r".?\n?(?:(?P<M>M\..*?(?=N\.|\n)))?"
        pattern = pattern + r".?\n?Answer:\s+(?P<Answer>[ABCDEFGHIJK]+).?\n?" + r"(?:.?\n?Explanation:\s+(?P<Explain>[\s\S]*))?"
        match = re.search(pattern, question, re.DOTALL)

        if match:
            # 從正則表達式的匹配結果中提取所需信息
            question_number = match.group(1)
            print("Question Number:", question_number)
            question_text = match.group(2)
            A = match.group(3)
            B = match.group(4)
            C = match.group(5)
            D = match.group(6)
            E = match.groupdict()["E"]
            F = match.groupdict()["F"]
            G = match.groupdict()["G"]
            H = match.groupdict()["H"]
            I = match.groupdict()["I"]
            J = match.groupdict()["J"]
            K = match.groupdict()["K"]
            L = match.groupdict()["L"]
            M = match.groupdict()["M"]
            Answer = match.groupdict()["Answer"]
            Explain = match.groupdict()["Explain"]

            writer.writerow([question_number, question_text, A, B, C, D, E, F, G, H, I, J, K, L, M, Answer, Explain])

        else:
            print("No match found.")