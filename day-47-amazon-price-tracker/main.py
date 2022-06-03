import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "your@gmail.com"
PASSWORD = "your_password"

headers = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36,"
}

response = requests.get("https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B06Y1MP2PY&pd_rd_w=tnIpA&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=X6SJ056S6F72E2VMXDCS&pd_rd_r=40e29294-2b6f-4815-b2a5-33f504f80bb5&pd_rd_wg=BioHw&th=1", headers=headers)
web_page_html = response.text

soup = BeautifulSoup(web_page_html, "html.parser")

price = soup.find("span", class_= "a-offscreen")
current_price = float(price.getText().strip("$"))
print(f"The electric pot is ${current_price} now.")

if current_price < 200:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"The electric pot is ${current_price} now.")


