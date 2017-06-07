import echoprint
import json
import unittest

class EchoprintTest(unittest.TestCase):
    def test_codegen(self):

        code = json.loads(open('test_data.json').read())

        d = echoprint.codegen(code)

        # self.assertEqual(d['code'], 'eJydz7sNAzAIRdGV-GPGiQHvP0KcypVdpDnNFUIPANDhAdWL963AC7T_YbrSnjJMocwJo7Qy5FAELdcqtpBt6Ezu38I0r4MH7e-3iroTDooJAZO7LO2AWeszaBXyXt_anXgQlcBr_QIy12Qh')
        self.assertEqual(d['code'], 'eJyd0juuQyEMRdEp2cbYZjjgz_yHEKrHy1VCkWYVW0I6CAAAFX6G4sb9LMMNtBtMN3q_cV_V2g2U32n0FUusWpTsn0h1NukQooQjImzVPwiSn-0PlsIm1pe33K9S06QOOgjw0Q7YNMEEW7U1vRvGhMzBqmpTi2B23KNkjBg83YEOblrz0Q5WwV5jmWUsXct65YES9_T3dsC-ryO8mnwCPfZ2qsC2_1F6H2QH7jzw0Q4vGHW94A==')
        self.assertEqual(str(d['version']), '4.12')

