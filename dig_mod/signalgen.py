def sine_wave ( f , overSampRate , phase , nCyl ) :
    """
    Generate sine wave signal with the following parameters
    Parameters:
    f : frequency of sine wave in Hertz
    overSampRate : oversampling rate (integer)
    phase : desired phase shift in radians
    nCyl : number of cycles of sine wave to generate
    Returns:
    (t,g) : time base (t) and the signal g(t) as tuple
    Example:
    f=10; overSampRate=30;
    phase = 1/3*np.pi ; nCyl = 5;
    (t,g) = sine_wave(f,overSampRate,phase,nCyl)
    """
fs = overSampRate * f # sampling frequency
t = np.arange ( 0 , nCyl * 1 / f - 1 / fs , 1 / fs ) # time base
g = np.sin ( 2 * np.pi * f * t + phase ) # replace with cos if a cosine wave is desired

return ( t , g ) # return time base and signal g(t) as tuple