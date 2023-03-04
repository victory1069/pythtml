with open("py2html.html", "a") as html:
    # creating the external html tags
    html.write("<!DOCTYPE html>\n<html>\n <head><title>DISPLAYING 1 to 1,000,000</title></head><body>\n")
    for i in range(1, 1000001):
        # not putting the spaces here result in about enverything being on a stright line
        # and using <div></div> around the lines of html, renders a million+ lines of html pages to crash once you start scrolling
        result = f" {i} " 

        # i use multiple if statements instead of elif, so that when a number satisfies the 2 conditions it adds the both properties to it's html
        if i % 10 == 0:
            result = f"<strong>{result}</strong>" 
        if i % 3 == 0:
            result = f"<i>{result}</i>"
        html.write(result)
    html.write("</body>\n</html>")