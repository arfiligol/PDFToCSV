import csv

with open("output1.csv", "a+", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # writer.writerow(["question_id", "question_content", "A", "B", "C", "D", "true_answer", "detail_explain", "export_comment"])

    finish = "false"
    while (finish != "true"):
        question_id = input("question_id: ")
        question_content = input("question_content: ")
        A = input("A: ")
        B = input("B: ")
        C = input("C: ")
        D = input("D: ")
        E = input("E: ")
        F = input("F: ")
        G = input("G: ")
        H = input("H: ")
        I = input("I: ")
        J = input("J: ")
        true_answer = input("true_answer: ")
        detail_explain = input("detail_explain: ")
        expert_comment = input("expert_comment: ")
        finish = input("finish?: ")
        writer.writerow([question_id, question_content, A, B, C, D, E, F, G, H, I, J, true_answer, detail_explain, expert_comment])
