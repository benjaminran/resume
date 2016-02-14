#!/usr/bin/env python
import xml.etree.ElementTree as ET


cv = ET.parse('cv.xml').getroot()

def expand_links(links):
    return " | ".join([str.format("\\href{{{0}}}{{{1}}}", link.attrib['url'], link.attrib['title']) for link in links.findall("./link")])

def expand_description(desc):
    output = desc.find("./general").text
    if output is None: output=""
    if len(desc.findall("./details/detail"))!=0: output+="\n\\begin{itemize*}\n" + "".join(["  \\item "+detail.text.strip()+"\n" for detail in desc.findall("./details/detail")]) + "\\end{itemize*}\n"
    return output

def get_experience():
    for exp in cv.findall("./experience/exp[category='professional']"):
        if exp.attrib['type']=='work':
            print(str.format("\\textbf{{{0}}}, {1} \\rdate{{{2}}}\\\\\n\\emph{{{3}}} \\hfill \\suplinks{{{4}}}\\\\\n{5}\\medskip\n",
                             exp.find("./employer").text,
                             exp.find("./location").text,
                             exp.find("./timespan").text,
                             exp.find("./position").text,
                             expand_links(exp.find("./links")),
                             expand_description(exp.find("./description"))))
        elif exp.attrib['type']=='hackathon':
            print(str.format("\\textbf{{{0}}}, \\rdate{{{1}}}\\\\\n\\emph{{{2}}} \\hfill \\suplinks{{{3}}}\\\\\n{4}\\medskip\n",
                             exp.find("./hackathon").text,
                             exp.find("./timespan").text,
                             "Developer",
                             expand_links(exp.find("./links")),
                             expand_description(exp.find("./description"))))

def get_projects():
    for exp in cv.findall("./experience/exp[category='project']"):
        if exp.attrib['type']=='private project':
           print(str.format("\\textbf{{{0}}} \\rdate{{{1}}}\\\\\n\\emph{{{2}}} \\hfill \\suplinks{{{3}}}\\\\\n{4}\\medskip\n",
                            exp.find("./name").text,
                            exp.find("./timespan").text,
                            exp.find("./medium").text,
                            expand_links(exp.find("./links")),
                            expand_description(exp.find("./description"))))

def get_skills():
    return "\\begin{itemize}"+"".join(["\item "+skill.attrib['name']+"\n" for skill in cv.findall("./skills/skill")])+"\\end{itemize}"

def get_languages():
    return ", ".join([language.text for language in cv.findall("./languages/language")])

def get_interests():
    return ", ".join([interest.attrib['name'] for interest in cv.findall("./interests/interest")])

if __name__=="__main__":
    get_projects()




