import random
level=0
wrong_a = [0,0,0,0,0,0,0,0,0,0]
def main():
    level = get_level()
    #print (level)
    score = 0
    if level in [1,2,3]:
        for q in range(10):
            qa_list = generate_q(level)
            #print(qa_list)
            while wrong_a[q] < 3:
                ans = input(f"{qa_list[0]} = ")
                try:
                    if int(ans) != qa_list[1]:
                        wrong_a[q] += 1
                        print("EEE")
                    else:
                        score += 1
                        break
                except ValueError:
                    wrong_a[q] += 1
                    print("EEE")
            else:
                print(f"{qa_list[0]} = {qa_list[1]}")
        return(score)


def get_level():
    try:
        while True:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
    except ValueError:
        get_level()

def generate_q(l):
    if l == 1:
        question = "".join(str(random.randint(0,9))+" + "+str(random.randint(0,9)))
        broken = question.split(" + ")
        answer = int(broken[0]) + int(broken[1])
        return [question,answer]
    elif l ==2:
        question = "".join(str(random.randint(10,99))+" + "+str(random.randint(10,99)))
        broken = question.split(" + ")
        answer = int(broken[0]) + int(broken[1])
        return [question,answer]
    else:
        question = "".join(str(random.randint(100,999))+" + "+str(random.randint(100,999)))
        broken = question.split(" + ")
        answer = int(broken[0]) + int(broken[1])
        return [question,answer]

if __name__ == "__main__":
    s=main()
    print(f"Score: {str(s)}")