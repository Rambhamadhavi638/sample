import pytest

from pytestframe.homepagedata import homepgdata
from pytestframe.inherit import Baseclass
from pytestframe.utility import Enters


class Testpage(Baseclass):
    def test_Homepage(self,dataload):

        log=self.getLogger()
        homepage=Enters(self.driver)
        log.info("sending keeys")
        homepage.getname().send_keys(dataload["NAME"])
        homepage.getemail().send_keys(dataload["email"])
        homepage.getpswd().send_keys(dataload["password"])
        homepage.getchk()
        homepage.shopitem()
        homepage.getadd()
        homepage.getcart()
        homepage.getcheckout()
        homepage.getCountry().send_keys("indi")
        self.VerifyText("India")
        homepage.getIndia()
        homepage.geetcheck()
        homepage.getpurchase()
        i=homepage.getmsg().text
        log.info("asserting text message"+i)
        assert i
        openwindow = self.driver.window_handles
        self.driver.switch_to.window(openwindow[0])

        self.driver.refresh()
    @pytest.fixture(params=homepgdata.gettestdata())
    def dataload(self,request):
        return request.param




