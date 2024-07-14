def plot_signal ( n , x_n ) :
    """
    Plot signal with the following parameters
    Parameters:
    x   x axes tuple
    y   y axes tuple
    """

    import matplotlib.pyplot as plt

    plt.figure ( figsize = ( 10 , 5 ) )
    # plt.plot ( n , x_n , label = 'Signal amplitude' )
    plt.scatter ( n , x_n , color = 'red' , marker = '*' , s = 100 , label = 'Samples (n)' )
    plt.title ( 'Samples of x_n input signal ' )
    plt.xlabel ( 'n' )
    plt.ylabel ( 'x (n)' )
    plt.legend ()
    plt.grid ( True )
    plt.show ()

def plot_dft ( m_freq , X_m_mag , X_m_phi ) :

    import matplotlib.pyplot as plt

    plt.figure ( figsize = ( 10 , 5 ) )
    plt.subplot ( 211 )
    plt.stem ( m_freq , X_m_mag , 'b' ,  markerfmt = " " , basefmt = "-b" )
    plt.ylabel ( 'Magnitude of X(m) |X(freq)|' )

    plt.subplot ( 212 )
    plt.stem ( m_freq , X_m_phi , 'b', markerfmt = " ", basefmt = "-b" )
    plt.xlabel ( 'Freq (Hz)' )
    plt.ylabel ( 'Phase Angle of X(m) Xphi(freq)' )
    plt.show ()