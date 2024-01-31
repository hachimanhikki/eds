import win32com.client
import api.handlers.constants as constants
import pythoncom


class KalkanCOMTest:
    def __init__(self) -> None:
        self.lib = win32com.client.Dispatch("KalkanCryptCOMLib.KalkanCryptCOM.2", pythoncom.CoInitialize())
        print(self.lib.Init())
        self.lib.Init()
        self.kalkan_flags = 0
        self.kalkan_flags += constants.KC_IN_BASE64
        self.kalkan_flags += constants.KC_OUT_BASE64
        self.kalkan_flags += constants.KC_SIGN_CMS
        print("FLAGS", self.kalkan_flags)
        
    def sign_data(self, data):
        out_sign = ""
        try: 
            out_sign = KalkanCOMTest.SignData('', self.kalkan_flags, data)
            print(out_sign)
        except :
            str_err, err = KalkanCOMTest.GetLastErrorString()
            if err > 0:
               print(" Error: " + str(hex(int(err))) + "\n" + str_err.replace("\n","\r\n"))
            return out_sign

    def verify_data(self, in_data, in_sign):
        out_data = ""
        out_verify_info = ""
        out_cert = ""
        out_data, out_verify_info, out_cert =  self.lib.VerifyData(" ", self.kalkan_flags, 0, in_data, in_sign)
        str_err, err = self.lib.GetLastErrorString()
        if err > 0:
            print(" Error: " + str(hex(int(err))) + "\n" + str_err.replace("\n","\r\n"))
        print(out_data + "\n" + out_verify_info + "\n" + out_cert)
        return out_data, out_verify_info, out_cert


kalkan_com_test = KalkanCOMTest()
    