import requests
import json
import numpy as np
import pandas as pd
from .SP500PeerList import SP500Peers
from .TSXPeerList import TSXPeers
from .NasdaqPeerList import NasdaqPeers
from .EuroPeerList import EuroPeers

class UniverseData:

    def __init__(self, ticker, universe):
        self.ticker = ticker
        self.sp_universe = SP500Peers().get_available()
        self.nasdaq_universe = NasdaqPeers().get_available()
        self.tsx_universe = TSXPeers().get_available()
        self.euro_universe = EuroPeers().get_available()
        self.universe = universe

    def get_universe(self):
        if self.universe == 'sp500':
            return self.sp_universe
        elif self.universe == 'nasdaq':
            return self.nasdaq_universe
        elif self.universe == 'tsx':
            return self.tsx_universe
        elif self.universe == 'euro':
            return self.euro_universe