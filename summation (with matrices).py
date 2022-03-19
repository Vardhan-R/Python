import import_matrices as mat

def pwrSum(p):
    m_1 = []
    m_2 = []
    for i in range(p + 2):
        m_1.append([])
        m_2.append([0])
        for j in range(p + 2):
            m_1[i].append(i ** j)
        for j in range(i):
            m_2[i][0] += (j + 1) ** p
    return [x[0] for x in mat.mult(mat.inv(m_1), m_2)]