"""
Functions to get different term order in Trotterization
"""
import qforte
import numpy as np

# class TermOrdering:
#     def __init__(self, operator, order_type):
#         if isinstance(operator, list):
#             self.op = operator
#         elif isinstance(operator, qforte.QuantumOperator):
#             self.op = operator.terms()
#         self.type = order_type

#     def lexical_order(self):
#         pass

def lexical_term_order_qf(op, n_qubits, rule='XYZI'):
    """ Return a sorted list for the input quantum operator according to the lexical rule

    Parameters
    ----------
    op: list
        a qubit operator in the form
        [[coeff_a, [("X", i),("Z", j),("Y", k)]], [...] ...]
    n_qubits: int
    rule: str, optional
        string to define lexical ordering priority, default 'XYZI' -> X<Y<Z<I

    """
    
    rule_list = list(rule.upper())
    g1 = rule[0]
    g2 = rule[1]
    g3 = rule[2]
    g4 = rule[3]

    I_gate_priority_num = rule_list.index('I') + 1

    cir_list = []
    idx_list = [n for n in range(len(op))]

    for coeff, cir in op:
        cir_str = [str(I_gate_priority_num)]*n_qubits

        for gate_symbol, qubit_idx in cir:
            if gate_symbol == g1:
                cir_str[qubit_idx] = '1'
            elif gate_symbol == g2:
                cir_str[qubit_idx] = '2'
            elif gate_symbol == g3:
                cir_str[qubit_idx] = '3'
            elif gate_symbol == g4:
                cir_str[qubit_idx] = '4'

        cir_num = int(''.join(cir_str))
        cir_list.append(cir_num)
        
    pair = sorted(zip(cir_list, idx_list), key=lambda x: x[0])
    cir_list, idx_list = map(list, zip(*pair))

    sorted_op_list = [op[i] for i in idx_list]
    return sorted_op_list


def lexical_term_order_of(op, n_qubits, rule='XYZI'):
    """ Return a sorted list for the input quantum operator according to the lexical rule

    Parameters
    ----------
    op: list
        a qubit operator in the form
        [ [[(i, "X"),(j, "Z"),(k, "Y")], coeff_a], [...] ...]
    n_qubits: int
    rule: str, optional
        string to define lexical ordering priority, default 'XYZI' -> X<Y<Z<I

    """

    rule_list = list(rule.upper())
    g1 = rule[0]
    g2 = rule[1]
    g3 = rule[2]
    g4 = rule[3]

    I_gate_priority_num = rule_list.index('I') + 1

    cir_list = []
    idx_list = [n for n in range(len(op))]

    for cir, coeff in op:
        if len(cir) == 0:
            scalar = [[cir, coeff]]
        else:
            cir_str = [str(I_gate_priority_num)]*n_qubits

            for qubit_idx, gate_symbol in cir:
                if gate_symbol == g1:
                    cir_str[qubit_idx] = '1'
                elif gate_symbol == g2:
                    cir_str[qubit_idx] = '2'
                elif gate_symbol == g3:
                    cir_str[qubit_idx] = '3'
                elif gate_symbol == g4:
                    cir_str[qubit_idx] = '4'

            cir_num = int(''.join(cir_str))
            cir_list.append(cir_num)

    pair = sorted(zip(cir_list, idx_list), key=lambda x: x[0])
    cir_list, idx_list = map(list, zip(*pair))

    sorted_op_list = [op[i] for i in idx_list]
    sorted_op_list += scalar
    return sorted_op_list
    

def interleaved_term_order(op_sq):
    """ Return a sorted list of second-quantized operator in the optimized fermionic ordering
    Parameters
    ----------
    op_sq: list 
        [ [((idx1, action), (idx2, action)), coeff], ... ]
        required to be normal ordered (indices of creation operators come first)
    """
    length_list = [len(fop) for fop, c in op_sq]
    pp_pq_idx = [length_list.index(i) for i in length_list if i == 2]
    other_idx = [length_list.index(i) for i in length_list if i == 4]
    scalar = [op_sq[length_list.index(i)] for i in length_list if i == 2]
    op_sq_sorted = []

    H_pp = []
    H_pq = []
    H_pqqp = []
    H_prrq = []
    H_pqrs = []
    for i in pp_pq_idx.copy():
        term = op_sq[i]
        ((idx1, _), (idx2, _)) = term[0]
        if idx1 == idx2:
            H_pp.append(term)
            # pp_pq_idx.remove(i)
        else:
            H_pq.append(term)
    for i in other_idx.copy():
        term = op_sq[i]
        ((idx1, _), (idx2, _),
         (idx3, _), (idx4, _)) = term[0]
        if idx1 == idx4 and idx2 == idx3:
            H_pqqp.append(term)
            # other_idx.remove(i)
        elif idx1 != idx4 and idx2 == idx3:
            H_prrq.append(term)
        else:
            H_pqrs.append(term)
            # other_idx.remove(i)
    
    pq_prrq = H_pq.copy()
    for idx, term in enumerate(H_pq):
        ((idx1, _), (idx2, _)) = term
        index = pq_prrq.index(term)
        for term1 in H_prrq:
            p = term[0][0][0]
            q = term[0][3][0]
            if idx1 == p and idx2 == q:
                pq_prrq.insert(index, term1)


    # H_pp = [op_sq[i]
    #         for i in pp_pq_idx if op_sq[i][0][0][0] == op_sq[i][0][1][0]]
    # H_pqqp = [op_sq[i] for i in pp_pq_idx 
    #             if op_sq[i][0][0][0] == op_sq[i][0][3][0] and op_sq[i][0][1][0] == op_sq[i][0][2][0]]
    op_sq_sorted = H_pp + H_pqqp + pq_prrq + H_pqrs + scalar
    return op_sq_sorted
