"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    ans=[]
    for i in student_scores:
        ans.append(round(i))
    return ans 


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    c=0
    for i in student_scores:
        if i <= 40 :
            c=c+1
    return c 


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    best=[]
    for i in student_scores:
        if i >= threshold:
            best.append(i)
    return best 

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    g=[41]
    r = highest-40
    duration = round(r/4)
    for i in range(0,3):
        if g[i]+duration <= highest:
            g.append(g[i]+duration)
    return g
        

    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
  
    l=[]
    for i,n in enumerate(student_names):
        l.append(f"{i+1}. {n}: {student_scores[i]}")
    return l
    
    


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """


    for i,n in student_info:
        if n==100:
            return [i,n]
    return []

