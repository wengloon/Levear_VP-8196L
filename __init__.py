#!/usr/bin/env python

__author__    = 'CHANG WENG LOON'
__copyright__ = 'Copyright (c) 2017 CHANG WENG LOON'
__license__   = 'MIT'
__version__   = '0.1'

import serial
'''
########################################################################################################################
#  Header Code	#	Data Code	        #	Unit Code	#	Description                                                #
########################################################################################################################
#  FR           #	0.0001 to 165.0000	#		        #	Specific an RF frequency                                   #
########################################################################################################################
#	        	#	-20.0 to 126.0      #	(DB)	    #	Specifies an output level: dBuV [emf]	                   #
#               ########################################################################################################
#               #	-133.0 to 13.0	    #	DM	        #	Specifies an output level: dBm(50ohm)	                   #
#               ########################################################################################################
#	AP or LE    #	-134.8 to 11.2	    #	DM	        #	Specifies an output level: dBm(75ohm)	                   #
#               ########################################################################################################
#		        #	ON	                #		        #	Turns the output signal ON	                               #
#               ########################################################################################################
#		        #	OF	                #		        #	Turns the output signal OFF	                               #
########################################################################################################################
#	ZO	        #	50	                #		        #	Set the output impedance 50ohm	                           #
#               ########################################################################################################
#		        #	75	                #		        #	Set the output impedance 75ohm	                           #
########################################################################################################################
#	  	        #		                #		        #	Selects amplitude modulation	                           #
#               ########################################################################################################
#		        #	ON	                #		        #	Turns amplitude modulation ON	                           #
#               ########################################################################################################
#	        	#	OF	                #		        #	Turns amplitude modulation OFF	                           #
#   AM          ########################################################################################################
#	        	#	TO	                #		        #	Sets the AM signal to internal DDS	                       #
#               ########################################################################################################
#	        	#	XD	                #		        #	Sets the AM signal to EXT	                               #
#               ########################################################################################################
#	        	#	TD	                #		        #	Sets the AM signal to internal DDS	                       #
#               ########################################################################################################
#	        	#	0.0 TO 100	        #		        #	Specifies the AM depth in %	                               #
########################################################################################################################
#	AF	        #	0.02 TO 10.000	    #		        #	Sets the AM modulation frequency of internal DDS in kHz    #
########################################################################################################################
#	  	        #		                #		        #	Selects frequency modulation	                           #
#               ########################################################################################################
#		        #	ON	                #		        #	FM-related settings are reset	                           #
#               ########################################################################################################
#		        #	OF	                #		        #	FM-related settings are all tuned OFF	                   #
#               ########################################################################################################
#  FM           #	TO	                #		        #	Sets the FM signal to internal DDS                  	   #
#               ########################################################################################################
#		        #	XD	                #		        #	Sets the FM signal to EXT	                               #
#               ########################################################################################################
#		        #	TD	                #		        #	Sets the FM signal to internal DDS	                       #
#               ########################################################################################################
#		        #	0.0 TO 100	        #	(KZ)	    #	Specifies the FM deviation in KHz	                       #
#               ########################################################################################################
#		        #	0.0 to 127	        #	(PC)	    #	Specifies the FM stereo modulation ratio in %	           #
########################################################################################################################
#	  	        #	1	                #		        #	Sets the frequency of internal DDS to 1kHz	               #
#   TO          ########################################################################################################
#		        #	4	                #		        #	Sets the frequency of internal DDS to 400kHz	           #
########################################################################################################################
#	  	        #	1	                #		        #	Sets the modulation mode to FM MONO	                       #
#               ########################################################################################################
#		        #	2	                #		        #	Sets the modulation mode to FM STEREO L=R	               #
#               ########################################################################################################
#		        #	3	                #		        #	Sets the modulation mode to FM STEREO L	                   #
#   MS          ########################################################################################################
#		        #	4	                #		        #	Sets the modulation mode to FM STEREO R	                   #
#               ########################################################################################################
#		        #	5	                #		        #	Sets the modulation mode to FM STEREO L=-R	               #
#               ########################################################################################################
#		        #	ON	                #		        #	Turns FM modulation ON ( same features as FM-SIG key )	   #
#               ########################################################################################################
#		        #	OF	                #		        #	Turns FM modulation OFF  ( same features as FM-SIG key )   #
########################################################################################################################
#	FF	        #	0.020 to 100.000	#		        #	Sets the FM modulation frequency of internal DDS in kHz	   #
########################################################################################################################
#	  	        #	ON	                #		        #	Turns an RDS signal ON	                                   #
#               ########################################################################################################
#		        #	OF	                #		        #	Turns an RDS signal OFF	                                   #
#               ########################################################################################################
#		        #	0.0 to 10.0	        #		        #	Specifies an RDS signal level	                           #
#               ########################################################################################################
#		        #	NULL	            #		        #	Selects the pattern data Null	                           #
#               ########################################################################################################
#		        #	SC	                #		        #	Selects the pattern data Sc	                               #
#  RD           ########################################################################################################
#               #	0 to F	            #		        #	Selects a registered pattern data                          #
#               #                       #		        #	( among the pattern 0 to 15 )	                           #
#               ########################################################################################################
#               #	00 to 99	        #		        #	Selects a registered pattern data                          #
#               #	        	        #		        #   ( among the pattern 00 to 99 )	                           #
#               ########################################################################################################
#	        	#	P0	                #		        #	Sets a sub-carrier phase to 0	                           #
#               ########################################################################################################
#		        #	P9	                #		        #	Sets a sub-carrier phase to9 0	                           #
########################################################################################################################
#	RC	        #	00 to 99	        #		        #	Recalls the preset memories                                #
#               #                       #		        #	with the addresses ranging from 00 to 99	               #
########################################################################################################################
#	ST	        #	00 to 99	        #		        #	Stores settings in the preset memories                     #
#               #                       #		        #	with the addresses ranging from 00 to 99	               #
########################################################################################################################
#	  	        #	t	                #		        #	Specifies an interval time for                             #
#               #                       #               #   the currently displayed address to t(s)	                   #
#               ########################################################################################################
#		        #	t-a1-a2         	#		        #	Specifies an interval time for                             #
#               #                       #               #   the addresses a1 to a2 to t(s)	                           #
#   NT          ########################################################################################################
#		        #	t--	                #		        #	Specifies ab interval time for                         	   #
#               #                       #               #   the start to stop addresses to t(s)                        #
#               ########################################################################################################
#		        #	t(interval time): 0.10 to 60.0					                                                   #
#		        #	a1, a2(address): 00 to 99 (a1<a2)					                                               #
########################################################################################################################
#	  	        #	0	                #		        #	Sets the operation mode to Repeat up	                   #
#               ########################################################################################################
#		        #	1	                #		        #	Sets the operation mode to Single up	                   #
#   AS          ########################################################################################################
#		        #	2	                #		        #	Sets the operation mode to Repeat down	                   #
#               ########################################################################################################
#		        #	3	                #		        #	Sets the operation mode to Single down	                   #
########################################################################################################################
'''


COMMAND_LIST = {
    'RF_OUTPUT_ON': 'AP ON',
    'RF_OUTPUT_OFF': 'AP OF',
    'OUTPUT_IMPEDANCE_50_OHM': 'ZO 50',
    'OUTPUT_IMPEDANCE_75_OHM': 'ZO 75',
    'AMPLITUDE_MODULATION_SELECT': 'AM',
    'AMPLITUDE_MODULATION_ON': 'AM ON',
    'AMPLITUDE_MODULATION_OFF': 'AM OF',
    'AM_SIGNAL_TO_INTERNAL_DDS': 'AM TO',
    'AM_SIGNAL_TO_EXTERNAL': 'AM XD',
    'FREQUENCY_MODULATION_SELECT': 'FM',
    'FM_ALL_SETTING_RESET': 'FM ON',
    'FM_ALL_SETTING_OFF': 'FM OF',
    'FM_SIGNAL_TO_INTERNAL_DDS': 'FM TO',
    'FM_SIGNAL_TO_EXTERNAL': 'FM XD',
    'INTERNAL_DDS_FREQ_TO_1KHZ': 'TO 1',
    'INTERNAL_DDS_FREQ_TO_400KHZ': 'TO 4',
    'FM_MODE_MONO': 'MS 1',
    'FM_MODE_STEREO_L=R': 'MS 2',
    'FM_MODE_STEREO_L': 'MS 3',
    'FM_MODE_STEREO_R': 'MS 4',
    'FM_MODE_STEREO_L=-R': 'MS 5',
    'FM_MODE_MODULATION_ON': 'MS ON',
    'FM_MODE_MODULATION_OFF': 'MS OF',
    'RDS_SIGNAL_ON': 'RD ON',
    'RDS_SIGNAL_OFF': 'RD OF',
    'RDS_PATTERN_NULL_SELECT': 'RD NULL',
    'RDS_PATTERN_SC_SELECT': 'RD SC',
}


class SignalGenerator:

    frequency_Mhz = 0.1  # kHz
    amplitude_dbuv = 80  # dbuv
    modulation = "L=R"

#    def __init__(self, model, port):
    def __init__(self, port):
#        self.model = model
        self.port = port
        self.baudRate = 38400
        self.parity = serial.PARITY_EVEN
        self.stopBits = serial.STOPBITS_ONE
        self.bytesize = serial.EIGHTBITS
        self.timeout = 2
        self._serial = serial.Serial(port=self.port,
                                     baudrate=self.baudRate,
                                     parity=self.parity,
                                     stopbits=self.stopBits,
                                     bytesize=self.bytesize,
                                     timeout=self.timeout)

    def __del__(self):
        self._serial.close()

    def __write(self, command):
        serial.Serial.write(self._serial, bytes(command + '\r\n', 'UTF-8'))
    # end-of-method

    def set_rf_frequency_in_khz(self, frequency):
        self.__write("FR " + frequency)
    # end-of-method

    def set_amplitude_level_in_dbuv(self, power_level):
        self.__write("AP "+power_level+"(DB)")
    # end-of-method

    def set_rf_signal_on(self):
        self.__write(COMMAND_LIST['RF_OUTPUT_ON'])
    # end-of-method

    def set_rf_signal_off(self):
        self.__write(COMMAND_LIST['RF_OUTPUT_OFF'])
    # end-of-method

    def set_output_impedance_50_ohm(self):
        self.__write(COMMAND_LIST['OUTPUT_IMPEDANCE_50_OHM'])
    # end-of-method

    def set_output_impedance_75_ohm(self):
        self.__write(COMMAND_LIST['OUTPUT_IMPEDANCE_75_OHM'])
    # end-of-method

    def select_amplitude_modulation(self):
        self.__write(COMMAND_LIST['AMPLITUDE_MODULATION_SELECT'])
    # end-of-method

    def set_am_on(self):
        self.__write(COMMAND_LIST['AMPLITUDE_MODULATION_ON'])
    # end-of-method

    def set_am_off(self):
        self.__write(COMMAND_LIST['AMPLITUDE_MODULATION_OFF'])
    # end-of-method

    def set_am_signal_to_internal_dds(self):
        self.__write(COMMAND_LIST['AM_SIGNAL_TO_INTERNAL_DDS'])
    # end-of-method

    def set_am_signal_to_external(self):
        self.__write(COMMAND_LIST['AM_SIGNAL_TO_EXTERNAL'])
    # end-of-method

    def select_frequency_modulation(self):
        self.__write(COMMAND_LIST['FREQUENCY_MODULATION_SELECT'])
    # end-of-method

    def reset_all_fm_setting(self):
        self.__write(COMMAND_LIST['FM ON'])
    # end-of-method

    def off_all_fm_setting(self):
        self.__write(COMMAND_LIST['FM OF'])
    # end-of-method

    def set_fm_signal_to_internal_dds(self):
        self.__write(COMMAND_LIST['FM_SIGNAL_TO_INTERNAL_DDS'])
    # end-of-method

    def set_fm_signal_to_external(self):
        self.__write(COMMAND_LIST['FM_SIGNAL_TO_EXTERNAL'])
    # end-of-method

    def set_internal_dds_freq_to_1khz(self):
        self.__write(COMMAND_LIST['INTERNAL_DDS_FREQ_TO_1KHZ'])
    # end-of-method

    def set_internal_dds_freq_to_400khz(self):
        self.__write(COMMAND_LIST['INTERNAL_DDS_FREQ_TO_400KHZ'])

    def set_fm_mode_to_mono(self):
        self.__write(COMMAND_LIST['FM_MODE_MONO'])

    def set_fm_mode_to_stereo_left_equal_right(self):
        self.__write(COMMAND_LIST['FM_MODE_STEREO_L=R'])

    def set_fm_mode_to_stereo_left(self):
        self.__write(COMMAND_LIST['FM_MODE_STEREO_L'])

    def set_fm_mode_to_stereo_right(self):
        self.__write(COMMAND_LIST['FM_MODE_STEREO_R'])

    def set_fm_mode_to_stereo_left_equal_invert_right(self):
        self.__write(COMMAND_LIST['FM_MODE_STEREO_L=-R'])

    def fm_mode_modulation_on(self):
        self.__write(COMMAND_LIST['FM_MODE_MODULATION_ON'])

    def fm_mode_modulation_off(self):
        self.__write(COMMAND_LIST['FM_MODE_MODULATION_OFF'])

    def fm_rds_signal_on(self):
        self.__write(COMMAND_LIST['RDS_SIGNAL_ON'])

    def fm_rds_signal_off(self):
        self.__write(COMMAND_LIST['RDS_SIGNAL_OFF'])

    def select_fm_rds_null_pattern(self):
        self.__write(COMMAND_LIST['RDS_PATTERN_NULL_SELECT'])

    def select_fm_rds_sc_pattern(self):
        self.__write(COMMAND_LIST['RDS_PATTERN_SC_SELECT'])

    # end-of-method
if __name__ == '__main__':
    pass
