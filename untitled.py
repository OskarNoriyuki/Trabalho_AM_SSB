#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
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
from PyQt5.QtCore import QObject, pyqtSlot
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
from gnuradio import eng_notation

from gnuradio import qtgui

class untitled(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "untitled")

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
        self.source = source = 0
        self.message_samp_rate = message_samp_rate = 44100
        self.carrier_samp_rate = carrier_samp_rate = 20e06
        self.carrier_f = carrier_f = 5e05
        self.W = W = 20e03

        ##################################################
        # Blocks
        ##################################################
        # Create the options list
        self._source_options = (0, 1, 2, )
        # Create the labels list
        self._source_labels = ('Sine Wave', 'Music_ch1', 'Realtek_Audio', )
        # Create the combo box
        self._source_tool_bar = Qt.QToolBar(self)
        self._source_tool_bar.addWidget(Qt.QLabel('Input Select' + ": "))
        self._source_combo_box = Qt.QComboBox()
        self._source_tool_bar.addWidget(self._source_combo_box)
        for _label in self._source_labels: self._source_combo_box.addItem(_label)
        self._source_callback = lambda i: Qt.QMetaObject.invokeMethod(self._source_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._source_options.index(i)))
        self._source_callback(self.source)
        self._source_combo_box.currentIndexChanged.connect(
            lambda i: self.set_source(self._source_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._source_tool_bar)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_HAMMING, #wintype
            0, #fc
            carrier_samp_rate, #bw
            "modulated", #name
            1
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)



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
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            message_samp_rate, #bw
            "Message FFT", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.05)
        self.qtgui_freq_sink_x_0.set_y_axis(-160, 10)
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
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                message_samp_rate,
                W/2,
                1000,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                message_samp_rate,
                W/2,
                1000,
                firdes.WIN_HAMMING,
                6.76))
        self.hilbert_fc_1 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Program Files\\GNURadio-3.8\\bin\\wav_music.wav', True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,source,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_xx_1_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.band_pass_filter_1 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                message_samp_rate,
                100,
                20000,
                50,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_source_0 = audio.source(44100, '', True)
        self.analog_sig_source_x_1_1 = analog.sig_source_c(carrier_samp_rate, analog.GR_SIN_WAVE, carrier_f-W/2, 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(message_samp_rate, analog.GR_SIN_WAVE, W/2, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(message_samp_rate, analog.GR_COS_WAVE, 1000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.band_pass_filter_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.hilbert_fc_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_selector_0, 2))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_selector_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.hilbert_fc_1, 0), (self.blocks_multiply_xx_1_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_1_0_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "untitled")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source
        self._source_callback(self.source)
        self.blocks_selector_0.set_input_index(self.source)

    def get_message_samp_rate(self):
        return self.message_samp_rate

    def set_message_samp_rate(self, message_samp_rate):
        self.message_samp_rate = message_samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.message_samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.message_samp_rate)
        self.band_pass_filter_1.set_taps(firdes.band_pass(1, self.message_samp_rate, 100, 20000, 50, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.message_samp_rate, self.W/2, 1000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.message_samp_rate, self.W/2, 1000, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.message_samp_rate)

    def get_carrier_samp_rate(self):
        return self.carrier_samp_rate

    def set_carrier_samp_rate(self, carrier_samp_rate):
        self.carrier_samp_rate = carrier_samp_rate
        self.analog_sig_source_x_1_1.set_sampling_freq(self.carrier_samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.carrier_samp_rate)

    def get_carrier_f(self):
        return self.carrier_f

    def set_carrier_f(self, carrier_f):
        self.carrier_f = carrier_f
        self.analog_sig_source_x_1_1.set_frequency(self.carrier_f-self.W/2)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.analog_sig_source_x_1.set_frequency(self.W/2)
        self.analog_sig_source_x_1_1.set_frequency(self.carrier_f-self.W/2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.message_samp_rate, self.W/2, 1000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.message_samp_rate, self.W/2, 1000, firdes.WIN_HAMMING, 6.76))





def main(top_block_cls=untitled, options=None):

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
