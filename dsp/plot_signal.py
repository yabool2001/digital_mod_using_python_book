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