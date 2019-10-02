from .. import Metric


class BSSEval(Metric):
    def __init__(self, window, hop=None):
        super(BSSEval, self).__init__(name='BSSEval', window=None, hop=None)
        self.bss_window = window
        self.bss_hop = hop if hop is not None else window

    def test_window(self, audios, rate):
        from museval.metrics import bss_eval
        if len(audios) != 2:
            raise ValueError('BSSEval needs a reference and a test signals.')
        result = bss_eval(reference_sources=audios[0].T,
                        estimated_sources=audios[1].T,
                        window=self.bss_window * rate,
                        hop=self.bss_hop * rate)
        return {'sdr': result[0], 'isr': result[1], 'sar': result[3]}


def load(window, hop=None):
    return BSSEval(window, hop)