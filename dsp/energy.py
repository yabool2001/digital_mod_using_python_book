def power_spectrum ( x_n , N , verbose = False ) :
    """
    Parameters:
    sin         sinus or cosinus
    Returns:
    ( n , x_n ) time base (n) and the signal x(n) as tuple
    """
    
    from numpy.linalg import norm

    
    P = ( norm ( x_n ) ** 2 ) / N
    if ( verbose ) : print('Power of the Signal from Time domain {:0.4f}'.format(P))

    return P # return time base and signal as tuple