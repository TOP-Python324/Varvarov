def central_tendency(numb: float, numb1: float, /, *numb_):
    sum_numb = numb, numb1, *numb_
    root_numb = 1/len(sum_numb)
    
    median = sum(sum_numb) / len(sum_numb)
    arithmetic = sum(sum_numb) / 2
    
    for numb2 in numb_:
        prod_ = numb2 * numb * numb1
        geometric = prod_ ** root_numb
        harmonic = (2 * numb * numb1 * numb2) / sum(sum_numb)
    return {'median' : float(median),
            'arithmetic' : float(arithmetic),
            'geometric' : float(geometric),
            'harmonic' : float(harmonic)}

# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 5.0, 'geometric': 1.681792830507429, 'harmonic': 1.6}
# >>>
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 7.5, 'geometric': 1.5848931924611136, 'harmonic': 1.3333333333333333}