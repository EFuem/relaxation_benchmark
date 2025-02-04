from kim_tools import minimize_wrapper



def minimize(atoms, calculator):

    atoms.set_calculator(calculator)
    
    minimize_wrapper(atoms)


if __name__ == "__main__":
    from ase.io import read
    
    # 3 different universal MLIP
    from chgnet.model.dynamics import CHGNetCalculator
    from chgnet.model.model import CHGNet
    
    # This one might need different dependencies
    # from matgl.ext.ase import PESCalculator
   
    from mace.calculators import mace_mp


    # read first 10 structures in this file
    atoms = read('mp_20_train.xyz', index=':10')

    # create calculator from MLIP

    # This model generally works well
    # mace_calculator = mace_mp(model="medium", dispersion=False, default_dtype="float32")
   
    # This model is more challenging
    chgnet = CHGNet.load()
    chgnet_calculator = CHGNetCalculator(chgnet)

    for a in atoms:
        minimize(a, chgnet_calculator)

