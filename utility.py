from selenium.webdriver.common.by import By


class Enters:
    name=(By.XPATH,"/html/body/app-root/form-comp/div/form/div[1]/input")
    email=(By.XPATH,"/html/body/app-root/form-comp/div/form/div[2]/input")
    pswd=(By.XPATH,"//*[@id='exampleInputPassword1']")
    chk=(By.XPATH,"//input[@id='exampleCheck1']")
    shop=(By.LINK_TEXT,"Shop")
    add=(By.XPATH,"//app-card-list[@class='row']/app-card[4]/div/div[2]/button")
    cart=(By.XPATH,"//a[@class='nav-link btn btn-primary']")
    checkout=(By.XPATH,"//button[@class='btn btn-success']")
    country=(By.ID,"country")
    india=(By.LINK_TEXT,"India")
    cheeckbox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchase=(By.XPATH,"//input[@class='btn btn-success btn-lg']")
    msg=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
    def __init__(self,driver):
        self.driver=driver


    def getname(self):
        return self.driver.find_element(*Enters.name)
    def getemail(self):
        return self.driver.find_element(*Enters.email)
    def getpswd(self):
        return self.driver.find_element(*Enters.pswd)
    def getchk(self):
        return self.driver.find_element(*Enters.chk).click()
    def shopitem(self):
        self.driver.find_element(*Enters.shop).click()

    def getadd(self):
        return self.driver.find_element(*Enters.add).click()
    def getcart(self):

        return self.driver.find_element(*Enters.cart).click()
    def getcheckout(self):
        return self.driver.find_element(*Enters.checkout).click()
    def getCountry(self):
        return self.driver.find_element(*Enters.country)
    def getIndia(self):
        return self.driver.find_element(*Enters.india).click()
    def geetcheck(self):
        return self.driver.find_element(*Enters.cheeckbox).click()
    def getpurchase(self):
        return self.driver.find_element(*Enters.purchase).click()
    def getmsg(self):
        return self.driver.find_element(*Enters.msg)