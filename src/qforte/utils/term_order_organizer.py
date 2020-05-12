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

def lexical_term_order(op, n_qubits, rule='XYZI'):
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

def interleaved_term_order(op_sq):
    """ Return a sorted list of second-quantized operator in the optimized fermionic ordering
    Parameters
    ----------
    op_sq: list 
        [ [(so_idx1, so_idx2,...), coeff], ...], 
        required to be normal ordered (indices of creation operators come first)
    """
    
    
