import unittest
from qforte import qforte # remove?
from qforte.ucc.adaptvqe import ADAPTVQE
from qforte.system.molecular_info import Molecule

class ADAPTVQETests(unittest.TestCase):
    def test_H4_adapt_vqe_exact(self):
        print('\n')

        # The FCI energy for H4 at 0.75 Angstrom in a sto-6g basis
        E_fci = -2.1628978832666865

        # The Nuclear repulsion energy
        NRE = 3.0574683298

        # The H4 hamilitonian from pyscf
        circ_vec = [
        qforte.QuantumCircuit(),
        qforte.build_circuit('Z_0'),
        qforte.build_circuit('Z_1'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Z_3 Y_4'),
        qforte.build_circuit('X_0 Z_1 Z_2 Z_3 X_4'),
        qforte.build_circuit('Y_1 Z_2 Z_3 Z_4 Y_5'),
        qforte.build_circuit('X_1 Z_2 Z_3 Z_4 X_5'),
        qforte.build_circuit('Z_2'),
        qforte.build_circuit('Z_3'),
        qforte.build_circuit('Y_2 Z_3 Z_4 Z_5 Y_6'),
        qforte.build_circuit('X_2 Z_3 Z_4 Z_5 X_6'),
        qforte.build_circuit('Y_3 Z_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('X_3 Z_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('Z_4'),
        qforte.build_circuit('Z_5'),
        qforte.build_circuit('Z_6'),
        qforte.build_circuit('Z_7'),
        qforte.build_circuit('Z_0 Z_1'),
        qforte.build_circuit('Z_0 Y_1 Z_2 Z_3 Z_4 Y_5'),
        qforte.build_circuit('Z_0 X_1 Z_2 Z_3 Z_4 X_5'),
        qforte.build_circuit('Y_0 Z_2 Z_3 Y_4'),
        qforte.build_circuit('X_0 Z_2 Z_3 X_4'),
        qforte.build_circuit('Y_0 X_1 X_2 Y_3'),
        qforte.build_circuit('Y_0 Y_1 X_2 X_3'),
        qforte.build_circuit('X_0 X_1 Y_2 Y_3'),
        qforte.build_circuit('X_0 Y_1 Y_2 X_3'),
        qforte.build_circuit('Y_0 X_1 X_2 Z_3 Z_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('Y_0 Y_1 X_2 Z_3 Z_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('X_0 X_1 Y_2 Z_3 Z_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('X_0 Y_1 Y_2 Z_3 Z_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('Y_0 X_1 X_3 Z_4 Z_5 Y_6'),
        qforte.build_circuit('X_0 X_1 X_3 Z_4 Z_5 X_6'),
        qforte.build_circuit('Y_0 Y_1 Y_3 Z_4 Z_5 Y_6'),
        qforte.build_circuit('X_0 Y_1 Y_3 Z_4 Z_5 X_6'),
        qforte.build_circuit('Y_0 X_1 X_4 Y_5'),
        qforte.build_circuit('Y_0 Y_1 X_4 X_5'),
        qforte.build_circuit('X_0 X_1 Y_4 Y_5'),
        qforte.build_circuit('X_0 Y_1 Y_4 X_5'),
        qforte.build_circuit('Y_0 X_1 X_6 Y_7'),
        qforte.build_circuit('Y_0 Y_1 X_6 X_7'),
        qforte.build_circuit('X_0 X_1 Y_6 Y_7'),
        qforte.build_circuit('X_0 Y_1 Y_6 X_7'),
        qforte.build_circuit('Z_0 Z_2'),
        qforte.build_circuit('Z_0 Z_3'),
        qforte.build_circuit('Z_1 Z_2'),
        qforte.build_circuit('Z_1 Z_3'),
        qforte.build_circuit('Z_0 Y_2 Z_3 Z_4 Z_5 Y_6'),
        qforte.build_circuit('Z_0 X_2 Z_3 Z_4 Z_5 X_6'),
        qforte.build_circuit('Z_0 Y_3 Z_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('Z_0 X_3 Z_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('Z_1 Y_2 Z_3 Z_4 Z_5 Y_6'),
        qforte.build_circuit('Z_1 X_2 Z_3 Z_4 Z_5 X_6'),
        qforte.build_circuit('Z_1 Y_3 Z_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('Z_1 X_3 Z_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('Y_0 Z_1 Z_3 Y_4'),
        qforte.build_circuit('X_0 Z_1 Z_3 X_4'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Y_3 Z_4 Y_5'),
        qforte.build_circuit('Y_0 Z_1 Y_2 X_3 Z_4 X_5'),
        qforte.build_circuit('X_0 Z_1 X_2 Y_3 Z_4 Y_5'),
        qforte.build_circuit('X_0 Z_1 X_2 X_3 Z_4 X_5'),
        qforte.build_circuit('Y_1 X_2 X_3 Y_4'),
        qforte.build_circuit('Y_1 Y_2 X_3 X_4'),
        qforte.build_circuit('X_1 X_2 Y_3 Y_4'),
        qforte.build_circuit('X_1 Y_2 Y_3 X_4'),
        qforte.build_circuit('Y_1 Z_2 Z_4 Y_5'),
        qforte.build_circuit('X_1 Z_2 Z_4 X_5'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Y_4'),
        qforte.build_circuit('X_0 Z_1 Z_2 X_4'),
        qforte.build_circuit('Y_1 Z_3 Z_4 Y_5'),
        qforte.build_circuit('X_1 Z_3 Z_4 X_5'),
        qforte.build_circuit('Y_0 Z_1 X_2 X_4 Z_5 Y_6'),
        qforte.build_circuit('Y_0 Z_1 Y_2 X_4 Z_5 X_6'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Y_4 Z_5 Y_6'),
        qforte.build_circuit('X_0 Z_1 X_2 X_4 Z_5 X_6'),
        qforte.build_circuit('X_0 Z_1 X_2 Y_4 Z_5 Y_6'),
        qforte.build_circuit('X_0 Z_1 Y_2 Y_4 Z_5 X_6'),
        qforte.build_circuit('Y_0 Z_1 Z_2 X_3 X_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Y_3 X_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('X_0 Z_1 Z_2 X_3 Y_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('X_0 Z_1 Z_2 Y_3 Y_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('Y_1 X_2 X_5 Y_6'),
        qforte.build_circuit('Y_1 Y_2 X_5 X_6'),
        qforte.build_circuit('X_1 X_2 Y_5 Y_6'),
        qforte.build_circuit('X_1 Y_2 Y_5 X_6'),
        qforte.build_circuit('Y_1 Z_2 X_3 X_5 Z_6 Y_7'),
        qforte.build_circuit('Y_1 Z_2 Y_3 X_5 Z_6 X_7'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Y_5 Z_6 Y_7'),
        qforte.build_circuit('X_1 Z_2 X_3 X_5 Z_6 X_7'),
        qforte.build_circuit('X_1 Z_2 X_3 Y_5 Z_6 Y_7'),
        qforte.build_circuit('X_1 Z_2 Y_3 Y_5 Z_6 X_7'),
        qforte.build_circuit('Y_0 Z_1 Z_2 X_3 X_5 Y_6'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Y_3 Y_5 Y_6'),
        qforte.build_circuit('X_0 Z_1 Z_2 X_3 X_5 X_6'),
        qforte.build_circuit('X_0 Z_1 Z_2 Y_3 Y_5 X_6'),
        qforte.build_circuit('Y_1 X_2 X_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('Y_1 Y_2 Y_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('X_1 X_2 X_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('X_1 Y_2 Y_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('Z_0 Z_4'),
        qforte.build_circuit('Z_0 Z_5'),
        qforte.build_circuit('Z_1 Z_4'),
        qforte.build_circuit('Z_1 Z_5'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Y_5 Z_6 Y_7'),
        qforte.build_circuit('Y_0 Z_1 Y_2 X_5 Z_6 X_7'),
        qforte.build_circuit('X_0 Z_1 X_2 Y_5 Z_6 Y_7'),
        qforte.build_circuit('X_0 Z_1 X_2 X_5 Z_6 X_7'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Y_4 Z_5 Y_6'),
        qforte.build_circuit('Y_1 Z_2 Y_3 X_4 Z_5 X_6'),
        qforte.build_circuit('X_1 Z_2 X_3 Y_4 Z_5 Y_6'),
        qforte.build_circuit('X_1 Z_2 X_3 X_4 Z_5 X_6'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Z_3 Y_4 Z_5'),
        qforte.build_circuit('X_0 Z_1 Z_2 Z_3 X_4 Z_5'),
        qforte.build_circuit('Y_1 Z_2 Z_3 Y_5'),
        qforte.build_circuit('X_1 Z_2 Z_3 X_5'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Z_3 Z_4 X_5 X_6 Y_7'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Z_3 Z_4 Y_5 X_6 X_7'),
        qforte.build_circuit('X_0 Z_1 Z_2 Z_3 Z_4 X_5 Y_6 Y_7'),
        qforte.build_circuit('X_0 Z_1 Z_2 Z_3 Z_4 Y_5 Y_6 X_7'),
        qforte.build_circuit('Y_1 Z_2 Z_3 X_4 X_6 Y_7'),
        qforte.build_circuit('Y_1 Z_2 Z_3 Y_4 Y_6 Y_7'),
        qforte.build_circuit('X_1 Z_2 Z_3 X_4 X_6 X_7'),
        qforte.build_circuit('X_1 Z_2 Z_3 Y_4 Y_6 X_7'),
        qforte.build_circuit('Z_0 Z_6'),
        qforte.build_circuit('Z_0 Z_7'),
        qforte.build_circuit('Z_1 Z_6'),
        qforte.build_circuit('Z_1 Z_7'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Z_3 Y_4 Z_6'),
        qforte.build_circuit('X_0 Z_1 Z_2 Z_3 X_4 Z_6'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Z_3 Y_4 Z_7'),
        qforte.build_circuit('X_0 Z_1 Z_2 Z_3 X_4 Z_7'),
        qforte.build_circuit('Y_1 Z_2 Z_3 Z_4 Y_5 Z_6'),
        qforte.build_circuit('X_1 Z_2 Z_3 Z_4 X_5 Z_6'),
        qforte.build_circuit('Y_1 Z_2 Z_3 Z_4 Y_5 Z_7'),
        qforte.build_circuit('X_1 Z_2 Z_3 Z_4 X_5 Z_7'),
        qforte.build_circuit('Z_2 Z_3'),
        qforte.build_circuit('Z_2 Y_3 Z_4 Z_5 Z_6 Y_7'),
        qforte.build_circuit('Z_2 X_3 Z_4 Z_5 Z_6 X_7'),
        qforte.build_circuit('Y_2 Z_4 Z_5 Y_6'),
        qforte.build_circuit('X_2 Z_4 Z_5 X_6'),
        qforte.build_circuit('Y_2 X_3 X_4 Y_5'),
        qforte.build_circuit('Y_2 Y_3 X_4 X_5'),
        qforte.build_circuit('X_2 X_3 Y_4 Y_5'),
        qforte.build_circuit('X_2 Y_3 Y_4 X_5'),
        qforte.build_circuit('Y_2 X_3 X_6 Y_7'),
        qforte.build_circuit('Y_2 Y_3 X_6 X_7'),
        qforte.build_circuit('X_2 X_3 Y_6 Y_7'),
        qforte.build_circuit('X_2 Y_3 Y_6 X_7'),
        qforte.build_circuit('Z_2 Z_4'),
        qforte.build_circuit('Z_2 Z_5'),
        qforte.build_circuit('Z_3 Z_4'),
        qforte.build_circuit('Z_3 Z_5'),
        qforte.build_circuit('Y_2 Z_3 Z_5 Y_6'),
        qforte.build_circuit('X_2 Z_3 Z_5 X_6'),
        qforte.build_circuit('Y_2 Z_3 Y_4 Y_5 Z_6 Y_7'),
        qforte.build_circuit('Y_2 Z_3 Y_4 X_5 Z_6 X_7'),
        qforte.build_circuit('X_2 Z_3 X_4 Y_5 Z_6 Y_7'),
        qforte.build_circuit('X_2 Z_3 X_4 X_5 Z_6 X_7'),
        qforte.build_circuit('Y_3 X_4 X_5 Y_6'),
        qforte.build_circuit('Y_3 Y_4 X_5 X_6'),
        qforte.build_circuit('X_3 X_4 Y_5 Y_6'),
        qforte.build_circuit('X_3 Y_4 Y_5 X_6'),
        qforte.build_circuit('Y_3 Z_4 Z_6 Y_7'),
        qforte.build_circuit('X_3 Z_4 Z_6 X_7'),
        qforte.build_circuit('Y_2 Z_3 Z_4 Y_6'),
        qforte.build_circuit('X_2 Z_3 Z_4 X_6'),
        qforte.build_circuit('Y_3 Z_5 Z_6 Y_7'),
        qforte.build_circuit('X_3 Z_5 Z_6 X_7'),
        qforte.build_circuit('Z_2 Z_6'),
        qforte.build_circuit('Z_2 Z_7'),
        qforte.build_circuit('Z_3 Z_6'),
        qforte.build_circuit('Z_3 Z_7'),
        qforte.build_circuit('Y_2 Z_3 Z_4 Z_5 Y_6 Z_7'),
        qforte.build_circuit('X_2 Z_3 Z_4 Z_5 X_6 Z_7'),
        qforte.build_circuit('Y_3 Z_4 Z_5 Y_7'),
        qforte.build_circuit('X_3 Z_4 Z_5 X_7'),
        qforte.build_circuit('Z_4 Z_5'),
        qforte.build_circuit('Y_4 X_5 X_6 Y_7'),
        qforte.build_circuit('Y_4 Y_5 X_6 X_7'),
        qforte.build_circuit('X_4 X_5 Y_6 Y_7'),
        qforte.build_circuit('X_4 Y_5 Y_6 X_7'),
        qforte.build_circuit('Z_4 Z_6'),
        qforte.build_circuit('Z_4 Z_7'),
        qforte.build_circuit('Z_5 Z_6'),
        qforte.build_circuit('Z_5 Z_7'),
        qforte.build_circuit('Z_6 Z_7')]

        coef_vec = [
        -2.4821213214548132 ,
        0.23293969973034867 ,
        0.23293969973034867 ,
        0.0021983441988268106 ,
        0.0021983441988268106 ,
        0.0021983441988268106 ,
        0.0021983441988268106 ,
        0.09016180543667125 ,
        0.09016180543667125 ,
        -0.02376280835491324 ,
        -0.02376280835491324 ,
        -0.02376280835491324 ,
        -0.02376280835491324 ,
        -0.1660082742976722 ,
        -0.1660082742976722 ,
        -0.6281380278250508 ,
        -0.6281380278250508 ,
        0.14143194110264784 ,
        0.02343674037513122 ,
        0.02343674037513122 ,
        0.02343674037513122 ,
        0.02343674037513122 ,
        0.03877745930610871 ,
        -0.03877745930610871 ,
        -0.03877745930610871 ,
        0.03877745930610871 ,
        -0.012039864387060981 ,
        0.012039864387060981 ,
        0.012039864387060981 ,
        -0.012039864387060981 ,
        0.012039864387060981 ,
        0.012039864387060981 ,
        0.012039864387060981 ,
        0.012039864387060981 ,
        0.02671075000464898 ,
        -0.02671075000464898 ,
        -0.02671075000464898 ,
        0.02671075000464898 ,
        0.023305310169413392 ,
        -0.023305310169413392 ,
        -0.023305310169413392 ,
        0.023305310169413392 ,
        0.08509071624391439 ,
        0.1238681755500231 ,
        0.1238681755500231 ,
        0.08509071624391439 ,
        0.012213740873669738 ,
        0.012213740873669738 ,
        0.02425360526073072 ,
        0.02425360526073072 ,
        0.02425360526073072 ,
        0.02425360526073072 ,
        0.012213740873669738 ,
        0.012213740873669738 ,
        0.025799434584809343 ,
        0.025799434584809343 ,
        0.02633011407807468 ,
        0.02633011407807468 ,
        0.02633011407807468 ,
        0.02633011407807468 ,
        0.02633011407807468 ,
        -0.02633011407807468 ,
        -0.02633011407807468 ,
        0.02633011407807468 ,
        0.025799434584809343 ,
        0.025799434584809343 ,
        -0.0005306794932653464 ,
        -0.0005306794932653464 ,
        -0.0005306794932653464 ,
        -0.0005306794932653464 ,
        0.01361954106360348 ,
        0.012869714369249078 ,
        0.02648925543285256 ,
        0.02648925543285256 ,
        0.012869714369249078 ,
        0.01361954106360348 ,
        0.023297649975028263 ,
        -0.023297649975028263 ,
        -0.023297649975028263 ,
        0.023297649975028263 ,
        0.023297649975028263 ,
        -0.023297649975028263 ,
        -0.023297649975028263 ,
        0.023297649975028263 ,
        0.01361954106360348 ,
        0.012869714369249078 ,
        0.02648925543285256 ,
        0.02648925543285256 ,
        0.012869714369249078 ,
        0.01361954106360348 ,
        -0.009678108911424788 ,
        -0.009678108911424788 ,
        -0.009678108911424788 ,
        -0.009678108911424788 ,
        -0.009678108911424788 ,
        -0.009678108911424788 ,
        -0.009678108911424788 ,
        -0.009678108911424788 ,
        0.10160802401604081 ,
        0.1283187740206898 ,
        0.1283187740206898 ,
        0.10160802401604081 ,
        0.03616736434427735 ,
        0.03616736434427735 ,
        0.03616736434427735 ,
        0.03616736434427735 ,
        0.03616736434427735 ,
        0.03616736434427735 ,
        0.03616736434427735 ,
        0.03616736434427735 ,
        0.006175224127952704 ,
        0.006175224127952704 ,
        0.006175224127952704 ,
        0.006175224127952704 ,
        -0.011754365096435144 ,
        0.011754365096435144 ,
        0.011754365096435144 ,
        -0.011754365096435144 ,
        0.011754365096435144 ,
        0.011754365096435144 ,
        0.011754365096435144 ,
        0.011754365096435144 ,
        0.1281356271212588 ,
        0.1514409372906722 ,
        0.1514409372906722 ,
        0.1281356271212588 ,
        0.014288787752928002 ,
        0.014288787752928002 ,
        0.02604315284936315 ,
        0.02604315284936315 ,
        0.02604315284936315 ,
        0.02604315284936315 ,
        0.014288787752928002 ,
        0.014288787752928002 ,
        0.12852031505546538 ,
        0.004221577448593006 ,
        0.004221577448593006 ,
        0.004221577448593006 ,
        0.004221577448593006 ,
        0.03476143955777556 ,
        -0.03476143955777556 ,
        -0.03476143955777556 ,
        0.03476143955777556 ,
        0.025289605675922373 ,
        -0.025289605675922373 ,
        -0.025289605675922373 ,
        0.025289605675922373 ,
        0.09209733043445448 ,
        0.12685876999223003 ,
        0.12685876999223003 ,
        0.09209733043445448 ,
        0.030781697768748062 ,
        0.030781697768748062 ,
        0.02586097809210897 ,
        0.02586097809210897 ,
        0.02586097809210897 ,
        0.02586097809210897 ,
        0.02586097809210897 ,
        -0.02586097809210897 ,
        -0.02586097809210897 ,
        0.02586097809210897 ,
        0.030781697768748062 ,
        0.030781697768748062 ,
        0.004920719676639087 ,
        0.004920719676639087 ,
        0.004920719676639087 ,
        0.004920719676639087 ,
        0.10888698089636414 ,
        0.13417658657228654 ,
        0.13417658657228654 ,
        0.10888698089636414 ,
        0.02874930179276457 ,
        0.02874930179276457 ,
        0.02874930179276457 ,
        0.02874930179276457 ,
        0.1336059981515232 ,
        0.03967071839372038 ,
        -0.03967071839372038 ,
        -0.03967071839372038 ,
        0.03967071839372038 ,
        0.10137564054056286 ,
        0.14104635893428324 ,
        0.14104635893428324 ,
        0.10137564054056286 ,
        0.17484481783101552]

        H4_qubit_hamiltonian = qforte.QuantumOperator()
        for i in range(len(circ_vec)):
            H4_qubit_hamiltonian.add_term(coef_vec[i], circ_vec[i])

        ref = [1, 1, 1, 1, 0, 0, 0, 0]

        # make test with algorithm class #
        mol = Molecule()
        mol.set_hamiltonian(H4_qubit_hamiltonian)

        alg = ADAPTVQE(mol, ref, trotter_number=4)
        alg.run(adapt_maxiter=20, avqe_thresh=1.0e-3)
        Egs = alg.get_gs_energy()
        Egs += NRE
        self.assertLess(abs(Egs-E_fci), 1.0e-5)
        ##

        # myAVQE= vqe.ADAPTVQE(ref, H4_qubit_hamiltonian, 5.0e-4, trott_num = 8)
        #
        # myAVQE.fill_pool()
        # myAVQE._pool_obj.print_pool()
        # myAVQE.fill_comutator_pool()
        #
        # avqe_iter = 0
        # hit_maxiter = 0
        # while not myAVQE._converged:
        #
        #     print('\n\n -----> ADAPT-VQE iteration ', avqe_iter, ' <-----\n')
        #     myAVQE.update_ansatz()
        #
        #     if myAVQE._converged:
        #         break
        #
        #     print('\ntoperators included from pool: \n', myAVQE._tops)
        #     print('tamplitudes for tops: \n', myAVQE._tamps)
        #     myAVQE.solve(fast=True, opt_maxiter=100)
        #     print('  Current ADAPT-VQE energy: ', myAVQE._energies[-1]+NRE)
        #     avqe_iter += 1
        #
        #     if avqe_iter > 10:
        #         hit_maxiter = 1
        #         break
        #
        # if hit_maxiter:
        #     final_energy = myAVQE.get_final_energy(hit_max_avqe_iter=1)
        #
        # final_energy = myAVQE.get_final_energy()
        #
        # final_energy += NRE
        #
        # print('Note: added nuclear repulsion!')
        # print('final energy: ', final_energy)
        # print('FCI energy:   ', E_fci)
        #
        # self.assertLess(abs(final_energy-E_fci), 1.0e-5)

if __name__ == '__main__':
    unittest.main()
