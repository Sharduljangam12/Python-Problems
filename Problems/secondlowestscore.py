if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    
    scores = [s[1] for s in students]
    
    lowest = min(scores)
    
    remaining = [s for s in students if s[1] != lowest]
    
    remaining_scores = [s[1] for s in remaining]
    second_lowest = min(remaining_scores)
    
    result_names = [s[0] for s in remaining if s[1] == second_lowest]
    
    result_names.sort()
    
    for name in result_names:
        print(name)
