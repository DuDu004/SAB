def isInterLeaving(nA, nB, nC):
    print(A[nA:], B[nB:], C[nC:])
    if (nA == len(A)) and (nB == len(B)) and (nC == len(C)):
        return True
    if (len(A) + len(B) != len(C)):
        return False
    
    caseA = False
    caseB = False

    if (nA < len(A) and A[nA] == C[nC]):
        caseA = isInterLeaving(nA + 1, nB, nC + 1)
    if (nB < len(B) and B[nB] == C[nC]):
        caseB = isInterLeaving(nA, nB + 1, nC + 1)

    return (caseA or caseB)

A = "xyz"
B = "abcd"
C = "xabyczd"
print(isInterLeaving(0, 0, 0))