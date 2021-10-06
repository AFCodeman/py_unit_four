import math

def gets_a_zero(total_classes, class_missed):
    if (class_missed/total_classes)*100 <= 24:
        return(False)
    else:
        return(True)

gets_a_zero(100,24)