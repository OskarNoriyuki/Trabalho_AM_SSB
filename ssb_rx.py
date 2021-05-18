#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SSB Receiver
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class ssb_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SSB Receiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SSB Receiver")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ssb_rx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 800m
        self.variable_qtgui_range_0_0_0_0_0_0 = variable_qtgui_range_0_0_0_0_0_0 = 50
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = 0
        self.tuner = tuner = -1.3k
        self.samp_rate = samp_rate = 250000
        self.gain = gain = 10k
        self.filter_width = filter_width = 1.2e3
        self.decimate = decimate = 5
        self.center_freq = center_freq = 14.2e6
        self.agc_decay = agc_decay = 65u
        self.agc_attack = agc_attack = 100m

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 1, 10m, 800m, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'Volume', "slider", float)
        self.top_grid_layout.addWidget(self._volume_win)
        self._tuner_range = Range(-25k, 25k, 1, -1.3k, 200)
        self._tuner_win = RangeWidget(self._tuner_range, self.set_tuner, 'Tune', "slider", float)
        self.top_grid_layout.addWidget(self._tuner_win)
        self._gain_range = Range(0, 30k, 1k, 10k, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, 'Gain', "slider", float)
        self.top_grid_layout.addWidget(self._gain_win)
        self._agc_decay_range = Range(10u, 100u, 1u, 65u, 200)
        self._agc_decay_win = RangeWidget(self._agc_decay_range, self.set_agc_decay, 'AGC Decay', "counter_slider", float)
        self.top_grid_layout.addWidget(self._agc_decay_win)
        self._agc_attack_range = Range(100m, 300m, 1m, 100m, 200)
        self._agc_attack_win = RangeWidget(self._agc_attack_range, self.set_agc_attack, 'AGC Attack', "counter_slider", float)
        self.top_grid_layout.addWidget(self._agc_attack_win)
        self._variable_qtgui_range_0_0_0_0_0_0_range = Range(0, 100, 1, 50, 200)
        self._variable_qtgui_range_0_0_0_0_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_0_0_0_range, self.set_variable_qtgui_range_0_0_0_0_0_0, 'variable_qtgui_range_0_0_0_0_0_0', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_0_0_0_win)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('variable_qtgui_label_0' + ": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimate,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=16,
                decimation=10,
                taps=None,
                fractional_bw=None)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(decimate, firdes.low_pass(1, 50e3 ,filter_width-200, 300), tuner, samp_rate/decimate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(gain)
        self.blocks_multiply_const_vxx_0.set_block_alias("RF Gain")
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(16000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate/(decimate*decimate), analog.GR_COS_WAVE, filter_width, .5, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate/(decimate*decimate), analog.GR_SIN_WAVE, filter_width, .5, 0, 0)
        self.analog_agc2_xx_0 = analog.agc2_cc(agc_attack, agc_decay, .3, 1)
        self.analog_agc2_xx_0.set_max_gain(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_wavfile_source_0, 1), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ssb_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_1.set_k(self.volume)

    def get_variable_qtgui_range_0_0_0_0_0_0(self):
        return self.variable_qtgui_range_0_0_0_0_0_0

    def set_variable_qtgui_range_0_0_0_0_0_0(self, variable_qtgui_range_0_0_0_0_0_0):
        self.variable_qtgui_range_0_0_0_0_0_0 = variable_qtgui_range_0_0_0_0_0_0

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_tuner(self):
        return self.tuner

    def set_tuner(self, tuner):
        self.tuner = tuner
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.tuner)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.blocks_multiply_const_vxx_0.set_k(self.gain)

    def get_filter_width(self):
        return self.filter_width

    def set_filter_width(self, filter_width):
        self.filter_width = filter_width
        self.analog_sig_source_x_0.set_frequency(self.filter_width)
        self.analog_sig_source_x_1.set_frequency(self.filter_width)
        self.freq_xlating_fft_filter_ccc_0.set_taps(firdes.low_pass(1, 50e3 ,self.filter_width-200, 300))

    def get_decimate(self):
        return self.decimate

    def set_decimate(self, decimate):
        self.decimate = decimate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq

    def get_agc_decay(self):
        return self.agc_decay

    def set_agc_decay(self, agc_decay):
        self.agc_decay = agc_decay
        self.analog_agc2_xx_0.set_decay_rate(self.agc_decay)

    def get_agc_attack(self):
        return self.agc_attack

    def set_agc_attack(self, agc_attack):
        self.agc_attack = agc_attack
        self.analog_agc2_xx_0.set_attack_rate(self.agc_attack)





def main(top_block_cls=ssb_rx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
