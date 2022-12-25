from .SP500PeerList import SP500Peers
from .TSXPeerList import TSXPeers
from .NasdaqPeerList import NasdaqPeers
from .EuroPeerList import EuroPeers
from stockuploader.models import FundamentalAttributes
from django.conf import settings



class PeerSpecificData:
    def __init__(self,ticker, universe):
        self.sp_universe = SP500Peers().get_available()
        self.nasdaq_universe = NasdaqPeers().get_available()
        self.tsx_universe = TSXPeers().get_available()
        self.euro_universe = EuroPeers().get_available()
        self.universe = universe
        self.ticker = ticker
        self.columns_required_for_analysis = ['netIncomePerShareTTM',  'revenuePerShareTTM', 'operatingCashFlowPerShareTTM', 'peRatioTTM', 'pocfratioTTM', 'pbRatioTTM',  \
                                'pfcfRatioTTM', 'priceToSalesRatioTTM', 'freeCashFlowPerShareTTM', 'bookValuePerShareTTM',  'freeCashFlowYieldTTM','earningsYieldTTM', \
                                'roicTTM', 'roeTTM', 'marketCapTTM', 'debtToAssetsTTM', 'debtToMarketCapTTM', 'debtToEquityTTM',\
                                'dividendYieldPercentageTTM', 'interestCoverageTTM','payoutRatioTTM', 'netDebtToEBITDATTM',\
                                'researchAndDevelopementToRevenueTTM', 'shareholdersEquityPerShareTTM', 'salesGeneralAndAdministrativeToRevenueTTM']
        self.fundamental_attirbute_name_mappings ={
                                                    'netIncomePerShareTTM':'Net Income Per Share',
                                                    'revenuePerShareTTM':'Revenue Per Share',
                                                    'operatingCashFlowPerShareTTM':'Operating Cash Flow Per Share',
                                                    'peRatioTTM':'Price to Earnings Ratio',
                                                    'pocfratioTTM':'Price to Operating Cash Flow',
                                                    'pbRatioTTM':'Price to Book',
                                                    'pfcfRatioTTM':'Price to Cash Flow',
                                                    'priceToSalesRatioTTM':'Price to Sales',
                                                    'freeCashFlowPerShareTTM':'Free Cash Flow Per Share',
                                                    'bookValuePerShareTTM':'Book Value Per Share',
                                                    'freeCashFlowYieldTTM':'Free Cash Flow Yield',
                                                    'earningsYieldTTM':'Earnings Yield',
                                                    'roicTTM':'Return On Invested Capital',
                                                    'roeTTM':'Return On Equity',
                                                    'marketCapTTM':'Market Cap',
                                                    'debtToAssetsTTM':'Debt To Assets',
                                                    'debtToMarketCapTTM':'Debt To Market Cap',
                                                    'debtToEquityTTM':'Debt To Equity',
                                                    'dividendYieldPercentageTTM':'Dividend Yield (%)',
                                                    'interestCoverageTTM':'Interest Coverage',
                                                    'payoutRatioTTM':'Dividend Payout Ratio',
                                                    'netDebtToEBITDATTM':'Net Debt To EBITDA',
                                                    'researchAndDevelopementToRevenueTTM':'Research and Development to Revenue',
                                                    'shareholdersEquityPerShareTTM':'Shareholders Equity Per Share',
                                                    'salesGeneralAndAdministrativeToRevenueTTM':'Sales and Genral Admin to Revenue'
                                                }

    def get_universe(self):
        if self.universe == 'sp500':
            return self.sp_universe
        elif self.universe == 'nasdaq':
            return self.nasdaq_universe
        elif self.universe == 'tsx':
            return self.tsx_universe
        elif self.universe == 'euro':
            return self.euro_universe


    def get_peer_chart_data(self):
        universe = self.get_universe()
        peers = universe[self.ticker]
        if len(peers) == 0:
            return {
                'raw_data':"Unfortunately No Peer Specific Matches Found, we continue to grow our database to ensure your analysis retrieves the best results.",
                'mappings':self.fundamental_attirbute_name_mappings}
        else:
            if self.ticker in peers:
                pass
            else:
                peers.append(self.ticker)
            all_peer_data_retrieved = FundamentalAttributes.objects.filter(symbol__in=peers)
            all_symbols = []
            pe_data = []
            psales_data = []
            pcf_data = []
            pb_data = []
            de_data = []
            roe_data = []
            roic_data = []
            div_data = []
            capex_rev = []
            interest_cov = []
            fcfyld = []
            eyld = []
            fcf = []
            for i in range(0, len(all_peer_data_retrieved)):
                all_symbols.append([all_peer_data_retrieved[i].symbol][0])
                pe_data.append([all_peer_data_retrieved[i].price_to_earnings_ratio][0])
                psales_data.append([all_peer_data_retrieved[i].psales_ratio][0])
                pcf_data.append([all_peer_data_retrieved[i].price_to_cashflow][0])
                pb_data.append([all_peer_data_retrieved[i].price_to_book_ratio][0])
                de_data.append([all_peer_data_retrieved[i].debt_to_equity][0])
                roe_data.append([all_peer_data_retrieved[i].return_on_equity][0]*100)
                roic_data.append([all_peer_data_retrieved[i].return_on_invested_capital][0]*100)
                div_data.append([all_peer_data_retrieved[i].dividend_yield_percent][0])
                capex_rev.append([all_peer_data_retrieved[i].capex_to_revenue][0])
                interest_cov.append([all_peer_data_retrieved[i].interest_coverage][0])
                fcfyld.append([all_peer_data_retrieved[i].free_cash_flow_yield][0]*100)
                eyld.append([all_peer_data_retrieved[i].earnings_yield][0]*100)
                fcf.append([all_peer_data_retrieved[i].free_cash_flow_per_share][0])

            data_to_return = {
                'symbols':all_symbols,
                'pe':pe_data,
                'psales':psales_data,
                'pcf':pcf_data,
                'pb':pb_data,
                'de':de_data,
                'roe':roe_data,
                'roic':roic_data,
                'div':div_data,
                'capex':capex_rev,
                'int_cov':interest_cov,
                'fcfyld':fcfyld,
                'eyld':eyld,
                'fcf':fcf
            }

            data_package = {
                'raw_data':data_to_return,
                'mappings':self.fundamental_attirbute_name_mappings
            }

            return data_package