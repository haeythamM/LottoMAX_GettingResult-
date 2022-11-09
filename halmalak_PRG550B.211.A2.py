#!/home/pi/software/bin/python3
# import modules for CGI handling
import cgi, cgitb
import re
import datetime
import urllib.request
import collections
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
webPage = urllib.request.urlopen("http://www.lottolore.com/lottomax.html")
webPageText = webPage.read( )
webPageText = webPageText.decode("UTF-8")
cgitb.enable( )
form = cgi.FieldStorage( )
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
numberlist = [""]
LottryNumlist =[""]
colour = form.getvalue('colour' )
num1   = form.getvalue('number1')
num2   = form.getvalue('number2')
num3   = form.getvalue('number3')
num4   = form.getvalue('number4')
num5   = form.getvalue('number5')
num6   = form.getvalue('number6')
num7   = form.getvalue('number7')
numberlist = (num1 , num2, num3, num4, num5, num6,num7)#user numbers List
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
print("Content-type: text/html\n\n")
print("<html>\n")
print("<head>\n")
print(" <style type=\"text/css\">")
print("input[type=\"button\"]{")
print("display: inline-block; text-decoration: none; color: #fff; font-weight: bold;")
print("background-color: #538fbe; padding: 5px 20px; font-size: 19px; border: 2px solid #2d6898;}")
print("p { text-decoration: none; color: #000000; font-weight: bold; font-size: 24px;}")
print("h1 {font-family: inherit; font-style: inherit;}")
print("h2 {color:#FFF8DC ; text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #ff00de, 0 0 70px #ff00de, 0 0 80px #ff00de, 0 0 100px #ff00de, 0 0 150px #ff00de;}")
print("</style>")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
print("<title>Python CGI Program Lottery Resolts</title>\n")
print("</head>\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
if(len(set(numberlist)) != len(numberlist)):
    print("<body bgcolor = #822626>\n")
    print("<h2>&#8594;&#32;Sorry, numbers selected must be UNIQUE&#33;</h2>" )
    print("<p></p>")
    print("<form method=\"post\" action=\"cgi-bin/halmalak_PRG550B.211.A2.py\">")
    print("</font>\n")
    print("<h5>&#169;&#8459;&#8499;.</h5>")
    print("</body>\n")
    print("</html>\n")
else :
    print("<body bgcolor='%s'>\n" % colour)
    print("<h1>Lotto Results</h1>")
    print("<p>Your Numbers are&#32;:&#32;</p>") 
    print("<p></p>")
   #++++++++++++I_did_each_number_instead_for_a_loop___in_purpose++++++++++++++++++#
    for i in num1:       
        print("<img src=\"imag/",i,".gif\" alt=\"number1\" style=\"width:1%\">", sep='' )
    print("&#32;&#124;&#32;")
    for i in num2:
        print("<img src=\"imag/",i,".gif\" alt=\"number2\" style=\"width:1%\">", sep='' )
    print("&#32;&#124;&#32;")
    for i in num3:
        print("<img src=\"imag/",i,".gif\" alt=\"number3\" style=\"width:1%\">", sep='' )
    print("&#32;&#124;&#32;")
    for i in num4:
        print("<img src=\"imag/",i,".gif\" alt=\"number4\" style=\"width:1%\">", sep='' )
    print("&#32;&#124;&#32;")
    for i in num5:
        print("<img src=\"imag/",i,".gif\" alt=\"number5\" style=\"width:1%\">", sep='' )
    print("&#32;&#124;&#32;")
    for i in num6:
        print("<img src=\"imag/",i,".gif\" alt=\"number6\" style=\"width:1%\">", sep='' )
    print("&#32;&#124;&#32;")
    for i in num7:
        print("<img src=\"imag/",i,".gif\" alt=\"number7\" style=\"width:1%\">", sep='' )
        
    print("<p>Matching numbers&#32;:&#32;</p>")
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    x ="" # string for Cleaning the strings from space (Lottery Input) ==>x  to MUCH the results
    y ="" # string for Cleaning the strings from space (User Input) ==>y  to MUCH the results
    list1 =[""]
    list2 =[""]
    xy=[""]
    digitalSame =""
    lines = webPageText.split("\n")
    for i in range(72  , 79):#===============================Numbers____From____Website=============
        LottryNumlist = re.findall(r'<b>(.*?)<\/b>',lines[i])
        xy +=(re.findall(r'<b>(.*?)<\/b>',lines[i]))
        for i in LottryNumlist: # Cleaning the strings from space (Lottery Input) ==>x  to MUCH the results
            x += i          
    del xy[0] # to delet the extra index I have , I can find another way but this is works well too for now.
    list1 = str(list(xy))
    list2 = str(list(numberlist))
    #============Check Point __For_Testing_Purpose_Only__START==============#
    #print("<p>",list1,"</p>") #Lottery numbers
    #print("<p>",list2,"</p>") #User Numbers
    #============Check Point __For_Testing_Purpose_Only__E_N_D==============#
    for i in set(xy): #======>>>to make list of same numbers<<<<====#
        if i in numberlist:
            digitalSame += i         
    print("&#32;&#124;&#32;")
    #============Check Point __For_Testing_Purpose_Only__START==============#
    #print("<p>",digitalSame,"</p>") #User Numbers
    #============Check Point __For_Testing_Purpose_Only__E_N_D==============#    
    for i in digitalSame:#======>>>to compare list of same numbers<<<<====#
        if(digitalSame != 0 ):
            print("<img src=\"imag/",i,".gif\" alt=\"number\" style=\"width:1%\ >  <img src=\"imag/",i,".gif\" alt=\"number\" style=\"width:1%\">", sep='' )
        else:
            print("Do Nothing")
    print("&#32;&#124;&#32;")
    for i in numberlist: # Cleaning the strings from space ( User Input) ==> y to MACH the results
        y += i
    ########==============================to_check_the_number_of_matching========================#
    setstring1 = set(xy) 
    setstring2 = set(numberlist)
    matchedChar  = setstring1 & setstring2
    totalMuches = str(len(matchedChar))

    if(totalMuches > '2' and totalMuches < '7' ):
        print ("<h1>Partially! you win!</h1>")
    if (totalMuches == '1' or totalMuches == '2'):
        print("\n<h3>Sorry, matches found less than 3 numbers..</h3>\n")
    if (collections.Counter(x) == collections.Counter(y)):# Now to check the user if WIN or not muched results!
        print ("<h1>Cogratulations! YOU WIN! </h1>")
    if (totalMuches == '0'):
        print("\n<h3>Sorry, no matches found ..</h3>\n")
    print("<P><br>======================</br></P>")
    print("<p>Your Choices Matching : <p>")
    print("<img src=\"imag/",totalMuches,".gif\" alt=\"number\" style=\"width:1%\ >", sep='' )
    print("<p>&#32;</p>\n")
    
    print("<P><br>======================</br></P>")
    #+++++++++++++++++++if_part_or_all_or_not_matching_DONE+++++++++++++++++++++++++++++++#  
    print("<form method=\"post\" action=\"cgi-bin/halmalak_PRG550B.211.A2.py\">")
    print("<p><input type=\"button\" value=\"Go back!\" onclick=\"history.back()\"></p>") #button - back
    print("</font>\n")
    print("<sp><h5>&#169;&#8459;&#8499;.</h5><sp>")
    print("<p></p>")
    print("<a href=\"https://www.bitsandbots.ca/danny\link text</a>")
    print("</body>\n")
    print("</html>\n")
#Haeytham Almalak
#hamalak_PRG550NAB.211.L5.txt
