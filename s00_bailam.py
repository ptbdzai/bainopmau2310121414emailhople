#region debai
"""
--- ma debai / id
get_name_in_email(email_list)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310121414emailhople

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/11knZyUvwRzU7SvL6

--- debai / problem
Viết hàm 
  get_name_in_email(email_list)
trả về tên tài khoản trong email 
Nếu email không hợp lệ tả về ERROR invaid email

--- vidu mau / testcase
Khi chay voi input                                        | Ketqua output
--------------------------------------------------------- | -----------------
get_name_in_email(['ai-btx@gmail.com'])                   | ['ai-btx']
get_name_in_email(['user1@gmail.com', 'user2@gmail.com']) | ['user1', 'user2']
get_name_in_email([])                                     | []
get_name_in_email(['abb#ccc'])                            | ['ERROR invaid email']
get_name_in_email([None])                                 | ['ERROR invaid email']
get_name_in_email([None, 'abb#ccc'])                      | ['ERROR invaid email', 'ERROR invaid email']
"""
#endregion debai

#region bailam
import re
def get_name_in_email(email_list):
  b=[None]*len(email_list)
  a=[None]*len(email_list)
  for i in range(len(email_list)):
    if email_list[i] is None:
      email_list[i]='abcd'
  for i in range(len(email_list)):
    b[i]=re.findall(r'[0-9a-zA-z_-]+@',email_list[i])
    if b[i]:
      test=0
    else:
      a[i]='ERROR invaid email'
      
  for i in range(len(email_list)):
    if a[i]!='ERROR invaid email':
      a[i]=re.findall(r'[0-9a-zA-z_-]+',b[i][0])
  for i in range(len(email_list)):
    if a[i]!='ERROR invaid email':
      a[i]=a[i][0]
  return a

  
#endregion bailam
