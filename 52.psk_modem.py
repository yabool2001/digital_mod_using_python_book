class PSKModem(Modem):
    # Derived class: PSKModem
    def __init__(self, M):
        #Generate reference constellation
        m = np.arange(0,M) #all information symbols m={0,1,...,M-1}
        I = 1/np.sqrt(2)*np.cos(m/M*2*np.pi)
        Q = 1/np.sqrt(2)*np.sin(m/M*2*np.pi)
        constellation = I + 1j*Q #reference constellation
        Modem.__init__(self, M, constellation, name='PSK') #set the modem attributes