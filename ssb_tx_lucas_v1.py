#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SSB TX
# Author: lucas
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
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import channels
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class ssb_tx_lucas_v1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SSB TX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SSB TX")
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

        self.settings = Qt.QSettings("GNU Radio", "ssb_tx_lucas_v1")

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
        self.transition = transition = 200
        self.signal_bandwidth = signal_bandwidth = 5000
        self.samp_rate = samp_rate = 88.2e3
        self.input_gain = input_gain = 1
        self.fstart = fstart = 200
        self.carrier_freq = carrier_freq = 30e3

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=0.4)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=2,
                decimation=1,
                taps=None,
                fractional_bw=0.4)
        self.qtgui_waterfall_sink_x_2_2 = qtgui.waterfall_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            44100, #bw
            "AudioThrottle", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_2_2.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_2_2.enable_grid(False)
        self.qtgui_waterfall_sink_x_2_2.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_2_2.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_2_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_2_2.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_2_2.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_2_2.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_2_2.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_2_2_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_2_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_2_2_win)
        self.qtgui_waterfall_sink_x_2_0_0_0 = qtgui.waterfall_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            44100, #bw
            "RX_audio_sink", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_2_0_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_2_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_2_0_0_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_2_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_2_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_2_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_2_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_2_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_2_0_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_2_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_2_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_2_0_0_0_win)
        self.qtgui_waterfall_sink_x_2 = qtgui.waterfall_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "AudioResampled", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_2.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_2.enable_grid(False)
        self.qtgui_waterfall_sink_x_2.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_2.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_2.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_2.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_2.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_2_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_2_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "FilterOutTX", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)


        self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

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
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            44100, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                44100,
                signal_bandwidth,
                transition,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                samp_rate,
                signal_bandwidth,
                transition,
                firdes.WIN_HAMMING,
                6.76))
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=0.001,
            frequency_offset=0.0,
            epsilon=1.000010,
            taps=[1.0 + 1.0j],
            noise_seed=0,
            block_tags=False)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\lucas\\OneDrive\\Documentos\\2002_ERE\\Ivan\\TrabalhoPrincipios\\Trabalho_AM_SSB\\wav_music.wav', False)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                carrier_freq + fstart,
                carrier_freq + signal_bandwidth,
                200,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                carrier_freq + fstart,
                carrier_freq + signal_bandwidth,
                200,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_sink_0_0 = audio.sink(44100, '', True)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, carrier_freq, 1, 0, 0.5)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, carrier_freq, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_waterfall_sink_x_2_2, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_2, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.audio_sink_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.qtgui_waterfall_sink_x_2_0_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ssb_tx_lucas_v1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.signal_bandwidth, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, 44100, self.signal_bandwidth, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_signal_bandwidth(self):
        return self.signal_bandwidth

    def set_signal_bandwidth(self, signal_bandwidth):
        self.signal_bandwidth = signal_bandwidth
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.signal_bandwidth, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, 44100, self.signal_bandwidth, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.signal_bandwidth, self.transition, firdes.WIN_HAMMING, 6.76))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_2.set_frequency_range(0, self.samp_rate)

    def get_input_gain(self):
        return self.input_gain

    def set_input_gain(self, input_gain):
        self.input_gain = input_gain

    def get_fstart(self):
        return self.fstart

    def set_fstart(self, fstart):
        self.fstart = fstart
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.analog_sig_source_x_0.set_frequency(self.carrier_freq)
        self.analog_sig_source_x_0_0.set_frequency(self.carrier_freq)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.carrier_freq + self.fstart, self.carrier_freq + self.signal_bandwidth, 200, firdes.WIN_HAMMING, 6.76))





def main(top_block_cls=ssb_tx_lucas_v1, options=None):

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
