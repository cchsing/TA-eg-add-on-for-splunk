import ta_eg_add_on_for_splunk_declare

import os
import sys
import time
import datetime
import json

import modinput_wrapper.base_modinput
from splunklib import modularinput as smi



import input_module_input_1 as input_module

bin_dir = os.path.basename(__file__)

'''
    Do not edit this file!!!
    This file is generated by Add-on builder automatically.
    Add your modular input logic to file input_module_input_1.py
'''
class ModInputinput_1(modinput_wrapper.base_modinput.BaseModInput):

    def __init__(self):
        if 'use_single_instance_mode' in dir(input_module):
            use_single_instance = input_module.use_single_instance_mode()
        else:
            use_single_instance = False
        super(ModInputinput_1, self).__init__("ta_eg_add_on_for_splunk", "input_1", use_single_instance)
        self.global_checkbox_fields = None

    def get_scheme(self):
        """overloaded splunklib modularinput method"""
        scheme = super(ModInputinput_1, self).get_scheme()
        scheme.title = ("Input_1")
        scheme.description = ("Go to the add-on\'s configuration UI and configure modular inputs under the Inputs menu.")
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True

        scheme.add_argument(smi.Argument("name", title="Name",
                                         description="",
                                         required_on_create=True))

        """
        For customized inputs, hard code the arguments here to hide argument detail from users.
        For other input types, arguments should be get from input_module. Defining new input types could be easier.
        """
        scheme.add_argument(smi.Argument("hostname_ip_address", title="Hostname / IP Address",
                                         description="",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("port", title="Port",
                                         description="",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("username", title="Username",
                                         description="",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("password", title="Password",
                                         description="Base64 encoded password",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("component_type", title="Component Type",
                                         description="Technology monitored by eG, e.g. Oracle Database",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("component_name_and_test_port", title="Component Name and Test Port",
                                         description="Hostname of the server monitored by eG and its corresponding test port separated comma, e.g. <hostname1>:<testPort1>, <hostname2>:<testPort2>",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("category", title="Category",
                                         description="",
                                         required_on_create=False,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("test_type", title="Test Type",
                                         description="",
                                         required_on_create=False,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("checkpoint_initial_value", title="Checkpoint Initial Value",
                                         description="checkpoint for metric / test data, %Y-%m-%d %H:%M:%S",
                                         required_on_create=True,
                                         required_on_edit=False))
        return scheme

    def get_app_name(self):
        return "TA-eg-add-on-for-splunk"

    def validate_input(self, definition):
        """validate the input stanza"""
        input_module.validate_input(self, definition)

    def collect_events(self, ew):
        """write out the events"""
        input_module.collect_events(self, ew)

    def get_account_fields(self):
        account_fields = []
        return account_fields

    def get_checkbox_fields(self):
        checkbox_fields = []
        return checkbox_fields

    def get_global_checkbox_fields(self):
        if self.global_checkbox_fields is None:
            checkbox_name_file = os.path.join(bin_dir, 'global_checkbox_param.json')
            try:
                if os.path.isfile(checkbox_name_file):
                    with open(checkbox_name_file, 'r') as fp:
                        self.global_checkbox_fields = json.load(fp)
                else:
                    self.global_checkbox_fields = []
            except Exception as e:
                self.log_error('Get exception when loading global checkbox parameter names. ' + str(e))
                self.global_checkbox_fields = []
        return self.global_checkbox_fields

if __name__ == "__main__":
    exitcode = ModInputinput_1().run(sys.argv)
    sys.exit(exitcode)
