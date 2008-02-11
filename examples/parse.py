# -*- coding: utf-8 -*-
import cssutils
import xml.dom

EXPOUT = u'''\n--- source CSS ---\n/* This is a comment */\n    body {\n        background: white;\n        top: red;\n        x: 1;\n        }\n    a { y }\n            \n\n--- simple parsing ---\n/* This is a comment */\nbody {\n    background: white;\n    top: red;\n    x: 1\n    }\n\n--- CSSParser(raiseExceptions=True) ---\n:::RAISED::: Property: No ":" after name found: u\'y \' [7:10:  ]\n'''
EXPERR = u'''CSSValue: Invalid value for CSS2 property \'top\': u\'red\'\nProperty: No CSS2 Property: \'x\'. [5:9: x]\nProperty: No ":" after name found: u\'y \' [7:10:  ]\nProperty: No property value found: u\'y \'. [7:10:  ]\nCSSStyleDeclaration: Syntax Error in Property: y \nCSSValue: Invalid value for CSS2 property \'top\': u\'red\'\nProperty: No CSS2 Property: \'x\'. [5:9: x]\n'''   

def main():
    
    css = '''/* This is a comment */
    body {
        background: white;
        top: red;
        x: 1;
        }
    a { y }
            '''
    print "\n--- source CSS ---"
    print css
    
    print "\n--- simple parsing ---"
    c1 = cssutils.parseString(css)
    print c1.cssText
    
    print "\n--- CSSParser(raiseExceptions=True) ---"
    p = cssutils.CSSParser(raiseExceptions=True)
    try:
        c2 = p.parseString(css)
    except xml.dom.DOMException, e:
        print ":::RAISED:::", e

if __name__ == '__main__':
    main()