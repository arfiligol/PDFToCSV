import re

# 假設你已經有了問題的文本內容
question = """NEW QUESTION 54
Your company has a set of EC2 Instances defined in AWS. These Ec2 Instances have strict security groups attached to them. You need to ensure that changes to
the Security groups are noted and acted on accordingly. How can you achieve this?
Please select:
A. Use Cloudwatch logs to monitor the activity on the Security Group
B. Use filters to search for the changes and use SNS for the notification.
C. Use Cloudwatch metrics to monitor the activity on the Security Group
D. Use filters to search for the changes and use SNS for the notification.
E. Use AWS inspector to monitor the activity on the Security Group
F. Use filters to search for the changes and use SNS f the notification.
G. Use Cloudwatch events to be triggered for any changes to the Security Group
H. Configure the Lambda function for email notification as well.
Answer: D
Explanation:
The below diagram from an AWS blog shows how security groups can be monitored
C:\Users\wk\Desktop\mudassar\Untitled.jpg
Option A is invalid because you need to use Cloudwatch Events to check for chan, Option B is invalid because you need to use Cloudwatch Events to check for
chang
Option C is invalid because AWS inspector is not used to monitor the activity on Security Groups For more information on monitoring security groups, please visit
the below URL:
Ihttpsy/aws.amazon.com/blogs/security/how-to-automatically-revert-and-receive-notifications-about-changes-to 'pc-security-groups/
The correct answer is: Use Cloudwatch events to be triggered for any changes to the Security Groups. Configure the Lambda function for email notification as well.
Submit your Feedback/Queries to our Experts"""

question = r"" + question

# 使用正則表達式從文本中提取問題編號、問題和答案
pattern = r"NEW QUESTION\s*(\d+)\n" + r"(.*(?=A\.))" + r".?\n?\s*(A\..*?(?=B\.|\n))" + r".?\n?(B\..*?(?=C\.|\n))" + r".?\n?(C\..*?(?=D\.|\n))" + r".?\n?(D\..*?(?=E\.|\n))" + r".?\n?(?:(?P<E>E\..*?(?=\n|F\.)))?" + r".?\n?(?:(?P<F>F\..*?(?=G\.|\n)))?" + r".?\n?(?:(?P<G>G\..*?(?=H\.|\n)))?" + r".?\n?(?:(?P<H>H\..*?(?=I\.|\n)))?" + r".?\n?(?:(?P<I>I\..*?(?=J\.|\n)))?" + r".?\n?(?:(?P<J>J\..*?(?=K\.|\n)))?"
pattern = pattern + r".?\n?Answer:\s+(?P<Answer>[ABCDEFGHIJK]+).?\n?" + r"(?:.?\n?Explanation:\s+(?P<Explain>[\s\S]*))?"
match = re.search(pattern, question, re.DOTALL)

if match:
    # 從正則表達式的匹配結果中提取所需信息
    question_number = match.group(1)
    print("Question Number:", question_number)
    question_text = match.group(2)
    print("question content:", question_text)
    A = match.group(3)
    print("A:", A)
    B = match.group(4)
    print("B:", B)
    C = match.group(5)
    print("C:", C)
    D = match.group(6)
    print("D:", D)
    E = match.groupdict()["E"]
    print("E:", E)
    F = match.groupdict()["F"]
    print("F:", F)
    G = match.groupdict()["G"]
    print("G:", G)
    H = match.groupdict()["H"]
    print("H:", H)
    I = match.groupdict()["I"]
    print("I:", I)
    J = match.groupdict()["J"]
    print("J:", J)
    Answer = match.groupdict()["Answer"]
    print("Answer:", Answer)
    Explain = match.groupdict()["Explain"]
    print("Explain:", Explain)

else:
    print("No match found.")