import pandas as pd

def get_segments(path):
        df = pd.read_csv(path)
        formula = [a for a in [df.iloc[i,0] for i in range(5)]]
        no_of_tromb = [a for a in [df.iloc[i,1] for i in range(3)]]
        op_one = [a for a in [df.iloc[i,2] for i in range(4)]]
        op_three = [a for a in [df.iloc[i,3] for i in range(4)]]
        op_n = [a for a in [df.iloc[i,3] for i in range(4)]]
        return formula, no_of_tromb, op_one, op_three, op_n

def write_into(n, nt, formula, opo, opt, opn):
        file_name = '{}_QP_tromboloid.docx'.format(n)
        f = open(file_name, 'a')
        string1 = 'Given the formula for the volume of a tromboloid : {}. Where, l = length, b = breadth, h = height and k is the characteristic dimension of the tromboloid.\n'.format(formula)
        string2 = 'Find the following :\n'
        string3 = '{}.) Volume of {}. Also find the {}.\n\n{}.) Volume of {}. Also find the {}.\n\n{}.) Volume of {}. Also find the {}.\n'.format(1, nt[0], opo, 2, nt[1], opt, 3, nt[2], opn)
        string = string1 + string2 + string3
        f.write(string)
        f.close()

if __name__ == '__main__' :
        path = 'tromboloid_questions.csv'
        formula, nt, opo, opt, opn = get_segments(path)
        c = 1
        for i in formula:
                for j in opo :
                        for k in opt :
                                for l in opn:
                                        write_into(c, nt, i, j, k, l)
                                        c += 1
        print("SUCCESS!")
