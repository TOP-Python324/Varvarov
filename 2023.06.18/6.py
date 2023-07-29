def orth_triangle(*, cathetus1 = 1, cathetus2 = 1, hypotenuse = 1):
    triangle_ = cathetus1, cathetus2, hypotenuse
    cath2 = float(hypotenuse ** 2 - cathetus1 ** 2) ** 0.5
    cath1 = float(hypotenuse ** 2 - cathetus2 ** 2) ** 0.5
    hyp = float(cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
    for triangle in triangle_:
        if triangle > 2 and (hypotenuse < cathetus1 or hypotenuse < cathetus2):
            return(None)
        if hypotenuse > cathetus1:
            return cath2
        if hypotenuse > cathetus2:
            return cath1
        else:
            return hyp            